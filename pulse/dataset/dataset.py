import os, time, shutil, json, tarfile, torchvision, torch
from PIL import Image
from modelscope.hub.api import HubApi
import torchvision.transforms.functional


class ImageDatasetStorage:
    def __init__(self, target_dir, max_num_files_per_folder=5000, file_extension="png", image_keys=(), metadata_keys=(), modelscope_access_token=None, modelscope_dataset_id=None):
        os.makedirs(target_dir, exist_ok=True)
        self.target_dir = target_dir
        self.max_num_files_per_folder = max_num_files_per_folder
        self.file_extension = file_extension
        self.image_keys = image_keys
        self.metadata_keys = metadata_keys
        self.save_dir = None
        self.modelscope_access_token = modelscope_access_token
        self.modelscope_dataset_id = modelscope_dataset_id
        self.set_new_dir()
        
        
    def push_to_hub(self):
        if self.save_dir is not None and self.modelscope_dataset_id is not None:
            tar_file = self.save_dir + ".tar.gz"
            with tarfile.open(tar_file, "w:gz") as tar:
                tar.add(self.save_dir, arcname=os.path.basename(self.save_dir))
            api = HubApi()
            api.login(self.modelscope_access_token)
            api.upload_file(
                path_or_fileobj=tar_file,
                path_in_repo="data/" + os.path.basename(self.save_dir) + ".tar.gz",
                repo_id=self.modelscope_dataset_id,
                repo_type="dataset",
                commit_message=f"Upload {os.path.basename(self.save_dir)}",
            )
                    
        
    def set_new_dir(self):
        self.push_to_hub()
        timestamp = str(time.time_ns())
        self.save_dir = os.path.join(self.target_dir, timestamp)
        print(f"Dataset will be saved at {self.save_dir}")
        os.makedirs(self.save_dir, exist_ok=True)
        self.num_files = 0
        
        
    def get_image(self, image):
        timestamp = str(time.time_ns())
        if isinstance(image, Image.Image):
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
        
        
        
class ImageDataset:
    def __init__(self, base_path, crop=False, height=1024, width=1024, max_num=10000000):
        self.path = []
        self.search_for_images(base_path)
        self.crop = crop
        self.height = height
        self.width = width
        self.max_num = max_num
    
    def is_image_file(self, file_path):
        if "." not in file_path:
            return False
        file_ext_name = file_path.split(".")[-1]
        if file_ext_name.lower() in ["jpg", "jpeg", "png", "webp"]:
            return True
        return False

    def search_for_images(self, path):
        if os.path.isfile(path):
            if self.is_image_file(path):
                self.path.append(path)
        else:
            for file_name in os.listdir(path):
                sub_path = os.path.join(path, file_name)
                self.search_for_images(sub_path)
                
    def crop_and_resize(self, image):
        width, height = image.size
        scale = max(self.width / width, self.height / height)
        image = torchvision.transforms.functional.resize(
            image,
            (round(height*scale), round(width*scale)),
            interpolation=torchvision.transforms.InterpolationMode.BILINEAR
        )
        image = torchvision.transforms.functional.center_crop(
            image,
            (self.height, self.width),
        )
        return image
    
    def __getitem__(self, idx):
        while True:
            try:
                idx = torch.randint(0, len(self.path), size=(1,)).tolist()[0]
                path = self.path[idx]
                image = Image.open(path)
                if self.crop:
                    image = self.crop_and_resize(image)
                return image
            except:
                continue
    
    def __len__(self):
        return self.max_num
