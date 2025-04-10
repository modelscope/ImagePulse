# ImagePulse-图律脉动

图律脉动项目旨在为下一代图像理解和生成模型提供数据集支撑，将模型的能力原子化，并构建原子能力数据集。

[切换到英文](./README.md)

## 原子能力数据集

### 1. 修改、添加、移除

* 数据集：https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-ChangeAddRemove
* 数据集构建脚本：[./scripts/change_add_remove.py](./scripts/change_add_remove.py)

|image_1|image_2|mask|editing_instruction|reverse_editing_instruction|
|-|-|-|-|-|
|![](https://github.com/user-attachments/assets/3a657ccd-6fae-4c44-bff8-a3b702c89d65)|![](https://github.com/user-attachments/assets/cc91af21-0090-4392-89d3-ddd62e056da5)|![](https://github.com/user-attachments/assets/5e4c0fdf-15ef-4bf0-b027-ef863e74afaa)|Remove the mustache and beard, change the white shirt to a blue turtleneck sweater, and remove the glass of milk.|Add a mustache and beard, change the blue turtleneck sweater to a white shirt, and add a glass of milk.|
|![](https://github.com/user-attachments/assets/e3ed5116-1d51-47ab-ae51-0fd4e1548bfd)|![](https://github.com/user-attachments/assets/f78eb833-82bd-4a1f-9856-58718b05dc03)|![](https://github.com/user-attachments/assets/8d1e7e9d-6f5e-4abc-905a-c9f3321ec772)|Add a silver butterfly to the glowing golden lace on her face.|Remove the silver butterfly from the glowing golden lace on her face.|
|![](https://github.com/user-attachments/assets/169e1170-f1d2-4f37-a758-baee81343720)|![](https://github.com/user-attachments/assets/6c250bd1-a705-45ba-8c8a-aacb91eaaa0f)|![](https://github.com/user-attachments/assets/167eb187-605b-4dcd-be62-b6833309aa5c)|Remove the necklace.|Add a necklace.|

### 2. 放大、缩小

* 数据集：https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-ZoominZoomout
* 数据集构建脚本：[./scripts/zoomin_zoomout.py](./scripts/zoomin_zoomout.py)

|image_1|image_2|image_cropped|mask|editing_instruction|reverse_editing_instruction|
|-|-|-|-|-|-|
|![](https://github.com/user-attachments/assets/c90e2a05-8bbe-4897-83f6-fad5692677e2)|![](https://github.com/user-attachments/assets/70ab6767-e088-49f1-afb8-b85cca894031)|![](https://github.com/user-attachments/assets/76718ff8-f6ae-4f75-8f3f-be10d2eebde4)|![](https://github.com/user-attachments/assets/4bebe7f6-a3a7-481b-bcef-100bb18bec5d)|Zoom in to focus on the headband.|Zoom out to show the full view of the anime girl.|
|![](https://github.com/user-attachments/assets/99fc81f9-77e5-4181-a376-06cdf5feaf65)|![](https://github.com/user-attachments/assets/e97b398d-a68e-4f34-a5e9-a831d16f3941)|![](https://github.com/user-attachments/assets/aef092d1-8d8c-4353-a9b7-089875307830)|![](https://github.com/user-attachments/assets/dcf2578a-df22-471c-96c0-34ba361a10b5)|Remove the superhero costume and replace it with a red shirt. Adjust the lighting to highlight the man's face.|Add a superhero costume with a red and yellow emblem on the chest and a red cape. Adjust the lighting to emphasize the costume.|
|![](https://github.com/user-attachments/assets/356fc12b-02ca-4f3c-bf65-3248ca5576eb)|![](https://github.com/user-attachments/assets/41dcdf1c-3ce6-49aa-a651-cfc981932689)|![](https://github.com/user-attachments/assets/d5facc03-99d0-4f15-93ce-9f1bc5397bfd)|![](https://github.com/user-attachments/assets/5df06650-8c2b-47f2-9bf4-d3e2510e224d)|Remove the elephant and replace it with a large rock.|Replace the large rock with an elephant.|

### 3. 风格迁移

* 数据集：https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-StyleTransfer
* 数据集构建脚本：[./scripts/style_transfer.py](./scripts/style_transfer.py)

|image_1|image_2|image_3|image_4|editing_instruction|reverse_editing_instruction|
|-|-|-|-|-|-|
|![](https://github.com/user-attachments/assets/f8974a51-fe70-4081-b0c8-60acc0c73f28)|![](https://github.com/user-attachments/assets/81e99ac5-8458-4f4a-ac4e-ae57e809f7f2)|![](https://github.com/user-attachments/assets/c8bb8062-3ad9-44b5-9ee0-a70be4dcbfb3)|![](https://github.com/user-attachments/assets/9edd818e-b6ae-4e6e-924b-cdb21d02a2ec)|transform the image into a cartoon style with vibrant colors and a confident expression.|transform the image into a realistic portrait with a serious expression and subtle lighting.|
|![](https://github.com/user-attachments/assets/82253243-028b-43b4-9a37-796f17fa21af)|![](https://github.com/user-attachments/assets/84bf1c5b-55ae-4084-82ec-3a45c15b2030)|![](https://github.com/user-attachments/assets/b8908d78-ad41-42ce-af4b-c52bf92b2989)|![](https://github.com/user-attachments/assets/6593c9d6-7d5e-4cc0-b2ba-49e5fb38a229)|transform the image to have a brighter, more colorful palette and a clear blue sky.|transform the image to have a more muted color palette and an overcast sky.|
|![](https://github.com/user-attachments/assets/705efc5f-504b-49ac-ba76-ae2f9edb56e4)|![](https://github.com/user-attachments/assets/d0e2e902-d97f-4ffd-91c3-56c96aa19f71)|![](https://github.com/user-attachments/assets/d8c0150f-2e41-480a-9873-dbb8419c8ac5)|![](https://github.com/user-attachments/assets/7be0991c-06e8-4560-8ff8-5fbd2f81b1a0)|transform the style of the image to an anime illustration, change the jacket to red, and add a cityscape background.|transform the style of the image to a digital painting, change the jacket to black, and remove the cityscape background.|

### 4. 人脸保持

* 数据集：https://www.modelscope.cn/datasets/DiffSynth-Studio/ImagePulse-FaceID
* 数据集构建脚本：[./scripts/faceid.py](./scripts/faceid.py)

|image_face|image_1|image_2|editing_instruction|reverse_editing_instruction|
|-|-|-|-|-|
|![](https://github.com/user-attachments/assets/6b61c298-1938-405b-a680-c767bc8913e0)|![](https://github.com/user-attachments/assets/071f2743-3fc8-42d1-b17a-768835c3f9f4)|![](https://github.com/user-attachments/assets/05b45391-df5b-453c-9007-e94674056c5a)|Change the woman's white t-shirt to a white tank top.|Change the woman's white tank top to a white t-shirt.|
|![](https://github.com/user-attachments/assets/203c9f5d-58fe-4e55-8ab8-5adbf14a1fbf)|![](https://github.com/user-attachments/assets/1022a76c-9ac2-43f0-bde2-d65322834251)|![](https://github.com/user-attachments/assets/09511643-8370-46ba-aee8-bcf4efd86d72)|Add a nighttime street scene with bokeh lights in the background.|Remove the nighttime street scene and bokeh lights from the background.|
|![](https://github.com/user-attachments/assets/64d8d216-0966-4108-a378-1ad2312ad8eb)|![](https://github.com/user-attachments/assets/9d182b1e-8b4f-4f74-9f58-d14d7ad15474)|![](https://github.com/user-attachments/assets/c0f9a43e-dd2e-48c9-945c-643f11852808)|Change the background to a warmly lit room with lamps, change the suit to maroon, and add a sweater under the suit.|Change the background to a dimly lit room with red lighting, change the suit to black, and remove the sweater.|

## 运行数据集生成

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

* `target_dir`: 数据集存储路径
* `cache_dir`: 缓存路径
* `dashscope_api_key`: [百炼](https://bailian.console.aliyun.com/#/home) API Key，调用百炼 API 时需填入
* `qwenvl_model_id`: [百炼](https://bailian.console.aliyun.com/#/home) 上 Qwen-VL 模型的 ID，调用百炼 API 时需填入
* `modelscope_access_token`: [魔搭社区](https://modelscope.cn/my/myaccesstoken) 访问令牌，上传数据集到魔搭社区时需填入
* `modelscope_dataset_id`: [魔搭社区](https://modelscope.cn) 数据集 ID，上传数据集到魔搭社区时需填入
* `num_data`: 数据样本总量
* `max_num_files_per_folder`: 每个打包文件中的文件数量

## 致谢

* [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio)：为本项目提供 Diffusion 模型推理支持
* [魔搭社区](https://modelscope.cn)：为本项目提供模型和数据集的存储与下载支持
* [百炼](https://bailian.console.aliyun.com/#/home)：为本项目提供大型语言模型的推理 API 支持
