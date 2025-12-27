import os
from PIL import Image

# [1] 模拟
from multi_system.dummy import DummyWindowCapture
# [2] OCR 提取文字
from core.ocr.ocr_engine import OCREngine
# [3] 翻译
os.environ["STANZA_RESOURCES_DIR"] = "./models/translate/stanza_models"
os.environ["ARGOS_PACKAGES_DIR"] = "./models/translate/argos_translatei/packages"
from argostranslate import translate, package

# 性能监测
import time
import tracemalloc



def test_2_3():
    # [ 开始监测 ]
    start_time = time.perf_counter()
    cpu_start_time = time.process_time()
    tracemalloc.start()

    # 1. 获取截图
    img_path = os.path.expanduser("~/图片/ocr_test/2.jpg")
    img = DummyWindowCapture(img_path).capture()

    # 2. 提取文字
    # en: 英语; zh: 简体中文; japan: 日语; german: 德语
    ocr = OCREngine(lang="japan")
    text = ocr.predict(img)

    string = ""
    for i in range(len(text)):
        string += text[i]

    print(f"直接提取文本: {text}")
    print(f"处理后文本:   {string}")
    
    middle_string = translate.translate(string, "ja", "en")
    translated_string = translate.translate(middle_string, "en", "zh")

    print(f"翻译后文本:   {translated_string}")
    
    # [ 结束监测 ]
    end_time = time.perf_counter()
    used_time = end_time - start_time
    cpu_end_time = time.process_time()
    cpu_used_time = cpu_end_time - cpu_start_time
    current, peak = tracemalloc.get_traced_memory()
    print(f"耗时: \t\t {used_time:.4f} 秒")
    print(f"cpu时间: \t {cpu_used_time:.4f} 秒")
    print(f"当前内存: \t {current / 1024 / 1024:.2f} MB ")
    print(f"峰值内存: \t {peak /1024 /1024:.2f} MB")

    tracemalloc.stop()

    assert translated_string is None
    
