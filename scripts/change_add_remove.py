from pulse.processor.flux_t2i import FLUXT2I
from pulse.processor.qwenvl_i2t import QwenVLI2T, QwenJsonParser, QwenBbox2Mask
from pulse.processor.general import ListSampler, TextFormater, ListPacker
from pulse.processor.preference import ImagePreferenceModel
from pulse.processor.image_cache import ImageCache
from pulse.dataset.dataset import ImageDatasetStorage
from pulse.pipeline import DataProcessUnit, DataPipeline
from pulse.dataset.diffusiondb import DiffusionDB
from diffsynth import ControlNetConfigUnit, download_models
from diffsynth.extensions.ImageQualityMetric import download_preference_model
from modelscope import dataset_snapshot_download
from tqdm import tqdm
import argparse


qwen_prompt_1 = """
Please use relative coordinates in range [0, 1000] to mark all the entities in the image and write the corresponding text descriptions for each bbox in English.

Please provide the results in JSON format as follows, which can be directly loads by json.loads() in Python:
[
    {
        "bbox": [x1, y1, x2, y2],
        "description": "a dog is running"
    },
    {
        "bbox": [x1, y1, x2, y2],
        "description": "a red car"
    },
    {
        "bbox": [x1, y1, x2, y2],
        "description": "black hair"
    },
    ...
]
"""
qwen_prompt_2 = """
There is an image, and the full text description of this image is "%s" The area in the image (%s) indicates "%s".

Now I need to modify this part to reflect other content in the image. Please write a piece of randomly modified text (local_description) describing the localized image content after the modification; as well as another piece of text (global_description) describing the overall image content after the modification." 

Please provide the results in JSON format as follows, which can be directly loads by json.loads() in Python:
{
    "original_local_description": "...",
    "original_global_description": "...",
    "local_description": "...",
    "global_description": "..."
}

Here are some examples:
{
    "original_local_description": "a basketball",
    "original_global_description": "a girl holding a basketball",
    "local_description": "a Teddy bear doll",
    "global_description": "a girl holding a Teddy bear doll"
}

{
    "original_local_description": "an apple",
    "original_global_description": "an apple on the desk",
    "local_description": "a banana",
    "global_description": "a banana on the desk"
}
"""
qwen_prompt_3 = """
Here are two images, denoted as image_1 and image_2

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
    "image_1_caption": "an apple on the desk",
    "image_2_caption": "a desk",
    "editing_instruction": "Remove the apple.",
    "reverse_editing_instruction": "Add an apple on the desk.",
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
    dataset_snapshot_download("AI-ModelScope/diffusiondb", allow_file_pattern=["metadata-large.parquet"], cache_dir="./data")
    download_models(["FLUX.1-dev", "alimama-creative/FLUX.1-dev-Controlnet-Inpainting-Beta"])
    download_preference_model("MPS", cache_dir="./models")
    
    t2i = FLUXT2I(
        model_path=[
            "models/FLUX/FLUX.1-dev/text_encoder/model.safetensors",
            "models/FLUX/FLUX.1-dev/text_encoder_2",
            "models/FLUX/FLUX.1-dev/ae.safetensors",
            "models/FLUX/FLUX.1-dev/flux1-dev.safetensors",
            "models/ControlNet/alimama-creative/FLUX.1-dev-Controlnet-Inpainting-Beta/diffusion_pytorch_model.safetensors"
        ],
        device="cuda",
        model_kwargs={
            "controlnet_config_units": [
                ControlNetConfigUnit(
                    processor_id="inpaint",
                    model_path="models/ControlNet/alimama-creative/FLUX.1-dev-Controlnet-Inpainting-Beta/diffusion_pytorch_model.safetensors",
                    scale=0.9
                ),
            ]
        }
    )
    preference_model = ImagePreferenceModel("MPS", cache_dir="./models", device="cuda")
    cache = ImageCache(cache_dir=args.cache_dir)
    
    dataset = DiffusionDB("data/AI-ModelScope/diffusiondb/metadata-large.parquet", shuffle=True, num_data=args.num_data)

    pipe = DataPipeline(units=[
        DataProcessUnit(
            processor=t2i,
            input_params={"prompt": "prompt"},
            output_params=("image_1",),
            extra_input_kwargs={"progress_bar_cmd": lambda x: x}
        ),
        DataProcessUnit(
            processor=cache,
            input_params={"image": "image_1"},
            output_params=("image_1_path",)
        ),
        DataProcessUnit(
            processor=QwenVLI2T(
                api_key=args.dashscope_api_key,
                model_id=args.qwenvl_model_id,
                prompt=qwen_prompt_1
            ),
            input_params={"images": "image_1_path"},
            output_params=("grounding_results_str",)
        ),
        DataProcessUnit(
            processor=QwenJsonParser(),
            input_params={"text": "grounding_results_str"},
            output_params=("grounding_results_list",)
        ),
        DataProcessUnit(
            processor=ListSampler(),
            input_params={"ls": "grounding_results_list"},
            parse_output_dict=True,
        ),
        DataProcessUnit(
            processor=QwenBbox2Mask(),
            input_params={"bbox": "bbox"},
            output_params=("mask",)
        ),
        DataProcessUnit(
            processor=cache,
            input_params={"image": "mask"},
            output_params=("mask_path",)
        ),
        DataProcessUnit(
            processor=TextFormater(template=qwen_prompt_2),
            input_params={"prompt": "prompt", "bbox": "bbox", "description": "description"},
            output_params=("editing_prompt_for_qwen",)
        ),
        DataProcessUnit(
            processor=QwenVLI2T(
                api_key=args.dashscope_api_key,
                model_id=args.qwenvl_model_id,
            ),
            input_params={"images": "image_1_path", "prompt": "editing_prompt_for_qwen"},
            output_params=("editing_str",)
        ),
        DataProcessUnit(
            processor=QwenJsonParser(),
            input_params={"text": "editing_str"},
            parse_output_dict=True,
        ),
        DataProcessUnit(
            processor=t2i,
            input_params={
                "prompt": "local_description",
                "controlnet_image": "image_1",
                "controlnet_inpaint_mask": "mask"
            },
            output_params=("image_2",),
            extra_input_kwargs={"progress_bar_cmd": lambda x: x, "num_inference_steps": 50}
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
                prompt=qwen_prompt_3,
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
            processor=preference_model,
            input_params={"image": "image_1", "prompt": "image_1_caption"},
            output_params=("image_1_preference_score",)
        ),
        DataProcessUnit(
            processor=preference_model,
            input_params={"image": "image_2", "prompt": "image_2_caption"},
            output_params=("image_2_preference_score",)
        ),
        DataProcessUnit(
            processor=ImageDatasetStorage(
                target_dir=args.target_dir,
                image_keys=("image_1", "image_2", "mask"),
                metadata_keys=(
                    "editing_instruction", "reverse_editing_instruction", "prompt", "image_1_caption", "image_2_caption",
                    "image_1_preference_score", "image_2_preference_score", "artifacts_in_image_1", "artifacts_in_image_2"
                ),
                modelscope_access_token=args.modelscope_access_token,
                modelscope_dataset_id=args.modelscope_dataset_id,
                max_num_files_per_folder=args.max_num_files_per_folder,
            ),
            input_params={
                "image_1": "image_1", "image_2": "image_2", "mask": "mask",
                "editing_instruction": "editing_instruction", "reverse_editing_instruction": "reverse_editing_instruction",
                "prompt": "prompt", "image_1_caption": "image_1_caption", "image_2_caption": "image_2_caption",
                "image_1_preference_score": "image_1_preference_score", "image_2_preference_score": "image_2_preference_score",
                "artifacts_in_image_1": "artifacts_in_image_1", "artifacts_in_image_2": "artifacts_in_image_2",
            },
            output_params=("metadata_path"),
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
