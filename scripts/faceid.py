from pulse.processor.flux_t2i import FLUXT2I
from pulse.processor.sd_t2i import SDT2I
from pulse.processor.qwenvl_i2t import QwenVLI2T, QwenJsonParser, QwenBbox2Mask
from pulse.processor.general import ListSampler, TextFormater, ListPacker, ImageResizer
from pulse.processor.preference import ImagePreferenceModel
from pulse.processor.image_cache import ImageCache
from pulse.processor.face import FaceDataSelector
from pulse.dataset.dataset import ImageDatasetStorage, ImageDataset
from pulse.pipeline import DataProcessUnit, DataPipeline
from pulse.dataset.diffusiondb import DiffusionDB
from diffsynth import ControlNetConfigUnit, download_models
from diffsynth.extensions.ImageQualityMetric import download_preference_model
from modelscope import dataset_snapshot_download
from tqdm import tqdm
import argparse, os, io
import pandas as pd
from PIL import Image


qwen_prompt_1 = """
Here are some image descriptions. Please select those (`descriptions`) that describe a single person and identify the gender in each image description.

1. %s
2. %s
3. %s
4. %s
5. %s
6. %s
7. %s
8. %s
9. %s
10. %s

Next, identify the gender of the person in the image (`gender_in_image`).

Please provide the results in JSON format as follows, which can be directly loads by json.loads() in Python:
{
    "descriptions": [
        {
            "description": "a girl holding an apple",
            "gender": "female",
        },
        {
            "description": "a man is reading a book",
            "gender": "male",
        },
        ...
    ]
    "gender_in_image": "male",
}
"""
qwen_prompt_2 = """
Here are two images of the same person, denoted as image_1 and image_2

Generate a caption (image_1_caption and image_2_caption) according to each image so that another image generation model can generate the image via the caption.

Write image editing instructions (editing_instruction) to edit from image_1 to image_2. Write another image editing instructions (reverse_editing_instruction) to edit from image 2 to image 1. Do not say "change back" or "transform back" in the instructions.

Determine whether there are artifacts (e.g., distorted limbs, extra fingers, abnormal composition) in Image 1 and Image 2, denoted by artifacts_in_image_1 and artifacts_in_image_2.

Please provide the results in JSON format as follows, which can be directly loads by json.loads() in Python:
{
    "image_1_caption": "...",
    "image_2_caption": "...",
    "editing_instruction": "...",
    "reverse_editing_instruction": "...",
    "artifacts_in_image_1": ...,
    "artifacts_in_image_2": ...
}

Here are some examples:
{
    "image_1_caption": "a girl holding a basketball",
    "image_2_caption": "a girl holding a Teddy bear doll",
    "editing_instruction": "Change the basketball to a teddy bear.",
    "reverse_editing_instruction": "Change the teddy bear to a basketball.",
    "artifacts_in_image_1": false,
    "artifacts_in_image_2": false
}

{
    "image_1_caption": "a man is walking on the street",
    "image_2_caption": "a man is sitting on a chair",
    "editing_instruction": "Let the man sit down.",
    "reverse_editing_instruction": "Let the man walk.",
    "artifacts_in_image_1": false,
    "artifacts_in_image_2": true
}
"""


def parse_args():
    parser = argparse.ArgumentParser(description="Dataset generation script: Change, add & remove.")
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
    # dataset_snapshot_download("AI-ModelScope/diffusiondb", allow_file_pattern=["metadata-large.parquet"], cache_dir="./data")
    # dataset_snapshot_download("AI-ModelScope/celeb-a-hq_training_untransformed_faces", allow_file_pattern=["*.parquet"], cache_dir="./data")
    # download_models(["FLUX.1-dev", "InfiniteYou"])
    
    for file_name in os.listdir("data/AI-ModelScope/celeb-a-hq_training_untransformed_faces/data"):
        if file_name.endswith(".parquet"):
            if not os.path.exists(f"data/AI-ModelScope/celeb-a-hq_training_untransformed_faces/data/{file_name}_images"):
                data = pd.read_parquet(f"data/AI-ModelScope/celeb-a-hq_training_untransformed_faces/data/{file_name}")
                os.makedirs(f"data/AI-ModelScope/celeb-a-hq_training_untransformed_faces/data/{file_name}_images")
                for image_id, image_data in enumerate(tqdm(data["image"], desc=file_name)):
                    image = image_data["bytes"]
                    image = Image.open(io.BytesIO(image))
                    image.save(f"data/AI-ModelScope/celeb-a-hq_training_untransformed_faces/data/{file_name}_images/{image_id}.png")
    
    t2i = FLUXT2I(
        model_path=[
            "models/FLUX/FLUX.1-dev/text_encoder/model.safetensors",
            "models/FLUX/FLUX.1-dev/text_encoder_2",
            "models/FLUX/FLUX.1-dev/ae.safetensors",
            "models/FLUX/FLUX.1-dev/flux1-dev.safetensors",
            [
                "models/InfiniteYou/InfuseNetModel/diffusion_pytorch_model-00001-of-00002.safetensors",
                "models/InfiniteYou/InfuseNetModel/diffusion_pytorch_model-00002-of-00002.safetensors"
            ],
            "models/InfiniteYou/image_proj_model.bin",
        ],
        device="cuda",
        model_kwargs={
            "controlnet_config_units": [
                ControlNetConfigUnit(
                    processor_id="none",
                    model_path=[
                        'models/InfiniteYou/InfuseNetModel/diffusion_pytorch_model-00001-of-00002.safetensors',
                        'models/InfiniteYou/InfuseNetModel/diffusion_pytorch_model-00002-of-00002.safetensors'
                    ],
                    scale=1.0
                )
            ]
        }
    )
    cache = ImageCache(cache_dir=args.cache_dir)
    
    dataset = DiffusionDB("data/AI-ModelScope/diffusiondb/metadata-large.parquet", shuffle=True, num_data=args.num_data, multi_prompt=True, num_prompt=10)
    face_generator = ImageDataset("data/AI-ModelScope/celeb-a-hq_training_untransformed_faces")

    pipe = DataPipeline(units=[
        DataProcessUnit(
            processor=TextFormater(template=qwen_prompt_1),
            input_params={"text_list": "prompt"},
            output_params=("qwen_prompt_for_prompt_selection",)
        ),
        DataProcessUnit(
            processor=cache,
            input_params={"image": "image_face"},
            output_params=("image_face_path",)
        ),
        DataProcessUnit(
            processor=QwenVLI2T(
                api_key=args.dashscope_api_key,
                model_id=args.qwenvl_model_id,
                prompt=qwen_prompt_1
            ),
            input_params={"images": "image_face_path", "prompt": "qwen_prompt_for_prompt_selection"},
            output_params=("face_prompts_str",)
        ),
        DataProcessUnit(
            processor=QwenJsonParser(),
            input_params={"text": "face_prompts_str"},
            output_params=("face_prompts",)
        ),
        DataProcessUnit(
            processor=FaceDataSelector(),
            input_params={"metadata": "face_prompts"},
            output_params=("prompt_1", "prompt_2")
        ),
        
        DataProcessUnit(
            processor=t2i,
            input_params={"infinityou_id_image": "image_face", "prompt": "prompt_1"},
            output_params=("image_1",),
            extra_input_kwargs={
                "progress_bar_cmd": lambda x: x,
                "num_inference_steps": 50,
                "infinityou_guidance": 1.0,
            }
        ),
        DataProcessUnit(
            processor=cache,
            input_params={"image": "image_1"},
            output_params=("image_1_path",)
        ),

        DataProcessUnit(
            processor=t2i,
            input_params={"infinityou_id_image": "image_face", "prompt": "prompt_2"},
            output_params=("image_2",),
            extra_input_kwargs={
                "progress_bar_cmd": lambda x: x,
                "num_inference_steps": 50,
                "infinityou_guidance": 1.0,
            }
        ),
        DataProcessUnit(
            processor=cache,
            input_params={"image": "image_2"},
            output_params=("image_2_path",)
        ),
        
        DataProcessUnit(
            processor=ListPacker(),
            input_params={"image_1_path": "image_1_path", "image_2_path": "image_2_path"},
            output_params=("image_list",)
        ),
        
        DataProcessUnit(
            processor=QwenVLI2T(
                api_key=args.dashscope_api_key,
                model_id=args.qwenvl_model_id,
                prompt=qwen_prompt_2
            ),
            input_params={"images": "image_list"},
            output_params=("generated_instructions",)
        ),
        DataProcessUnit(
            processor=QwenJsonParser(),
            input_params={"text": "generated_instructions"},
            parse_output_dict=True,
        ),
        DataProcessUnit(
            processor=ImageDatasetStorage(
                target_dir=args.target_dir,
                image_keys=("image_face", "image_1", "image_2"),
                metadata_keys=(
                    "editing_instruction", "reverse_editing_instruction", "prompt_1", "prompt_2", "image_1_caption", "image_2_caption",
                    "artifacts_in_image_1", "artifacts_in_image_2"
                )
            ),
            input_params={
                "image_face": "image_face", "image_1": "image_1", "image_2": "image_2",
                "editing_instruction": "editing_instruction", "reverse_editing_instruction": "reverse_editing_instruction",
                "prompt_1": "prompt_1", "prompt_2": "prompt_2", "image_1_caption": "image_1_caption", "image_2_caption": "image_2_caption",
                "artifacts_in_image_1": "artifacts_in_image_1", "artifacts_in_image_2": "artifacts_in_image_2",
            },
            output_params=("metadata_path")
        )
    ])
    return dataset, pipe, face_generator


if __name__ == "__main__":
    args = parse_args()
    dataset, pipe, face_generator = initialize(args)
    for data_id, data in enumerate(tqdm(dataset)):
        data["image_face"] = face_generator[0]
        pipe(data, ignore_errors=True)
        if (data_id + 1) % 100 == 0:
            pipe.report_log()
