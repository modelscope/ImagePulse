from pulse.processor.flux_t2i import FLUXT2I
from pulse.processor.qwenvl_i2t import QwenVLI2T, QwenJsonParser, QwenBbox2Mask, QwenBbox2Square
from pulse.processor.general import ListSampler, ListPacker, ImageCropper, ImageResizer, TextFormater
from pulse.processor.image_cache import ImageCache
from pulse.processor.preference import ImagePreferenceModel
from pulse.processor.style import RandomPromptStyler
from pulse.processor.sdxl_t2i import SDXLT2I
from pulse.dataset.dataset import ImageDatasetStorage
from pulse.pipeline import DataProcessUnit, DataPipeline
from pulse.dataset.diffusiondb import DiffusionDB
from diffsynth import ControlNetConfigUnit, download_models
from diffsynth.extensions.ImageQualityMetric import download_preference_model
from modelscope import dataset_snapshot_download
from tqdm import tqdm
import argparse


qwen_prompt_1 = """
Please describe the content of the image in concise text, focusing only on the elements present in the image without discussing its style.

Here are some examples:
* A dog is running
* Red and blue flowers in a garden
* An apple and a cup on the desk

Just return the string description, do not return anything else.
"""
qwen_prompt_2 = """
Here are two images, denoted as image_1 and image_2

Generate a caption (image_1_caption and image_2_caption) according to each image so that another image generation model can generate the image via the caption.

Write image editing instructions (editing_instruction) to edit from image_1 to image_2. Write another image editing instructions (reverse_editing_instruction) to edit from image 2 to image 1. Do not say "change back" or "transform back" in the instructions. Please ensure that the editing instructions emphasize the style of the image.

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
    "image_1_caption": "a photo of a girl holding a basketball.",
    "image_2_caption": "an oil painting of a teenage girl holding a basketball.",
    "editing_instruction": "transform the photo into an oil painting style.",
    "reverse_editing_instruction": "generate a realistic scene based on the content of this oil painting.",
    "artifacts_in_image_1": false,
    "artifacts_in_image_2": false
}

{
    "image_1_caption": "flat illustration, anime style, featuring an orange kitten.",
    "image_2_caption": "highly outlined anime illustration, featuring an orange kitten.",
    "editing_instruction": "transform the style of the image to enhance the line definition.",
    "reverse_editing_instruction": "transform the style of the image to make it appear more flat.",
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
    args = parser.parse_args()
    return args
    
    
def initialize(args):
    dataset_snapshot_download("AI-ModelScope/diffusiondb", allow_file_pattern=["metadata-large.parquet"], cache_dir="./data")
    download_models(["FLUX.1-dev", "InstantX/FLUX.1-dev-IP-Adapter", "StableDiffusionXL_v1", "IP-Adapter-SDXL", "ControlNet_union_sdxl_promax"])
    download_preference_model("MPS", cache_dir="./models")
    
    t2i = FLUXT2I(
        model_path=[
            "models/FLUX/FLUX.1-dev/text_encoder/model.safetensors",
            "models/FLUX/FLUX.1-dev/text_encoder_2",
            "models/FLUX/FLUX.1-dev/ae.safetensors",
            "models/FLUX/FLUX.1-dev/flux1-dev.safetensors",
            "models/IpAdapter/InstantX/FLUX.1-dev-IP-Adapter/ip-adapter.bin",
            "models/IpAdapter/InstantX/FLUX.1-dev-IP-Adapter/image_encoder",
        ],
        device="cuda",
    )
    instant_style = SDXLT2I(
        model_path=[
            "models/stable_diffusion_xl/sd_xl_base_1.0.safetensors",
            "models/IpAdapter/stable_diffusion_xl/image_encoder/model.safetensors",
            "models/IpAdapter/stable_diffusion_xl/ip-adapter_sdxl.bin",
            "models/ControlNet/controlnet_union/diffusion_pytorch_model_promax.safetensors",
        ],
        device="cuda",
        model_kwargs={
            "controlnet_config_units": [
                ControlNetConfigUnit(
                    processor_id="canny",
                    model_path="models/ControlNet/controlnet_union/diffusion_pytorch_model_promax.safetensors",
                    scale=0.6
                )
            ]
        },
        pipeline_kwargs={
            "negative_prompt": "text, watermark, lowres, low quality, worst quality, deformed, glitch, low contrast, noisy, saturation, blurry",
            "cfg_scale": 5,
            "height": 1024,
            "width": 1024,
            "num_inference_steps": 50,
            "ipadapter_use_instant_style": True
        }
    )
    preference_model = ImagePreferenceModel("MPS", cache_dir="./models", device="cuda")
    cache = ImageCache(cache_dir=args.cache_dir)
    
    dataset = DiffusionDB("data/AI-ModelScope/diffusiondb/metadata-large.parquet", shuffle=True)

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
            output_params=("image_content_description",)
        ),
        DataProcessUnit(
            processor=RandomPromptStyler(),
            input_params={"prompt": "image_content_description"},
            output_params=("image_content_style_description",)
        ),
        DataProcessUnit(
            processor=t2i,
            input_params={"prompt": "image_content_style_description"},
            output_params=("image_2",),
            extra_input_kwargs={"progress_bar_cmd": lambda x: x}
        ),
        DataProcessUnit(
            processor=cache,
            input_params={"image": "image_2"},
            output_params=("image_2_path",)
        ),
        DataProcessUnit(
            processor=ListPacker(),
            input_params={"image": "image_2"},
            output_params=("ipadapter_images",)
        ),
        DataProcessUnit(
            processor=instant_style,
            input_params={
                "prompt": "image_content_style_description",
                "controlnet_image": "image_1",
                "ipadapter_images": "ipadapter_images",
            },
            output_params=("image_3",),
            extra_input_kwargs={"progress_bar_cmd": lambda x: x}
        ),
        DataProcessUnit(
            processor=cache,
            input_params={"image": "image_3"},
            output_params=("image_3_path",)
        ),
        DataProcessUnit(
            processor=t2i,
            input_params={
                "prompt": "image_content_style_description",
                "input_image": "image_3",
                "ipadapter_images": "ipadapter_images",
            },
            output_params=("image_4",),
            extra_input_kwargs={
                "progress_bar_cmd": lambda x: x,
                "denoising_strength": 0.6,
                "num_inference_steps": 50
            }
        ),
        DataProcessUnit(
            processor=cache,
            input_params={"image": "image_4"},
            output_params=("image_4_path",)
        ),
        DataProcessUnit(
            processor=ListPacker(),
            input_params={"image_1_path": "image_1_path", "image_4_path": "image_4_path"},
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
            processor=preference_model,
            input_params={"image": "image_1", "prompt": "image_1_caption"},
            output_params=("image_1_preference_score",)
        ),
        DataProcessUnit(
            processor=preference_model,
            input_params={"image": "image_4", "prompt": "image_2_caption"},
            output_params=("image_4_preference_score",)
        ),
        DataProcessUnit(
            processor=ImageDatasetStorage(
                target_dir=args.target_dir,
                image_keys=("image_1", "image_2", "image_3", "image_4"),
                metadata_keys=(
                    "editing_instruction", "reverse_editing_instruction",
                    "prompt", "image_content_description", "image_content_style_description",
                    "image_1_caption", "image_4_caption", "artifacts_in_image_1", "artifacts_in_image_4",
                    "image_1_preference_score", "image_4_preference_score"
                )
            ),
            input_params={
                "image_1": "image_1", "image_2": "image_2", "image_3": "image_3", "image_4": "image_4",
                "editing_instruction": "editing_instruction", "reverse_editing_instruction": "reverse_editing_instruction",
                "prompt": "prompt", "image_content_description": "image_content_description", "image_content_style_description": "image_content_style_description",
                "image_1_caption": "image_1_caption", "image_4_caption": "image_2_caption",
                "artifacts_in_image_1": "artifacts_in_image_1", "artifacts_in_image_4": "artifacts_in_image_2",
                "image_1_preference_score": "image_1_preference_score", "image_4_preference_score": "image_4_preference_score"
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
