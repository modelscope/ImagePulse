import torch
import numpy as np
from PIL import Image


class ListSampler:
    def __init__(self):
        pass
    
    def __call__(self, ls):
        i = torch.randint(0, len(ls), size=(1,)).tolist()[0]
        return ls[i]


class TextFormater:
    def __init__(self, template):
        self.template = template
        
    def __call__(self, *args, **kwargs):
        args = tuple(str(i) for i in args) + tuple(str(kwargs[i]) for i in kwargs)
        return self.template % args


class ListPacker:
    def __init__(self):
        pass
    
    def __call__(self, *args, **kwargs):
        ls = list(i for i in args) + list(kwargs[i] for i in kwargs)
        return ls


class ImageCropper:
    def __init__(self):
        pass
    
    def __call__(self, bbox, image):
        x1, y1, x2, y2 = bbox
        image = np.array(image)
        image = image[y1: y2, x1: x2]
        image = Image.fromarray(image)
        return image
    
    
class ImageResizer:
    def __init__(self):
        pass
    
    def __call__(self, image, height=1024, width=1024):
        return image.resize((width, height))
