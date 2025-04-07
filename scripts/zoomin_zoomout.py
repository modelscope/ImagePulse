from pulse.processor.flux_t2i import FLUXT2I
from pulse.processor.qwenvl_i2t import QwenVLI2T, QwenJsonParser, QwenBbox2Mask, QwenBbox2Square
from pulse.processor.general import ListSampler, ListPacker, ImageCropper, ImageResizer
from pulse.processor.image_cache import ImageCache
from pulse.dataset.dataset import ImageDatasetStorage
from pulse.pipeline import DataProcessUnit, DataPipeline
from pulse.dataset.diffusiondb import DiffusionDB
from diffsynth import ControlNetConfigUnit, download_models
from modelscope import dataset_snapshot_download
from tqdm import tqdm
import argparse


qwen_prompt_1 = """
Please use relative coordinates in range [0, 1000] to mark all the entities in the image and write the corresponding text descriptions for each bbox in English.

The bbox [x1, y1, x2, y2] is a square slightly larger than the corresponding object. Please ensure that the square contains a complete composition of another image as much as possible. Do not let the bbox almost cover the entire image.

Please provide the results in JSON format as follows, which can be directly loads by json.loads() in Python:
[
    {
        "bbox": [x1, y1, x2, y2],
        "description": "portrait of a man"
    },
    {
        "bbox": [x1, y1, x2, y2],
        "description": "a hat"
    },
    {
        "bbox": [x1, y1, x2, y2],
        "description": "a dog is running"
    },
    ...
]
"""
qwen_prompt_2 = """
Please provide a comprehensive and detailed description of the following image, ensuring the inclusion of the following elements:

- Main subjects and objects present in the image.
- Key visual elements, including colors, shapes, textures that stand out.
- Spatial relationships and composition, focusing on how elements are arranged and interact within the frame.
- Notable background elements that contribute to the overall context or setting.

Generate a caption according to the image so that another model can generate the image via the caption. Just return the string description, do not return anything else.
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
    "editing_instruction": "Zoom in to view the basketball in the girl's hand.",
    "reverse_editing_instruction": "Zoom out to view the girl holding the basketball.",
    "artifacts_in_image_1": false,
    "artifacts_in_image_2": false
}

{
    "image_1_caption": "an apple on the desk",
    "image_2_caption": "an apple",
    "editing_instruction": "Crop the apple from the image.",
    "reverse_editing_instruction": "Expand the image so that the enlarged version shows an apple on a table.",
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
    download_models(["FLUX.1-dev", "jasperai/Flux.1-dev-Controlnet-Upscaler"])
    
    t2i = FLUXT2I(
        model_path=[
            "models/FLUX/FLUX.1-dev/text_encoder/model.safetensors",
            "models/FLUX/FLUX.1-dev/text_encoder_2",
            "models/FLUX/FLUX.1-dev/ae.safetensors",
            "models/FLUX/FLUX.1-dev/flux1-dev.safetensors",
            "models/ControlNet/jasperai/Flux.1-dev-Controlnet-Upscaler/diffusion_pytorch_model.safetensors"
        ],
        device="cuda",
        model_kwargs={
            "controlnet_config_units": [
                    ControlNetConfigUnit(
                    processor_id="tile",
                    model_path="models/ControlNet/jasperai/Flux.1-dev-Controlnet-Upscaler/diffusion_pytorch_model.safetensors",
                    scale=0.6
                ),
            ]
        }
    )
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
            processor=QwenBbox2Square(),
            input_params={"bbox": "bbox"},
            parse_output_dict=True,
        ),
        DataProcessUnit(
            processor=QwenBbox2Mask(),
            input_params={"bbox": "square"},
            output_params=("mask",)
        ),
        DataProcessUnit(
            processor=cache,
            input_params={"image": "mask"},
            output_params=("mask_path",)
        ),
        DataProcessUnit(
            processor=ImageCropper(),
            input_params={"image": "image_1", "bbox": "square"},
            output_params=("image_cropped",)
        ),
        DataProcessUnit(
            processor=cache,
            input_params={"image": "image_cropped"},
            output_params=("image_cropped_path",)
        ),
        DataProcessUnit(
            processor=QwenVLI2T(
                api_key=args.dashscope_api_key,
                model_id=args.qwenvl_model_id,
                prompt=qwen_prompt_2
            ),
            input_params={"images": "image_cropped_path"},
            output_params=("local_description",)
        ),
        DataProcessUnit(
            processor=ImageResizer(),
            input_params={"image": "image_cropped"},
            output_params=("image_resized",)
        ),
        DataProcessUnit(
            processor=t2i,
            input_params={
                "prompt": "local_description",
                "controlnet_image": "image_resized",
                "input_image": "image_resized"
            },
            output_params=("image_2",),
            extra_input_kwargs={
                "progress_bar_cmd": lambda x: x,
                "num_inference_steps": 30,
                "denoising_strength": 0.9
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
                prompt=qwen_prompt_3
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
                image_keys=("image_1", "image_2", "image_cropped", "mask"),
                metadata_keys=(
                    "editing_instruction", "reverse_editing_instruction", "prompt", "local_description", "image_1_caption", "image_2_caption",
                    "artifacts_in_image_1", "artifacts_in_image_2", "square",
                ),
                modelscope_access_token=args.modelscope_access_token,
                modelscope_dataset_id=args.modelscope_dataset_id,
                max_num_files_per_folder=args.max_num_files_per_folder,
            ),
            input_params={
                "image_1": "image_1", "image_2": "image_2", "image_cropped": "image_cropped", "mask": "mask",
                "editing_instruction": "editing_instruction", "reverse_editing_instruction": "reverse_editing_instruction",
                "prompt": "prompt", "local_description": "local_description", "image_1_caption": "image_1_caption", "image_2_caption": "image_2_caption",
                "artifacts_in_image_1": "artifacts_in_image_1", "artifacts_in_image_2": "artifacts_in_image_2",
                "square": "square"
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
