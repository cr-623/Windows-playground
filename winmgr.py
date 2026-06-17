import ctypes
from ctypes import wintypes
import win_constants as wc

# Callback definition remains global to ensure it exists for the lifetime of the app
WNDPROC = ctypes.WINFUNCTYPE(wintypes.LRESULT, wintypes.HWND, wintypes.UINT, 
                             wintypes.WPARAM, wintypes.LPARAM)

class MainWindow:
    def __init__(self, title="Basic window", class_name="WindowClass"):
        self.hwnd = None
        self.class_name = class_name
        self.instance = wc.kernel32.GetModuleHandleW(None)
        self._proc_ref = WNDPROC(self._window_proc)
        
        self._register_class()
        self._create_window(title)

    def _register_class(self):
        wnd_class = wc.WNDCLASSEX()
        wnd_class.cbSize = ctypes.sizeof(wc.WNDCLASSEX)
        wnd_class.lpfnWndProc = self._proc_ref
        wnd_class.hInstance = self.instance
        wnd_class.lpszClassName = self.class_name
        wnd_class.hCursor = wc.user32.LoadCursorW(None, wc.IDC_WAIT)
        wnd_class.hBrush = wc.gdi32.GetStockObject(0)
        wnd_class.hIcon = wc.user32.LoadIconW(None, 32512)
        wnd_class.hIconSm = wc.user32.LoadIconW(None, 32512)

        if not wc.user32.RegisterClassExW(ctypes.byref(wnd_class)):
            # Ignore error if class is already registered
            pass

    def _create_window(self, title):
        self.hwnd = wc.user32.CreateWindowExW(
            0, self.class_name, title, 0x00CF0000,
            0x80000000, 0x80000000, 400, 300,
            None, None, self.instance, None
        )
        if not self.hwnd:
            raise ctypes.WinError()
        wc.user32.ShowWindow(self.hwnd, 5)

    # Custom behavior
    def _window_proc(self, hwnd, msg, wparam, lparam):
        if msg == wc.WM_DESTROY:
            print("Window destroyed, exiting...")
            wc.user32.PostQuitMessage(0)
            return 0
        return wc.user32.DefWindowProcW(hwnd, msg, wparam, lparam)

    def run(self):
        msg = wintypes.MSG()
        while wc.user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
            wc.user32.TranslateMessage(ctypes.byref(msg))
            wc.user32.DispatchMessageW(ctypes.byref(msg))

if __name__ == "__main__":
    import winattr
    app = MainWindow("Basic Window")
    app.run()
