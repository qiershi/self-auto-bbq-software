from abc import ABC, abstractmethod
from PIL import Image

# 定义平台接口
class WindowCapture(ABC):
    @abstractmethod
    def is_window_alive(self) -> bool:
        pass

    @abstractmethod
    def capture(self) -> Image.Image:
        pass


