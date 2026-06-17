import ctypes
from ctypes import wintypes
import win_constants as wc
import time
import threading

def winattr(hwnd, action, *args, **kwargs):
    hwnd = wintypes.HWND(int(hwnd))
    action = action.lower().strip()

    if action == "flash":
        flags = args[0] if len(args) > 0 else (wc.FLASHW_TRAY | wc.FLASHW_TIMER)
        count = args[1] if len(args) > 1 else 0
        timeout = args[2] if len(args) > 2 else 0

        info = wc.FLASHWINFO()
        info.cbSize = ctypes.sizeof(wc.FLASHWINFO)
        info.hwnd = hwnd
        info.dwFlags = flags
        info.uCount = count
        info.dwTimeout = timeout
        
        flash_func = getattr(wc, 'FlashWindowEx', wc.user32.FlashWindowEx)
        return bool(flash_func(ctypes.byref(info)))


    elif action == "style":
        flags = args[0]
        is_extended = kwargs.get('is_extended', False)
        index = wc.GWL_EXSTYLE if is_extended else wc.GWL_STYLE
        
        current_style = wc.user32.GetWindowLongW(hwnd, index)
        
        mode = kwargs.get('mode', 'apply')
        if mode == 'add':
            new_style = current_style | flags
        elif mode == 'remove':
            new_style = current_style & ~flags
        else:
            new_style = flags

        result = wc.user32.SetWindowLongW(hwnd, index, new_style)
        wc.user32.SetWindowPos(hwnd, None, 0, 0, 0, 0, 0x0020 | 0x0004 | 0x0002 | 0x0001) 
        return result

    elif action == "show":
        cmd = args[0] if len(args) > 0 else wc.SW_SHOW
        return bool(wc.user32.ShowWindow(hwnd, cmd))

    elif action == "position":
        if len(args) < 4:
            raise ValueError("Position requires: x, y, width, height")
        x, y, w, h = args[0], args[1], args[2], args[3]
        repaint = kwargs.get('repaint', True)
        return bool(wc.user32.MoveWindow(hwnd, x, y, w, h, repaint))

    else:
        raise ValueError(f"Unknown window manipulation action: '{action}'")

def set_alpha(hwnd, alpha):
    ex_style = wc.user32.GetWindowLongW(hwnd, wc.GWL_EXSTYLE)
    if not (ex_style & wc.WS_EX_LAYERED):
        wc.user32.SetWindowLongW(hwnd, wc.GWL_EXSTYLE, ex_style | wc.WS_EX_LAYERED)
    wc.user32.SetLayeredWindowAttributes(hwnd, 0, alpha, wc.LWA_ALPHA)

def ghost(hwnd, alpha=200):
    wc.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0002 | 0x0001)
    winattr(hwnd, "style", wc.WS_EX_LAYERED | wc.WS_EX_TRANSPARENT, is_extended=True, mode="add")
    wc.user32.SetLayeredWindowAttributes(hwnd, 0, alpha, wc.LWA_ALPHA)

def solid(hwnd):
    winattr(hwnd, "style", wc.WS_EX_LAYERED | wc.WS_EX_TRANSPARENT, is_extended=True, mode="remove")
    wc.user32.SetLayeredWindowAttributes(hwnd, 0, 255, wc.LWA_ALPHA)
    wc.user32.SetWindowPos(hwnd, -2, 0, 0, 0, 0, 0x0002 | 0x0001)

def hide_border(hwnd):
    style = wc.WS_CAPTION | wc.WS_THICKFRAME | wc.WS_MINIMIZEBOX | wc.WS_MAXIMIZEBOX
    winattr(hwnd, "style", style, mode="remove")
    wc.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0, 0x0020 | 0x0002 | 0x0001 | 0x0004 | 0x0010)

def show_border(hwnd):
    styles = wc.WS_CAPTION | wc.WS_THICKFRAME | wc.WS_MINIMIZEBOX | wc.WS_MAXIMIZEBOX
    winattr(hwnd, "style", styles, mode="add")
    wc.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0, 0x0020 | 0x0002 | 0x0001 | 0x0004 | 0x0010)

def hide(hwnd):
    winattr(hwnd, "style", wc.WS_EX_TOOLWINDOW, is_extended=True, mode="add")
    winattr(hwnd, "style", wc.WS_EX_APPWINDOW, is_extended=True, mode="remove")
    wc.user32.ShowWindow(hwnd, wc.SW_HIDE)

def show(hwnd):
    winattr(hwnd, "style", wc.WS_EX_TOOLWINDOW, is_extended=True, mode="remove")
    winattr(hwnd, "style", wc.WS_EX_APPWINDOW, is_extended=True, mode="add")
    wc.user32.ShowWindow(hwnd, wc.SW_SHOW)
    
def flash(hwnd, count=5, timeout=500):
    finfo = wc.FLASHWINFO(ctypes.sizeof(wc.FLASHWINFO), hwnd, wc.FLASHW_ALL, count, timeout)
    wc.user32.FlashWindowEx(ctypes.byref(finfo))

def permanent_flash(hwnd, timeout=500):
    finfo = wc.FLASHWINFO(ctypes.sizeof(wc.FLASHWINFO), hwnd, wc.FLASHW_ALL | wc.FLASHW_TIMER, 0, timeout)
    wc.user32.FlashWindowEx(ctypes.byref(finfo))

def stop_flash(hwnd):
    finfo = wc.FLASHWINFO(ctypes.sizeof(wc.FLASHWINFO), hwnd, wc.FLASHW_STOP, 0, 0)
    wc.user32.FlashWindowEx(ctypes.byref(finfo))

def bring_top(hwnd):
    wc.user32.SetForegroundWindow(hwnd)

def pin(hwnd):
    wc.user32.SetWindowPos(hwnd, wc.HWND_TOPMOST, 0, 0, 0, 0, wc.SWP_NOMOVE | wc.SWP_NOSIZE | wc.SWP_NOACTIVATE)

def unpin(hwnd):
    wc.user32.SetWindowPos(hwnd, wc.HWND_NOTOPMOST, 0, 0, 0, 0, wc.SWP_NOMOVE | wc.SWP_NOSIZE | wc.SWP_NOACTIVATE)

def adjust_window(hwnd, x=None, y=None, width=None, height=None):
    rect = wc.RECT()
    wc.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    
    new_x = x if x is not None else rect.left
    new_y = y if y is not None else rect.top
    new_w = width if width is not None else (rect.right - rect.left)
    new_h = height if height is not None else (rect.bottom - rect.top)
    wc.user32.MoveWindow(hwnd, new_x, new_y, new_w, new_h, True)

def winfov(hwnd):
    style = wc.user32.GetWindowLongW(hwnd, wc.GWL_STYLE)
    ex_style = wc.user32.GetWindowLongW(hwnd, wc.GWL_EXSTYLE)
    
    found_styles = []
    found_ex_styles = []

    for name, value in vars(wc).items():
        if name.startswith("WS_") and not name.startswith("WS_EX_"):
            if (style & value) == value:
                found_styles.append(name)
        
        elif name.startswith("WS_EX_"):
            if (ex_style & value) == value:
                found_ex_styles.append(name)

    print(f"--- Styles for {hex(hwnd)} ---")
    print("Standard WS_ Styles:")
    print("  " + "\n  ".join(found_styles))
    print("\nExtended WS_EX_ Styles:")
    print("  " + "\n  ".join(found_ex_styles))

def get_rect(hwnd):
    rect = wc.RECT()
    result = wc.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    
    if result:
        return rect
    else:
        raise ctypes.WinError(ctypes.get_last_error())

def get_name(hwnd):
    length = wc.user32.GetWindowTextLengthW(hwnd)
    if length == 0:
        return ""
    
    buffer = ctypes.create_unicode_buffer(length + 1)
    
    wc.user32.GetWindowTextW(hwnd, buffer, length + 1)
    return buffer.value

def set_name(hwnd, title):
    if not isinstance(title, str):
        title = str(title)
    
    return bool(wc.user32.SetWindowTextW(hwnd, title))

def get_windows(pretty=False):
    windows = []
    EnumWindowsProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    def callback(hwnd, lparam):
        if wc.user32.IsWindowVisible(hwnd):
            title = get_name(hwnd)
            if title:
                windows.append((hwnd, title))
        return True

    wc.user32.EnumWindows(EnumWindowsProc(callback), 0)
    if pretty:
        print(f"{'HWND':<12} | {'TITLE'}")
        print("-" * 40)
        for hwnd, title in windows:
            print(f"{hex(hwnd):<12} | {title}")
            
    return windows
