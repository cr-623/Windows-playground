import ctypes
import time
import win_constants as wc

class Mouse:
    def __init__(self):
        self._update_internal_pos()

    def _update_internal_pos(self):
        pt = wc.POINT()
        wc.user32.GetCursorPos(ctypes.byref(pt))
        self._x = pt.x
        self._y = pt.y

    @property
    def x(self):
        pt = wc.POINT()
        wc.user32.GetCursorPos(ctypes.byref(pt))
        self._x = pt.x
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        wc.user32.SetCursorPos(self._x, self._y)

    @property
    def y(self):
        pt = wc.POINT()
        wc.user32.GetCursorPos(ctypes.byref(pt))
        self._y = pt.y
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        wc.user32.SetCursorPos(self._x, self._y)

    @property
    def left_pressed(self):
        return bool(wc.user32.GetAsyncKeyState(wc.VK_LBUTTON) & 0x8000)

    @property
    def right_pressed(self):
        return bool(wc.user32.GetAsyncKeyState(wc.VK_RBUTTON) & 0x8000)

    @property
    def middle_pressed(self):
        return bool(wc.user32.GetAsyncKeyState(wc.VK_MBUTTON) & 0x8000)

    def _get_event_flags(self, button):
        if button == 0:
            return (wc.MOUSEEVENTF_LEFTDOWN, wc.MOUSEEVENTF_LEFTUP)
        elif button == 1:
            return (wc.MOUSEEVENTF_RIGHTDOWN, wc.MOUSEEVENTF_RIGHTUP)
        elif button == 2:
            return (wc.MOUSEEVENTF_MIDDLEDOWN, wc.MOUSEEVENTF_MIDDLEUP)
        raise ValueError("Button must be 0 (Left), 1 (Right), or 2 (Middle)")

    def click(self, button, duration=0.0):
        down_flag, up_flag = self._get_event_flags(button)
        
        wc.user32.mouse_event(down_flag, 0, 0, 0, 0)
        if duration > 0:
            time.sleep(duration)
        wc.user32.mouse_event(up_flag, 0, 0, 0, 0)

    def scroll(self, amount):
        wc.user32.mouse_event(wc.MOUSEEVENTF_WHEEL, 0, 0, amount * 120, 0)
