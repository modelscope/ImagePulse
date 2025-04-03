import json, dashscope
import numpy as np
from PIL import Image


class QwenVLI2T:
    def __init__(self, api_key, model_id, prompt=""):
        dashscope.api_key = api_key
        self.model_id = model_id
        self.prompt = prompt
        
    def __call__(self, images, prompt=None, system_prompt=None):
        messages = []
        if system_prompt is not None:
            messages.append({"role": "system", "content": system_prompt})
        if prompt is None:
            prompt = self.prompt
        if not isinstance(images, list):
            images = [images]
        messages.append({"role": "user", "content": [{"text": prompt}] + [{"image": image} for image in images]})
        response = dashscope.MultiModalConversation.call(model=self.model_id, messages=messages)
        response = response["output"]["choices"][0]["message"]["content"][0]["text"]
        return response


class QwenJsonParser:
    def __init__(self):
        pass
    
    def __call__(self, text):
        text = text.strip()
        if text.startswith("```json"):
            text = text[len("```json\n"):]
        if text.endswith("```"):
            text = text[:-len("\n```")]
        json_data = json.loads(text)
        return json_data


class QwenBbox2Mask:
    def __init__(self, absolute_coordinate=False):
        self.absolute_coordinate = absolute_coordinate
    
    def __call__(self, bbox, height=1024, width=1024):
        x1, y1, x2, y2 = bbox
        image = np.zeros((height, width, 3), dtype=np.uint8)
        if self.absolute_coordinate:
            image[y1: y2, x1: x2] = 255
        else:
            image[int(y1/1000*width): int(y2/1000*width), int(x1/1000*height): int(x2/1000*height)] = 255
        image = Image.fromarray(image)
        return image


class QwenBbox2Square:
    def __init__(self):
        pass
    
    def expand(self, x1, x2, dx):
        x1, x2 = x1 - dx // 2, x2 + dx // 2 + dx % 2
        return x1, x2
    
    def shift(self, x1, x2, max_length):
        if x1 < 0:
            dx = -x1
        elif x2 > max_length:
            dx = -(x2 - max_length)
        else:
            dx = 0
        x1, x2 = x1 + dx, x2 + dx
        return x1, x2
    
    def __call__(self, bbox, height=1024, width=1024):
        x1, y1, x2, y2 = bbox
        y1, y2, x1, x2 = int(y1/1000*width), int(y2/1000*width), int(x1/1000*height), int(x2/1000*height)
        h, w = x2 - x1, y2 - y1
        if h > w:
            y1, y2 = self.expand(y1, y2, h - w)
            y1, y2 = self.shift(y1, y2, width)
        else:
            x1, x2 = self.expand(x1, x2, w - h)
            x1, x2 = self.shift(x1, x2, height)
        return {"square": (x1, y1, x2, y2)}
