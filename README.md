# Windows-playground
Ctypes wrapper

## ARE YOU TIRED OF MANUALLY DEFINING WIN32 API CONSTANTS OVER AND OVER?
## DO YOU ABSOLUTELY HATE WIN32 API?
## HAVE YOU EVER TRIED TO GET INTO CTYPES BUT FELT TOO INTIMIDATED BY THE STRUCTURES?

## WELL FEAR NOT, FOR ABSTRACTION IS HERE TO SAVE THE DAY!
# **INTRODUCING THE ALL NEW WINDOWS PLAYGROUND**
## Where you can treat Windows like your playground!
## Move windows around, hide them! Fade them! 
## Hell, you can even make a platformer using only windows, in Windows!
With a simple 
`import winattr
windows = winattr.get_windows()
for item in windows:
    winattr.hide(item['hwnd']`
You can easily modify and apply windows styles to individual windows based on HWNDs!
```win_constants.py``` includes massive amounts of constants and structures so you will never have to define them again.
```winattr.py``` includes functions to apply WS_STYLES and WS_EX_STYLES to individual windows.
```winmgr.py``` and ```mouse.py``` need more development. Keyboard wrappers are still in development.
