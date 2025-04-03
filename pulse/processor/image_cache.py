import os, time, shutil
from PIL.Image import Image


class ImageCache:
    def __init__(self, cache_dir="cache", max_cache_num=10, file_extension="png"):
        timestamp = str(time.time_ns())
        self.cache_dir = os.path.join(cache_dir, timestamp)
        print(f"Image cache files will be saved at {self.cache_dir}")
        os.makedirs(self.cache_dir, exist_ok=True)
        self.max_cache_num = max_cache_num
        self.file_extension = file_extension
        self.cached_files = []
        
    def __call__(self, image):
        while len(self.cached_files) > self.max_cache_num:
            file_path = self.cached_files.pop(0)
            os.remove(file_path)
        timestamp = str(time.time_ns())
        if isinstance(image, Image):
            path = os.path.join(self.cache_dir, f"{timestamp}.{self.file_extension}")
            image.save(path)
            self.cached_files.append(path)
        elif isinstance(image, str):
            _, file_extension = os.path.splitext(image)
            path = os.path.join(self.cache_dir, f"{timestamp}.{file_extension}")
            shutil.copy(image, path)
            self.cached_files.append(path)
        else:
            raise ValueError("Unsupported image format.")
        return path
