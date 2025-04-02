import os, time, shutil
from PIL.Image import Image


class ImageCache:
    def __init__(self, cache_dir="cache", max_cache_num=100, file_extension="png"):
        timestamp = str(time.time_ns())
        self.cache_dir = os.path.join(cache_dir, timestamp)
        print(f"Image cache files will be saved at {self.cache_dir}")
        os.makedirs(self.cache_dir, exist_ok=True)
        self.max_cache_num = max_cache_num
        self.cache_num = 0
        self.file_extension = file_extension
        
    def __call__(self, image):
        self.cache_num += 1
        if self.cache_num > self.max_cache_num:
            for file_name in os.listdir(self.cache_dir):
                shutil.rmtree(os.path.join(self.cache_dir, file_name), ignore_errors=True)
        timestamp = str(time.time_ns())
        if isinstance(image, Image):
            path = os.path.join(self.cache_dir, f"{timestamp}.{self.file_extension}")
            image.save(path)
        elif isinstance(image, str):
            _, file_extension = os.path.splitext(image)
            path = os.path.join(self.cache_dir, f"{timestamp}.{file_extension}")
            shutil.copy(image, path)
        else:
            raise ValueError("Unsupported image format.")
        return path
