import ctypes
from ctypes import wintypes
import win_constants as wc

# 1. Callback definition
WNDPROC = ctypes.WINFUNCTYPE(wintypes.LRESULT, wintypes.HWND, wintypes.UINT, 
                             wintypes.WPARAM, wintypes.LPARAM)

# 2. The Window Procedure (Brain)
def window_proc(hwnd, msg, wparam, lparam):
    if msg == wc.WM_DESTROY:
        wc.user32.PostQuitMessage(0)
        return 0
    return wc.user32.DefWindowProcW(hwnd, msg, wparam, lparam)

_proc_ref = WNDPROC(window_proc)

def spawn(class_name, window_name):
    instance = wc.kernel32.GetModuleHandleW(None)
    
    # Setup Class
    wnd_class = wc.WNDCLASSEX()
    wnd_class.cbSize = ctypes.sizeof(wc.WNDCLASSEX)
    wnd_class.lpfnWndProc = _proc_ref
    wnd_class.hInstance = instance
    wnd_class.lpszClassName = class_name
    wnd_class.hCursor = wc.user32.LoadCursorW(None, 32512) # IDC_ARROW
    wnd_class.hBrush = wc.gdi32.GetStockObject(0)         # WHITE_BRUSH

    # Register
    if not wc.user32.RegisterClassExW(ctypes.byref(wnd_class)):
        # If it fails, check if the class name is already registered
        pass 
    
    # Create
    hwnd = wc.user32.CreateWindowExW(
        0, class_name, window_name, 0x00CF0000, # WS_OVERLAPPEDWINDOW
        0x80000000, 0x80000000, 400, 300,       # CW_USEDEFAULT
        None, None, instance, None
    )
    
    if not hwnd:
        raise ctypes.WinError()
        
    wc.user32.ShowWindow(hwnd, 5) # SW_SHOW
    return hwnd

def run_loop():
    msg = wintypes.MSG()
    while wc.user32.GetMessageW(ctypes.byref(msg), None, 0, 0) > 0:
        wc.user32.TranslateMessage(ctypes.byref(msg))
        wc.user32.DispatchMessageW(ctypes.byref(msg))

