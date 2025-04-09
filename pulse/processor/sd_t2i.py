import torch
from diffsynth import ModelManager, SDImagePipeline


class SDT2I:
    def __init__(self, model_path, device="cuda", textual_inversions=[], model_kwargs={}, pipeline_kwargs={}):
        model_manager = ModelManager(torch_dtype=torch.float16, device=device)
        model_manager.load_models(model_path)
        model_manager.load_lora("models/lora/add_detail.safetensors", lora_alpha=-4)
        self.pipe = SDImagePipeline.from_model_manager(model_manager, **model_kwargs)
        self.pipe.prompter.load_textual_inversions(textual_inversions)
        self.pipeline_kwargs = pipeline_kwargs

    def __call__(self, **kwargs):
        return self.pipe(**self.pipeline_kwargs, **kwargs)

