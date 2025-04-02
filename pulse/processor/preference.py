from diffsynth.extensions.ImageQualityMetric import download_preference_model, load_preference_model, preference_model_id


class ImagePreferenceModel:
    def __init__(self, model_name: preference_model_id, cache_dir="./models", device="cuda"):
        path = download_preference_model(model_name, cache_dir=cache_dir)
        self.preference_model = load_preference_model(model_name, device=device, path=path)
        
    def __call__(self, image, prompt):
        return self.preference_model.score(image, prompt)[0]
