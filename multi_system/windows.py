from PIL import Image
from multi_system.base import WindowCapture

import win32gui
import win32ui
import win32con


class WindowsWindowCapture(WindowCapture):
    """
    基于 Win32 API 的窗口截图实现
    """

    def __init__(self, hwnd: int):
        """
        :param hwnd: Windows 窗口句柄
        """
        self.hwnd = hwnd

    def is_window_alive(self) -> bool:
        return win32gui.IsWindow(self.hwnd)

    def capture(self) -> Image.Image:
        if not self.is_window_alive():
            raise RuntimeError("Target window does not exist")

        # 获取窗口大小
        left, top, right, bottom = win32gui.GetClientRect(self.hwnd)
        width = right - left
        height = bottom - top

        # 获取设备上下文
        hwnd_dc = win32gui.GetWindowDC(self.hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()

        # 创建位图
        bitmap = win32ui.CreateBitmap()
        bitmap.CreateCompatibleBitmap(mfc_dc, width, height)
        save_dc.SelectObject(bitmap)

        # 截图（PrintWindow 比 BitBlt 更稳定）
        result = win32gui.PrintWindow(
            self.hwnd,
            save_dc.GetSafeHdc(),
            1  # PW_CLIENTONLY
        )

        if result != 1:
            raise RuntimeError("PrintWindow failed")

        # 转为 PIL Image
        bmpinfo = bitmap.GetInfo()
        bmpstr = bitmap.GetBitmapBits(True)

        image = Image.frombuffer(
            "RGB",
            (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
            bmpstr,
            "raw",
            "BGRX",
            0,
            1,
        )

        # 释放资源
        win32gui.DeleteObject(bitmap.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwnd_dc)

        return image

