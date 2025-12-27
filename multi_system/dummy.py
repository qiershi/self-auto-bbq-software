from PIL import Image
from multi_system.base import WindowCapture

# Linux 下的假实现
class DummyWindowCapture(WindowCapture):
    '''
    在 Linux 环境下模拟 Windows 截图行为
    '''

    def __init__(self, image_path: str | None = None):
        '''
        : param image_path: 指定一张图片作为"截图"
        '''
        self.image_path = image_path
        self.alive = True

    def is_window_alive(self) -> bool:
        # dummy 永远认为窗口存在
        return self.alive
    
    def close(self):
        # 模拟窗口被关闭
        self.alive = False
    
    def capture(self) -> Image.Image:
        if not self.is_window_alive():
            raise RuntimeError("Dummy window is not alive")

        if self.image_path:
            # 使用固定图片模拟截图
            return Image.open(self.image_path).convert("RGB")

        # 否则生成一张纯色图
        return Image.new("RGB", (1280, 720), color=(128, 128, 128))

