import torch

class FaceDataSelector:
    def __init__(self):
        pass
    
    def __call__(self, metadata):
        descriptions = [data for data in metadata["descriptions"] if data["gender"] == metadata["gender_in_image"]]
        return descriptions[0]["description"], descriptions[1 if len(descriptions) > 1 else 0]["description"]