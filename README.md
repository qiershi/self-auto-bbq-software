# 架构

## 软件架构

Capture     窗口截取
OCR         文字提取
Translate   文本翻译

Translator.translate(OcrEngine.predict(Capture.capture()))

## Capture

基于 abc ( abstract class ) 的抽象基类，面向不同操作系统编写不同的 capture 类

目前在 Linux 上使用模拟 Windows 的 dummy.py

## OCR 

原使用 TesseractOCR ，但不适合本项目面对的情况

现使用 PaddleOCR ，使用 单例模式

## Translate 

原使用 deep-translator ，但需连接 Google ，在国内不稳定

现使用 argos-translate

### argos-translate 初始化

argos 须下载翻译模型

1. argos 翻译模型

``` bash
argospm update 
argospm install translate-zh_en
argospm install translate-en_zh
argospm install translate-ja_en 
```

本地化
``` bash 
ARGOS_PACKAGES_DIR = "./XXX/packages"
```

> AI一开始修改 ARGOS_PACKAGE_DIR 报错
> 后查询源代码，得到 argos 模型包依赖的根目录结构

2. stanza 语言模型

``` python
import os
import stanza

# 如果使用代理
os.environ['http.proxy'] = 'http://127.0.0.1:7890'
os.environ['https.proxy'] = 'http://127.0.0.1:7891'

stanza.download('en', processors='tokenize, mwt')
stanza.download('ja', processors='tokenize')
stanza.download('zh', processors='tokenize')
```

本地化
``` bash 
STANZA_RESOURCES_DIR = "./XXX"
```
