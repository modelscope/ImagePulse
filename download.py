#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('black-forest-labs/FLUX.1-Fill-dev', cache_dir="./models")