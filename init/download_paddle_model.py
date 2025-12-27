import os
import tarfile
import urllib.request as req
from pathlib import Path

PADDLE_OCR_MODELS = {
        # 文本检测
        "PP-OCRv5_server_det": {
            "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/PP-OCRv5_server_det_infer.tar",
            "dirname": "PP-OCRv5_server_det_infer" 
            },
        # 文本识别
        "PP-OCRv5_server_rec": {
            "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/PP-OCRv5_server_rec_infer.tar", 
            "dirname": "PP-OCRv5_server_rec_infer"
            }, 
        "japan_PP-OCRv3_mobile_rec": {
            "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/japan_PP-OCRv3_mobile_rec_infer.tar", 
            "dirname": "japan_PP-OCRv3_mobile_rec_infer"
            }, 
        "latin_PP-OCRv5_mobile_rec": {
            "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/latin_PP-OCRv5_mobile_rec_infer.tar", 
            "dirname": "latin_PP-OCRv5_mobile_rec_infer"
            }, 
        # 文本图像矫正
        "UVDoc": {
            "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/UVDoc_infer.tar", 
            "dirname": "UVDoc_infer"
            }, 
        # 文档图像方向分类
        "PP-LCNet_x1_0_doc_ori": {
            "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/PP-LCNet_x1_0_doc_ori_infer.tar",
            "dirname": "PP-LCNet_x1_0_doc_ori_infer"
            }, 
        # 文档行方向分类
        "PP-LCNet_x1_0_textline_ori": {
            "url": "https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/PP-LCNet_x1_0_textline_ori_infer.tar", 
            "dirname": "PP-LCNet_x1_0_textline_ori_infer"
            }
        }

def download_file(url: str, dst: Path):
    print(f"downloading: {url}")
    req.urlretrieve(url, dst)

def extract_tar(tar_path: Path, extract_to: Path):
    print(f"extracting: {tar_path.name}")
    with tarfile.open(tar_path) as tar:
        tar.extractall(path=extract_to)

def ensure_model(model_key: str, base_dir="./models/ocr/paddle-ocr"):
    model = PADDLE_OCR_MODELS[model_key]
    base_dir = Path(base_dir)
    base_dir.mkdir(parents=True, exist_ok=True)

    model_dir = base_dir / model["dirname"]
    if model_dir.exists():
        print(f"model exists: {model_dir}")
        return model_dir

    tar_path = base_dir / f"{model['dirname']}.tar"
    if not tar_path.exists():
        download_file(model["url"], tar_path)

    extract_tar(tar_path, base_dir)

    return model_dir

def ensure_all_models():
    for key in PADDLE_OCR_MODELS:
        ensure_model(key)

if __name__ == "__main__":
    ensure_all_models()

