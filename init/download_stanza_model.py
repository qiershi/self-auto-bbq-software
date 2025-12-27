import os

# 设置模型文件位置
os.environ["STANZA_RESOURCES_DIR"] = "./models/translate/stanza_models"
import stanza

def ensure_stanza_models():
    os.environ['http_proxy'] = 'http://127.0.0.1:7890'
    os.environ['https_proxy'] = 'http://127.0.0.1:7890'

    print("downloading: Stanza 英文模型")
    stanza.download('en', processors='tokenize, mwt')

    print("downloading: Stanza 中文模型")
    stanza.download('zh', processors='tokenize')

    print("downloading: Stanza 日语模型")
    stanza.download("ja", processors="tokenize")

