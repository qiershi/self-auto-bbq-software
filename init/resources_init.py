from pathlib import Path
from init.download_paddle_model import ensure_paddle_models
from init.download_stanza_model import ensure_stanza_models
from init.download_argos_model import ensure_argos_models

FLAG_FILE = Path("./temp/inited.flag")

def init():
    if FLAG_FILE.exists():
        return

    print("资源初始化下载...")

    ensure_paddle_models()
    ensure_stanza_models()
    ensure_argos_models()
    
    FLAG_FILE.touch()

