import cv2
import numpy as np
import paddle
from PIL import Image
from paddleocr import PaddleOCR

PADDLE_OCR_MODELS_DIR = "./models/ocr/paddle-ocr/"

class OCREngine:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # 单例模式
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, lang="japan", device="cpu"):
        if hasattr(self, "_initialized"):
            return 
        
        if paddle.is_compiled_with_cuda() and paddle.device.cuda.device_count() > 0:
            device="gpu"

        self.ocr = PaddleOCR(
                lang=lang,                      # 语言模型
                device=device,                  # 设备指定
                use_textline_orientation=True,  # 是否文本行方向分类模型
                text_detection_model_dir=PADDLE_OCR_MODELS_DIR + "PP-OCRv5_server_det_infer",
                text_recognition_model_dir=PADDLE_OCR_MODELS_DIR + "PP-OCRv5_server_rec_infer"
                )
        self._initialized = True

    def _prepare_image(self, img):
        # image_path: String
        if isinstance(img, str):
            return img

        # image: PIL.Image
        if isinstance(img, Image.Image):
            img = np.array(img)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            return img

        # image: numpy.ndarray
        if isinstance(img, np.ndarray):
            return img

        raise TypeError(f"Unsupported image type: {type(img)}")

    def predict(self, img):
        img = self._prepare_image(img)
        result = self.ocr.predict(img)
        return result[0]['rec_texts']

