import torch
from diffsynth import ModelManager, FluxImagePipeline


class FLUXT2I:
    def __init__(self, model_path, device="cuda", model_kwargs={}, pipeline_kwargs={}):
        model_manager = ModelManager(torch_dtype=torch.bfloat16, device=device)
        model_manager.load_models(model_path)
        self.pipe = FluxImagePipeline.from_model_manager(model_manager, **model_kwargs)
        self.pipeline_kwargs = pipeline_kwargs

    def __call__(self, **kwargs):
        return self.pipe(**self.pipeline_kwargs, **kwargs)

