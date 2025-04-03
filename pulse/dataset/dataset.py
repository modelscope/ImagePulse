import os, time, shutil, json
from PIL.Image import Image


class ImageDatasetStorage:
    def __init__(self, target_dir, max_num_files_per_folder=5000, file_extension="png", image_keys=(), metadata_keys=()):
        os.makedirs(target_dir, exist_ok=True)
        self.target_dir = target_dir
        self.max_num_files_per_folder = max_num_files_per_folder
        self.file_extension = file_extension
        self.image_keys = image_keys
        self.metadata_keys = metadata_keys
        self.set_new_dir()
        
        
    def set_new_dir(self):
        timestamp = str(time.time_ns())
        self.save_dir = os.path.join(self.target_dir, timestamp)
        print(f"Dataset will be saved at {self.save_dir}")
        os.makedirs(self.save_dir, exist_ok=True)
        self.num_files = 0
        
        
    def get_image(self, image):
        timestamp = str(time.time_ns())
        if isinstance(image, Image):
            path = os.path.join(self.save_dir, f"{timestamp}.{self.file_extension}")
            image.save(path)
        elif isinstance(image, str):
            _, file_extension = os.path.splitext(image)
            path = os.path.join(self.save_dir, f"{timestamp}.{file_extension}")
            shutil.copy(image, path)
        else:
            raise ValueError("Unsupported image format.")
        self.num_files += 1
        return path
        
        
    def get_images(self, images):
        if not isinstance(images, list):
            images = [images]
        path = [self.get_image(image) for image in images]
        return path
    
    
    def get_metadata(self, metadata):
        timestamp = str(time.time_ns())
        path = os.path.join(self.save_dir, f"{timestamp}.json")
        with open(path, "w") as f:
            json.dump(metadata, f, ensure_ascii=False)
        self.num_files += 1
        return path
    
    
    def __call__(self, **kwargs):
        metadata = {key: kwargs[key] for key in self.metadata_keys}
        for key in self.image_keys:
            path = self.get_image(kwargs[key])
            metadata[key] = os.path.basename(path)
        path = self.get_metadata(metadata)
        path = os.path.basename(path)
        if self.num_files > self.max_num_files_per_folder:
            self.set_new_dir()
        return path
        