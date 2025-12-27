import os

# 设置模型文件位置
os.environ["STANZA_RESOURCES_DIR"] = "./models/translate/stanza_models"

import stanza

os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['https_proxy'] = 'http://127.0.0.1:7890'

print("正在尝试下载 Stanza 英文模型")
stanza.download('en', processors='tokenize, mwt')

print("正在尝试下载 Stanza 中文模型")
stanza.download('zh', processors='tokenize')

print("正在尝试下载 Stanza 日语模型")
stanza.download("ja", processors="tokenize")
