# ImagePulse

ImagePulse project aims to provide dataset support for the next generation of image understanding and generation models, by atomizing the capabilities of these models and constructing atomic capability datasets.

[Switch to Chinese](./README_zh.md)

## Atomic Capability Datasets

### 1. Change, Add, Remove

* Dataset: [https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove](https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove)
* Dataset Construction Script: [./scripts/change_add_remove.py](./scripts/change_add_remove.py)

|image_1|image_2|mask|editing_instruction|reverse_editing_instruction|
|-|-|-|-|-|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove/repo?Revision=master&FilePath=examples%2F1744013120311361245.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove/repo?Revision=master&FilePath=examples%2F1744013120913689247.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove/repo?Revision=master&FilePath=examples%2F1744013121479743986.png&View=true)|Remove the mustache and beard, change the white shirt to a blue turtleneck sweater, and remove the glass of milk.|Add a mustache and beard, change the blue turtleneck sweater to a white shirt, and add a glass of milk.|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove/repo?Revision=master&FilePath=examples%2F1744015461339152045.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove/repo?Revision=master&FilePath=examples%2F1744015461913602903.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove/repo?Revision=master&FilePath=examples%2F1744015462528076745.png&View=true)|Add a silver butterfly to the glowing golden lace on her face.|Remove the silver butterfly from the glowing golden lace on her face.|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove/repo?Revision=master&FilePath=examples%2F1744016406622692833.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove/repo?Revision=master&FilePath=examples%2F1744016406879202494.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove/repo?Revision=master&FilePath=examples%2F1744016407103807249.png&View=true)|Remove the necklace.|Add a necklace.|

### 2. Zoom In, Zoom Out

* Dataset: [https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout](https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout)
* Dataset Construction Script: [./scripts/zoomin_zoomout.py](./scripts/zoomin_zoomout.py)

|image_1|image_2|image_cropped|mask|editing_instruction|reverse_editing_instruction|
|-|-|-|-|-|-|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744017806213212210.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744017806661371148.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744017807087521895.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744017807158059796.png&View=true)|Zoom in to focus on the headband.|Zoom out to show the full view of the anime girl.|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744018155020381346.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744018155427860250.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744018155855043024.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744018156047318211.png&View=true)|Remove the superhero costume and replace it with a red shirt. Adjust the lighting to highlight the man's face.|Add a superhero costume with a red and yellow emblem on the chest and a red cape. Adjust the lighting to emphasize the costume.|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744022952566167918.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744022953056227755.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744022953542855348.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout/repo?Revision=master&FilePath=examples%2F1744022953578925049.png&View=true)|Remove the elephant and replace it with a large rock.|Replace the large rock with an elephant.|

### 3. Style Transfer

* Dataset: [https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer](https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer)
* Dataset Construction Script: [./scripts/style_transfer.py](./scripts/style_transfer.py)

|image_1|image_2|image_3|image_4|editing_instruction|reverse_editing_instruction|
|-|-|-|-|-|-|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744027631796853160.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744027632264796657.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744027632584051560.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744027633022068239.png&View=true)|transform the image into a cartoon style with vibrant colors and a confident expression.|transform the image into a realistic portrait with a serious expression and subtle lighting.|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744031879395794851.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744031879898078896.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744031880408740400.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744031880783716279.png&View=true)|transform the image to have a brighter, more colorful palette and a clear blue sky.|transform the image to have a more muted color palette and an overcast sky.|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744050264122532325.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744050264640221066.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744050265127669284.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer/repo?Revision=master&FilePath=examples%2F1744050265613174226.png&View=true)|transform the style of the image to an anime illustration, change the jacket to red, and add a cityscape background.|transform the style of the image to a digital painting, change the jacket to black, and remove the cityscape background.|

### 4. Face ID

* Dataset: [https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-FaceID](https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-FaceID)
* Dataset Construction Script: [./scripts/faceid.py](./scripts/faceid.py)

|image_face|image_1|image_2|editing_instruction|reverse_editing_instruction|
|-|-|-|-|-|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-FaceID/repo?Revision=master&FilePath=examples%2F1744256330927573006.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-FaceID/repo?Revision=master&FilePath=examples%2F1744256330957069063.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-FaceID/repo?Revision=master&FilePath=examples%2F1744256331450025822.png&View=true)|Change the woman's white t-shirt to a white tank top.|Change the woman's white tank top to a white t-shirt.|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-FaceID/repo?Revision=master&FilePath=examples%2F1744259490418252494.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-FaceID/repo?Revision=master&FilePath=examples%2F1744258428429085213.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-FaceID/repo?Revision=master&FilePath=examples%2F1744258428839634350.png&View=true)|Add a nighttime street scene with bokeh lights in the background.|Remove the nighttime street scene and bokeh lights from the background.|
|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-FaceID/repo?Revision=master&FilePath=examples%2F1744259490418252494.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-FaceID/repo?Revision=master&FilePath=examples%2F1744259490442746082.png&View=true)|![](https://www.modelscope.cn/api/v1/datasets/DiffSynth-Studio/ImagePulse-FaceID/repo?Revision=master&FilePath=examples%2F1744259490835883304.png&View=true)|Change the background to a warmly lit room with lamps, change the suit to maroon, and add a sweater under the suit.|Change the background to a dimly lit room with red lighting, change the suit to black, and remove the sweater.|

## Running Dataset Generation

```bash
pip install -r requirements.txt
```

```bash
python change_add_remove.py \
  --target_dir "data/dataset" \
  --cache_dir "data/cache" \
  --dashscope_api_key "sk-xxxxxxxxxxxxxxxx" \
  --qwenvl_model_id "qwen-vl-max" \
  --modelscope_access_token "xxxxxxxxxxxxxxx" \
  --modelscope_dataset_id "DiffSynth-Studio/ImagePulse-ChangeAddRemove" \
  --num_data 1000000 \
  --max_num_files_per_folder 1000
```

* `target_dir`: Path to store the dataset
* `cache_dir`: Cache path
* `dashscope_api_key`: [DashScope](https://DashScope.console.aliyun.com/#/home) API Key, required when calling DashScope API
* `qwenvl_model_id`: ID of the Qwen-VL model on [DashScope](https://DashScope.console.aliyun.com/#/home), required when calling DashScope API
* `modelscope_access_token`: Access token from [ModelScope](https://modelscope.cn/my/myaccesstoken), required when uploading datasets to ModelScope
* `modelscope_dataset_id`: Dataset ID on [ModelScope](https://modelscope.cn), required when uploading datasets to ModelScope
* `num_data`: Total number of data samples
* `max_num_files_per_folder`: Number of files per packaged folder

## Acknowledgements

* [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio): Provided Diffusion model inference support for this project
* [ModelScope](https://modelscope.cn): Provided storage and download support for models and datasets in this project
* [DashScope](https://DashScope.console.aliyun.com/#/home): Provided inference API support for large language models in this project
