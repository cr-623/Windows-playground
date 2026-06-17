# Windows-playground

Ctypes wrapper

### ARE YOU TIRED OF MANUALLY DEFINING WIN32 API CONSTANTS OVER AND OVER?

### DO YOU ABSOLUTELY HATE WIN32 API?

### HAVE YOU EVER TRIED TO GET INTO CTYPES BUT FELT TOO INTIMIDATED BY THE STRUCTURES?

## WELL FEAR NOT, FOR ABSTRACTION IS HERE TO SAVE THE DAY!

# **INTRODUCING THE ALL NEW WINDOWS PLAYGROUND**

## Where you can treat Windows like your playground!

## Move windows around, hide them! Fade them!

## Hell, you can even make a platformer using only windows, in Windows!

With a simple:

```python
import winattr

windows = winattr.get_windows()
for item in windows:
    winattr.hide(item['hwnd'])

```

You can easily modify and apply windows styles to individual windows based on HWNDs! Almost all functions in winattr.py only require the HWND as the argument, making interacting with windows much much simpler. Examples include:
- ghost(hwnd). Makes the window see through and click through
- adjust_window(hwnd, x=None, y=None, width=None, height=None). Resize or move the window
- get_name(hwnd) and set_name(hwnd). Get the title or set the title of the window. However, the window's program will usually change the title back internally after an event
- set_alpha(hwnd, value). Set the transparency of the window
- bring_top(hwnd). Brings a window to the top.
- pin(hwnd). Brings a window to the top, but you can't click away. unpin(hwnd) to unpin it

Helper functions
- get_windows(pretty=False). Returns a list of tuples, (hwnd, name)
- winfov(hwnd). Stands for window info verbose, returns all styles of a window

Improvements should be made, such as:
- Window order management. Get the topmost window, or based on Z order of stacking
- Better window creation management

`win_constants.py` includes massive amounts of constants and structures so you will never have to define them again.

`winattr.py` includes functions to apply WS_STYLES and WS_EX_STYLES to individual windows.

`winmgr.py` and `mouse.py` need more development. Keyboard wrappers are still in development.

Note: Run on a Windows 10 machine. May not work on other versions. 
