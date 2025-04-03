import torch
from diffsynth import ModelManager, SDXLImagePipeline


class SDXLT2I:
    def __init__(self, model_path, device="cuda", model_kwargs={}, pipeline_kwargs={}):
        model_manager = ModelManager(torch_dtype=torch.float16, device=device)
        model_manager.load_models(model_path)
        self.pipe = SDXLImagePipeline.from_model_manager(model_manager, **model_kwargs)
        self.pipeline_kwargs = pipeline_kwargs

    def __call__(self, **kwargs):
        return self.pipe(**self.pipeline_kwargs, **kwargs)

