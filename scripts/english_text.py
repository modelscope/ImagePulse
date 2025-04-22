from pulse.processor.flux_t2i import FLUXT2I
from pulse.dataset.anytext import AnyText
from pulse.dataset.dataset import ImageDatasetStorage
from pulse.pipeline import DataProcessUnit, DataPipeline
from diffsynth import download_models
from diffsynth.extensions.ImageQualityMetric import download_preference_model
from modelscope import dataset_snapshot_download
from tqdm import tqdm
import argparse, os, zipfile



def parse_args():
    parser = argparse.ArgumentParser(description="Dataset generation script: Style Transfer.")
    parser.add_argument(
        "--target_dir",
        type=str,
        default="data/dataset",
        required=True,
        help="Path to save dataset.",
    )
    parser.add_argument(
        "--cache_dir",
        type=str,
        default="data/cache",
        help="Path to save cache files.",
    )
    parser.add_argument(
        "--dashscope_api_key",
        type=str,
        default="",
        help="Dashscope api key.",
    )
    parser.add_argument(
        "--qwenvl_model_id",
        type=str,
        default="qwen-vl-max-0809",
        help="QwenVL model id.",
    )
    parser.add_argument(
        "--modelscope_access_token",
        type=str,
        default=None,
        help="Modelscope access token",
    )
    parser.add_argument(
        "--modelscope_dataset_id",
        type=str,
        default=None,
        help="Modelscope Dataset ID",
    )
    parser.add_argument(
        "--num_data",
        type=int,
        default=100000,
        help="Number of data samples",
    )
    parser.add_argument(
        "--max_num_files_per_folder",
        type=int,
        default=5000,
        help="Max number of files per folder",
    )
    args = parser.parse_args()
    return args
    
    
def initialize(args):
    dataset_snapshot_download("iic/AnyWord-3M", allow_file_pattern=["anytext2_json_files.zip"], cache_dir="./data")
    if "TextEn" not in os.listdir("data"):
        os.makedirs("data/TextEn")
        with zipfile.ZipFile("data/iic/AnyWord-3M/anytext2_json_files.zip", 'r') as f:
            f.extractall("data/TextEn")
    download_models(["FLUX.1-dev"])
    
    t2i = FLUXT2I(
        model_path=[
            "models/FLUX/FLUX.1-dev/text_encoder/model.safetensors",
            "models/FLUX/FLUX.1-dev/text_encoder_2",
            "models/FLUX/FLUX.1-dev/ae.safetensors",
            "models/FLUX/FLUX.1-dev/flux1-dev.safetensors",
        ],
        device="cuda",
    )
    
    dataset = AnyText("data/TextEn/anytext2_json_files/laion_word/data_v1.2b.json", shuffle=True, num_data=args.num_data)

    pipe = DataPipeline(units=[
        DataProcessUnit(
            processor=t2i,
            input_params={"prompt": "prompt"},
            output_params=("image_1",),
            extra_input_kwargs={"progress_bar_cmd": lambda x: x}
        ),
        DataProcessUnit(
            processor=ImageDatasetStorage(
                target_dir=args.target_dir,
                image_keys=("image_1",),
                metadata_keys=("prompt",),
                modelscope_access_token=args.modelscope_access_token,
                modelscope_dataset_id=args.modelscope_dataset_id,
                max_num_files_per_folder=args.max_num_files_per_folder,
            ),
            input_params={
                "image_1": "image_1", "prompt": "prompt",
            },
            output_params=("metadata_path")
        )
    ])
    return dataset, pipe


if __name__ == "__main__":
    args = parse_args()
    dataset, pipe = initialize(args)
    for data_id, data in enumerate(tqdm(dataset)):
        pipe(data, ignore_errors=True)
        if (data_id + 1) % 100 == 0:
            pipe.report_log()
