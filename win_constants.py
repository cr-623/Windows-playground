"""
Complete Win32 API Constants for Python ctypes
Comprehensive collection of Windows API constants for GUI manipulation,
keyboard/mouse input, window management, and system interaction.
"""

import ctypes
from ctypes import wintypes

# ==============================================================================
# MESSAGE BOX CONFIGURATION (MB_)
# ==============================================================================
# Button combinations
MB_OK                = 0x00000000
MB_OKCANCEL          = 0x00000001
MB_ABORTRETRYIGNORE  = 0x00000002
MB_YESNOCANCEL       = 0x00000003
MB_YESNO             = 0x00000004
MB_RETRYCANCEL       = 0x00000005
MB_CANCELTRYCONTINUE = 0x00000006

# Icons
MB_ICONHAND          = 0x00000010  # Stop sign / Error
MB_ICONQUESTION      = 0x00000020
MB_ICONEXCLAMATION   = 0x00000030  # Warning
MB_ICONASTERISK      = 0x00000040  # Information
MB_ICONERROR         = MB_ICONHAND
MB_ICONSTOP          = MB_ICONHAND
MB_ICONWARNING       = MB_ICONEXCLAMATION
MB_ICONINFORMATION   = MB_ICONASTERISK

# Default button selection
MB_DEFBUTTON1        = 0x00000000
MB_DEFBUTTON2        = 0x00000100
MB_DEFBUTTON3        = 0x00000200
MB_DEFBUTTON4        = 0x00000300

# Modality
MB_APPLMODAL         = 0x00000000
MB_SYSTEMMODAL       = 0x00001000
MB_TASKMODAL         = 0x00002000

# Behavior flags
MB_HELP              = 0x00004000
MB_TOPMOST           = 0x00040000
MB_SETFOREGROUND     = 0x00010000
MB_DEFAULT_DESKTOP_ONLY = 0x00020000
MB_RIGHT             = 0x00080000
MB_RTLREADING        = 0x00100000
MB_SERVICE_NOTIFICATION = 0x00200000

# Message Box Return Values
IDOK         = 1
IDCANCEL     = 2
IDABORT      = 3
IDRETRY      = 4
IDIGNORE     = 5
IDYES        = 6
IDNO         = 7
IDCLOSE      = 8
IDHELP       = 9
IDTRYAGAIN   = 10
IDCONTINUE   = 11

# ==============================================================================
# WINDOW STYLES (WS_)
# ==============================================================================
WS_OVERLAPPED       = 0x00000000
WS_POPUP            = 0x80000000
WS_CHILD            = 0x40000000
WS_MINIMIZE         = 0x20000000
WS_VISIBLE          = 0x10000000
WS_DISABLED         = 0x08000000
WS_CLIPSIBLINGS     = 0x04000000
WS_CLIPCHILDREN     = 0x02000000
WS_MAXIMIZE         = 0x01000000
WS_CAPTION          = 0x00C00000
WS_BORDER           = 0x00800000
WS_DLGFRAME         = 0x00400000
WS_VSCROLL          = 0x00200000
WS_HSCROLL          = 0x00100000
WS_SYSMENU          = 0x00080000
WS_THICKFRAME       = 0x00040000
WS_GROUP            = 0x00020000
WS_TABSTOP          = 0x00010000
WS_MINIMIZEBOX      = 0x00020000
WS_MAXIMIZEBOX      = 0x00010000

# Composite styles
WS_OVERLAPPEDWINDOW = (WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | 
                       WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX)
WS_POPUPWINDOW      = (WS_POPUP | WS_BORDER | WS_SYSMENU)
WS_CHILDWINDOW      = WS_CHILD
WS_TILED            = WS_OVERLAPPED
WS_ICONIC           = WS_MINIMIZE
WS_SIZEBOX          = WS_THICKFRAME
WS_TILEDWINDOW      = WS_OVERLAPPEDWINDOW

# ==============================================================================
# EXTENDED WINDOW STYLES (WS_EX_)
# ==============================================================================
WS_EX_DLGMODALFRAME    = 0x00000001
WS_EX_NOPARENTNOTIFY   = 0x00000004
WS_EX_TOPMOST          = 0x00000008
WS_EX_ACCEPTFILES      = 0x00000010
WS_EX_TRANSPARENT      = 0x00000020
WS_EX_MDICHILD         = 0x00000040
WS_EX_TOOLWINDOW       = 0x00000080
WS_EX_WINDOWEDGE       = 0x00000100
WS_EX_CLIENTEDGE       = 0x00000200
WS_EX_CONTEXTHELP      = 0x00000400
WS_EX_RIGHT            = 0x00001000
WS_EX_LEFT             = 0x00000000
WS_EX_RTLREADING       = 0x00002000
WS_EX_LTRREADING       = 0x00000000
WS_EX_LEFTSCROLLBAR    = 0x00004000
WS_EX_RIGHTSCROLLBAR   = 0x00000000
WS_EX_CONTROLPARENT    = 0x00010000
WS_EX_STATICEDGE       = 0x00020000
WS_EX_APPWINDOW        = 0x00040000
WS_EX_LAYERED          = 0x00080000
WS_EX_NOINHERITLAYOUT  = 0x00100000
WS_EX_NOREDIRECTIONBITMAP = 0x00200000
WS_EX_LAYOUTRTL        = 0x00400000
WS_EX_COMPOSITED       = 0x02000000
WS_EX_NOACTIVATE       = 0x08000000

WS_EX_OVERLAPPEDWINDOW = (WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE)
WS_EX_PALETTEWINDOW    = (WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST)

# ==============================================================================
# WINDOW LONG OFFSETS (GWL_)
# ==============================================================================
GWL_WNDPROC    = -4
GWL_HINSTANCE  = -6
GWL_HWNDPARENT = -8
GWL_STYLE      = -16
GWL_EXSTYLE    = -20
GWL_USERDATA   = -21
GWL_ID         = -12

# For 64-bit compatibility
GWLP_WNDPROC    = -4
GWLP_HINSTANCE  = -6
GWLP_HWNDPARENT = -8
GWLP_USERDATA   = -21
GWLP_ID         = -12

# ==============================================================================
# SHOW WINDOW COMMANDS (SW_)
# ==============================================================================
SW_HIDE            = 0
SW_SHOWNORMAL      = 1
SW_NORMAL          = 1
SW_SHOWMINIMIZED   = 2
SW_SHOWMAXIMIZED   = 3
SW_MAXIMIZE        = 3
SW_SHOWNOACTIVATE  = 4
SW_SHOW            = 5
SW_MINIMIZE        = 6
SW_SHOWMINNOACTIVE = 7
SW_SHOWNA          = 8
SW_RESTORE         = 9
SW_SHOWDEFAULT     = 10
SW_FORCEMINIMIZE   = 11
SW_MAX             = 11

# ==============================================================================
# SETWINDOWPOS FLAGS (SWP_)
# ==============================================================================
SWP_NOSIZE         = 0x0001
SWP_NOMOVE         = 0x0002
SWP_NOZORDER       = 0x0004
SWP_NOREDRAW       = 0x0008
SWP_NOACTIVATE     = 0x0010
SWP_FRAMECHANGED   = 0x0020
SWP_SHOWWINDOW     = 0x0040
SWP_HIDEWINDOW     = 0x0080
SWP_NOCOPYBITS     = 0x0100
SWP_NOOWNERZORDER  = 0x0200
SWP_NOSENDCHANGING = 0x0400
SWP_DRAWFRAME      = SWP_FRAMECHANGED
SWP_NOREPOSITION   = SWP_NOOWNERZORDER
SWP_DEFERERASE     = 0x2000
SWP_ASYNCWINDOWPOS = 0x4000

# HWND values for SetWindowPos
HWND_TOP       = 0
HWND_BOTTOM    = 1
HWND_TOPMOST   = -1
HWND_NOTOPMOST = -2

# ==============================================================================
# LAYERED WINDOW ATTRIBUTES (LWA_)
# ==============================================================================
LWA_COLORKEY = 0x00000001
LWA_ALPHA    = 0x00000002

# ==============================================================================
# SYSTEM ICONS (IDI_)
# ==============================================================================
IDI_APPLICATION = 32512
IDI_HAND        = 32513
IDI_QUESTION    = 32514
IDI_EXCLAMATION = 32515
IDI_ASTERISK    = 32516
IDI_WINLOGO     = 32517
IDI_SHIELD      = 32518
IDI_WARNING     = IDI_EXCLAMATION
IDI_ERROR       = IDI_HAND
IDI_INFORMATION = IDI_ASTERISK

# ==============================================================================
# SYSTEM CURSORS (IDC_)
# ==============================================================================
IDC_ARROW       = 32512
IDC_IBEAM       = 32513
IDC_WAIT        = 32514
IDC_CROSS       = 32515
IDC_UPARROW     = 32516
IDC_SIZE        = 32640
IDC_ICON        = 32641
IDC_SIZENWSE    = 32642
IDC_SIZENESW    = 32643
IDC_SIZEWE      = 32644
IDC_SIZENS      = 32645
IDC_SIZEALL     = 32646
IDC_NO          = 32648
IDC_HAND        = 32649
IDC_APPSTARTING = 32650
IDC_HELP        = 32651

# ==============================================================================
# VIRTUAL KEY CODES (VK_)
# ==============================================================================
# Mouse buttons
VK_LBUTTON    = 0x01
VK_RBUTTON    = 0x02
VK_CANCEL     = 0x03
VK_MBUTTON    = 0x04
VK_XBUTTON1   = 0x05
VK_XBUTTON2   = 0x06

# Control keys
VK_BACK       = 0x08
VK_TAB        = 0x09
VK_CLEAR      = 0x0C
VK_RETURN     = 0x0D
VK_SHIFT      = 0x10
VK_CONTROL    = 0x11
VK_MENU       = 0x12  # Alt key
VK_PAUSE      = 0x13
VK_CAPITAL    = 0x14  # Caps Lock
VK_ESCAPE     = 0x1B
VK_SPACE      = 0x20

# Navigation keys
VK_PRIOR      = 0x21  # Page Up
VK_NEXT       = 0x22  # Page Down
VK_END        = 0x23
VK_HOME       = 0x24
VK_LEFT       = 0x25
VK_UP         = 0x26
VK_RIGHT      = 0x27
VK_DOWN       = 0x28

# Other special keys
VK_SELECT     = 0x29
VK_PRINT      = 0x2A
VK_EXECUTE    = 0x2B
VK_SNAPSHOT   = 0x2C  # Print Screen
VK_INSERT     = 0x2D
VK_DELETE     = 0x2E
VK_HELP       = 0x2F

# Number keys (0-9)
VK_0 = 0x30
VK_1 = 0x31
VK_2 = 0x32
VK_3 = 0x33
VK_4 = 0x34
VK_5 = 0x35
VK_6 = 0x36
VK_7 = 0x37
VK_8 = 0x38
VK_9 = 0x39

# Letter keys (A-Z)
VK_A = 0x41
VK_B = 0x42
VK_C = 0x43
VK_D = 0x44
VK_E = 0x45
VK_F = 0x46
VK_G = 0x47
VK_H = 0x48
VK_I = 0x49
VK_J = 0x4A
VK_K = 0x4B
VK_L = 0x4C
VK_M = 0x4D
VK_N = 0x4E
VK_O = 0x4F
VK_P = 0x50
VK_Q = 0x51
VK_R = 0x52
VK_S = 0x53
VK_T = 0x54
VK_U = 0x55
VK_V = 0x56
VK_W = 0x57
VK_X = 0x58
VK_Y = 0x59
VK_Z = 0x5A

# Windows keys
VK_LWIN       = 0x5B
VK_RWIN       = 0x5C
VK_APPS       = 0x5D  # Context menu key
VK_SLEEP      = 0x5F

# Numpad keys
VK_NUMPAD0    = 0x60
VK_NUMPAD1    = 0x61
VK_NUMPAD2    = 0x62
VK_NUMPAD3    = 0x63
VK_NUMPAD4    = 0x64
VK_NUMPAD5    = 0x65
VK_NUMPAD6    = 0x66
VK_NUMPAD7    = 0x67
VK_NUMPAD8    = 0x68
VK_NUMPAD9    = 0x69
VK_MULTIPLY   = 0x6A
VK_ADD        = 0x6B
VK_SEPARATOR  = 0x6C
VK_SUBTRACT   = 0x6D
VK_DECIMAL    = 0x6E
VK_DIVIDE     = 0x6F

# Function keys (F1-F24)
VK_F1  = 0x70
VK_F2  = 0x71
VK_F3  = 0x72
VK_F4  = 0x73
VK_F5  = 0x74
VK_F6  = 0x75
VK_F7  = 0x76
VK_F8  = 0x77
VK_F9  = 0x78
VK_F10 = 0x79
VK_F11 = 0x7A
VK_F12 = 0x7B
VK_F13 = 0x7C
VK_F14 = 0x7D
VK_F15 = 0x7E
VK_F16 = 0x7F
VK_F17 = 0x80
VK_F18 = 0x81
VK_F19 = 0x82
VK_F20 = 0x83
VK_F21 = 0x84
VK_F22 = 0x85
VK_F23 = 0x86
VK_F24 = 0x87

# Lock keys
VK_NUMLOCK    = 0x90
VK_SCROLL     = 0x91

# Shift variants
VK_LSHIFT     = 0xA0
VK_RSHIFT     = 0xA1
VK_LCONTROL   = 0xA2
VK_RCONTROL   = 0xA3
VK_LMENU      = 0xA4  # Left Alt
VK_RMENU      = 0xA5  # Right Alt

# Browser keys
VK_BROWSER_BACK      = 0xA6
VK_BROWSER_FORWARD   = 0xA7
VK_BROWSER_REFRESH   = 0xA8
VK_BROWSER_STOP      = 0xA9
VK_BROWSER_SEARCH    = 0xAA
VK_BROWSER_FAVORITES = 0xAB
VK_BROWSER_HOME      = 0xAC

# Volume keys
VK_VOLUME_MUTE   = 0xAD
VK_VOLUME_DOWN   = 0xAE
VK_VOLUME_UP     = 0xAF

# Media keys
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_MEDIA_STOP       = 0xB2
VK_MEDIA_PLAY_PAUSE = 0xB3

# Launch keys
VK_LAUNCH_MAIL         = 0xB4
VK_LAUNCH_MEDIA_SELECT = 0xB5
VK_LAUNCH_APP1         = 0xB6
VK_LAUNCH_APP2         = 0xB7

# OEM keys (keyboard-specific)
VK_OEM_1      = 0xBA  # ;: on US keyboard
VK_OEM_PLUS   = 0xBB  # =+
VK_OEM_COMMA  = 0xBC  # ,<
VK_OEM_MINUS  = 0xBD  # -_
VK_OEM_PERIOD = 0xBE  # .>
VK_OEM_2      = 0xBF  # /? on US keyboard
VK_OEM_3      = 0xC0  # `~ on US keyboard
VK_OEM_4      = 0xDB  # [{ on US keyboard
VK_OEM_5      = 0xDC  # \| on US keyboard
VK_OEM_6      = 0xDD  # ]} on US keyboard
VK_OEM_7      = 0xDE  # '" on US keyboard
VK_OEM_8      = 0xDF

# Additional keys
VK_PROCESSKEY = 0xE5
VK_PACKET     = 0xE7
VK_ATTN       = 0xF6
VK_CRSEL      = 0xF7
VK_EXSEL      = 0xF8
VK_EREOF      = 0xF9
VK_PLAY       = 0xFA
VK_ZOOM       = 0xFB
VK_NONAME     = 0xFC
VK_PA1        = 0xFD
VK_OEM_CLEAR  = 0xFE

# ==============================================================================
# HOTKEY MODIFIERS (MOD_)
# ==============================================================================
MOD_ALT      = 0x0001
MOD_CONTROL  = 0x0002
MOD_SHIFT    = 0x0004
MOD_WIN      = 0x0008
MOD_NOREPEAT = 0x4000

# ==============================================================================
# WINDOW MESSAGES (WM_)
# ==============================================================================
# General window messages
WM_NULL        = 0x0000
WM_CREATE      = 0x0001
WM_DESTROY     = 0x0002
WM_MOVE        = 0x0003
WM_SIZE        = 0x0005
WM_ACTIVATE    = 0x0006
WM_SETFOCUS    = 0x0007
WM_KILLFOCUS   = 0x0008
WM_ENABLE      = 0x000A
WM_SETREDRAW   = 0x000B
WM_SETTEXT     = 0x000C
WM_GETTEXT     = 0x000D
WM_GETTEXTLENGTH = 0x000E
WM_PAINT       = 0x000F
WM_CLOSE       = 0x0010
WM_QUERYENDSESSION = 0x0011
WM_QUIT        = 0x0012
WM_QUERYOPEN   = 0x0013
WM_ERASEBKGND  = 0x0014
WM_SYSCOLORCHANGE = 0x0015
WM_ENDSESSION  = 0x0016
WM_SHOWWINDOW  = 0x0018
WM_WININICHANGE = 0x001A
WM_SETTINGCHANGE = WM_WININICHANGE
WM_DEVMODECHANGE = 0x001B
WM_ACTIVATEAPP = 0x001C
WM_FONTCHANGE  = 0x001D
WM_TIMECHANGE  = 0x001E
WM_CANCELMODE  = 0x001F
WM_SETCURSOR   = 0x0020
WM_MOUSEACTIVATE = 0x0021
WM_CHILDACTIVATE = 0x0022
WM_QUEUESYNC   = 0x0023
WM_GETMINMAXINFO = 0x0024

# Window state messages
WM_WINDOWPOSCHANGING = 0x0046
WM_WINDOWPOSCHANGED  = 0x0047
WM_POWER       = 0x0048
WM_COPYDATA    = 0x004A
WM_CANCELJOURNAL = 0x004B
WM_NOTIFY      = 0x004E
WM_INPUTLANGCHANGEREQUEST = 0x0050
WM_INPUTLANGCHANGE = 0x0051
WM_TCARD       = 0x0052
WM_HELP        = 0x0053
WM_USERCHANGED = 0x0054
WM_NOTIFYFORMAT = 0x0055
WM_CONTEXTMENU = 0x007B
WM_STYLECHANGING = 0x007C
WM_STYLECHANGED  = 0x007D
WM_DISPLAYCHANGE = 0x007E
WM_GETICON     = 0x007F
WM_SETICON     = 0x0080

# Non-client messages
WM_NCCREATE    = 0x0081
WM_NCDESTROY   = 0x0082
WM_NCCALCSIZE  = 0x0083
WM_NCHITTEST   = 0x0084
WM_NCPAINT     = 0x0085
WM_NCACTIVATE  = 0x0086
WM_GETDLGCODE  = 0x0087
WM_SYNCPAINT   = 0x0088
WM_NCMOUSEMOVE = 0x00A0
WM_NCLBUTTONDOWN = 0x00A1
WM_NCLBUTTONUP = 0x00A2
WM_NCLBUTTONDBLCLK = 0x00A3
WM_NCRBUTTONDOWN = 0x00A4
WM_NCRBUTTONUP = 0x00A5
WM_NCRBUTTONDBLCLK = 0x00A6
WM_NCMBUTTONDOWN = 0x00A7
WM_NCMBUTTONUP = 0x00A8
WM_NCMBUTTONDBLCLK = 0x00A9

# Keyboard messages
WM_KEYDOWN     = 0x0100
WM_KEYUP       = 0x0101
WM_CHAR        = 0x0102
WM_DEADCHAR    = 0x0103
WM_SYSKEYDOWN  = 0x0104
WM_SYSKEYUP    = 0x0105
WM_SYSCHAR     = 0x0106
WM_SYSDEADCHAR = 0x0107
WM_KEYLAST     = 0x0108
WM_UNICHAR     = 0x0109
WM_IME_STARTCOMPOSITION = 0x010D
WM_IME_ENDCOMPOSITION = 0x010E
WM_IME_COMPOSITION = 0x010F
WM_IME_KEYLAST = 0x010F

# Dialog messages
WM_INITDIALOG  = 0x0110
WM_COMMAND     = 0x0111
WM_SYSCOMMAND  = 0x0112
WM_TIMER       = 0x0113
WM_HSCROLL     = 0x0114
WM_VSCROLL     = 0x0115

# Menu messages
WM_INITMENU    = 0x0116
WM_INITMENUPOPUP = 0x0117
WM_MENUSELECT  = 0x011F
WM_MENUCHAR    = 0x0120
WM_ENTERIDLE   = 0x0121
WM_MENURBUTTONUP = 0x0122
WM_MENUDRAG    = 0x0123
WM_MENUGETOBJECT = 0x0124
WM_UNINITMENUPOPUP = 0x0125
WM_MENUCOMMAND = 0x0126

# Control color messages
WM_CTLCOLORMSGBOX = 0x0132
WM_CTLCOLOREDIT   = 0x0133
WM_CTLCOLORLISTBOX = 0x0134
WM_CTLCOLORBTN    = 0x0135
WM_CTLCOLORDLG    = 0x0136
WM_CTLCOLORSCROLLBAR = 0x0137
WM_CTLCOLORSTATIC = 0x0138

# Mouse messages
WM_MOUSEMOVE   = 0x0200
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP   = 0x0202
WM_LBUTTONDBLCLK = 0x0203
WM_RBUTTONDOWN = 0x0204
WM_RBUTTONUP   = 0x0205
WM_RBUTTONDBLCLK = 0x0206
WM_MBUTTONDOWN = 0x0207
WM_MBUTTONUP   = 0x0208
WM_MBUTTONDBLCLK = 0x0209
WM_MOUSEWHEEL  = 0x020A
WM_XBUTTONDOWN = 0x020B
WM_XBUTTONUP   = 0x020C
WM_XBUTTONDBLCLK = 0x020D
WM_MOUSEHWHEEL = 0x020E

# User messages (custom range)
WM_USER        = 0x0400
WM_APP         = 0x8000

# Hotkey message
WM_HOTKEY      = 0x0312

# ==============================================================================
# MOUSE KEY FLAGS (MK_)
# ==============================================================================
MK_LBUTTON  = 0x0001
MK_RBUTTON  = 0x0002
MK_SHIFT    = 0x0004
MK_CONTROL  = 0x0008
MK_MBUTTON  = 0x0010
MK_XBUTTON1 = 0x0020
MK_XBUTTON2 = 0x0040

# ==============================================================================
# SYSTEM COMMANDS (SC_)
# ==============================================================================
SC_SIZE         = 0xF000
SC_MOVE         = 0xF010
SC_MINIMIZE     = 0xF020
SC_MAXIMIZE     = 0xF030
SC_NEXTWINDOW   = 0xF040
SC_PREVWINDOW   = 0xF050
SC_CLOSE        = 0xF060
SC_VSCROLL      = 0xF070
SC_HSCROLL      = 0xF080
SC_MOUSEMENU    = 0xF090
SC_KEYMENU      = 0xF100
SC_ARRANGE      = 0xF110
SC_RESTORE      = 0xF120
SC_TASKLIST     = 0xF130
SC_SCREENSAVE   = 0xF140
SC_HOTKEY       = 0xF150
SC_DEFAULT      = 0xF160
SC_MONITORPOWER = 0xF170
SC_CONTEXTHELP  = 0xF180
SC_SEPARATOR    = 0xF00F

# ==============================================================================
# COLOR CONSTANTS
# ==============================================================================
COLOR_SCROLLBAR           = 0
COLOR_BACKGROUND          = 1
COLOR_ACTIVECAPTION       = 2
COLOR_INACTIVECAPTION     = 3
COLOR_MENU                = 4
COLOR_WINDOW              = 5
COLOR_WINDOWFRAME         = 6
COLOR_MENUTEXT            = 7
COLOR_WINDOWTEXT          = 8
COLOR_CAPTIONTEXT         = 9
COLOR_ACTIVEBORDER        = 10
COLOR_INACTIVEBORDER      = 11
COLOR_APPWORKSPACE        = 12
COLOR_HIGHLIGHT           = 13
COLOR_HIGHLIGHTTEXT       = 14
COLOR_BTNFACE             = 15
COLOR_BTNSHADOW           = 16
COLOR_GRAYTEXT            = 17
COLOR_BTNTEXT             = 18
COLOR_INACTIVECAPTIONTEXT = 19
COLOR_BTNHIGHLIGHT        = 20
COLOR_3DDKSHADOW          = 21
COLOR_3DLIGHT             = 22
COLOR_INFOTEXT            = 23
COLOR_INFOBK              = 24
COLOR_DESKTOP             = COLOR_BACKGROUND
COLOR_3DFACE              = COLOR_BTNFACE
COLOR_3DSHADOW            = COLOR_BTNSHADOW
COLOR_3DHIGHLIGHT         = COLOR_BTNHIGHLIGHT
COLOR_3DHILIGHT           = COLOR_BTNHIGHLIGHT
COLOR_BTNHILIGHT          = COLOR_BTNHIGHLIGHT

# ==============================================================================
# KEYBD_EVENT FLAGS
# ==============================================================================
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

# ==============================================================================
# MOUSE_EVENT FLAGS
# ==============================================================================
MOUSEEVENTF_MOVE        = 0x0001
MOUSEEVENTF_LEFTDOWN    = 0x0002
MOUSEEVENTF_LEFTUP      = 0x0004
MOUSEEVENTF_RIGHTDOWN   = 0x0008
MOUSEEVENTF_RIGHTUP     = 0x0010
MOUSEEVENTF_MIDDLEDOWN  = 0x0020
MOUSEEVENTF_MIDDLEUP    = 0x0040
MOUSEEVENTF_XDOWN       = 0x0080
MOUSEEVENTF_XUP         = 0x0100
MOUSEEVENTF_WHEEL       = 0x0800
MOUSEEVENTF_HWHEEL      = 0x1000
MOUSEEVENTF_MOVE_NOCOALESCE = 0x2000
MOUSEEVENTF_VIRTUALDESK = 0x4000
MOUSEEVENTF_ABSOLUTE    = 0x8000

# ==============================================================================
# GET WINDOW FLAGS (GW_)
# ==============================================================================
GW_HWNDFIRST    = 0
GW_HWNDLAST     = 1
GW_HWNDNEXT     = 2
GW_HWNDPREV     = 3
GW_OWNER        = 4
GW_CHILD        = 5
GW_ENABLEDPOPUP = 6

# ==============================================================================
# REDRAW WINDOW FLAGS (RDW_)
# ==============================================================================
RDW_INVALIDATE      = 0x0001
RDW_INTERNALPAINT   = 0x0002
RDW_ERASE           = 0x0004
RDW_VALIDATE        = 0x0008
RDW_NOINTERNALPAINT = 0x0010
RDW_NOERASE         = 0x0020
RDW_NOCHILDREN      = 0x0040
RDW_ALLCHILDREN     = 0x0080
RDW_UPDATENOW       = 0x0100
RDW_ERASENOW        = 0x0200
RDW_FRAME           = 0x0400
RDW_NOFRAME         = 0x0800

# ==============================================================================
# PEEK MESSAGE FLAGS (PM_)
# ==============================================================================
PM_NOREMOVE = 0x0000
PM_REMOVE   = 0x0001
PM_NOYIELD  = 0x0002

# ==============================================================================
# GET ANCESTOR FLAGS (GA_)
# ==============================================================================
GA_PARENT    = 1
GA_ROOT      = 2
GA_ROOTOWNER = 3

# ==============================================================================
# WINDOW POSITION FLAGS (WINDOWPOS)
# ==============================================================================
SWP_ASYNCWINDOWPOS = 0x4000
SWP_DEFERERASE     = 0x2000

# ==============================================================================
# MONITOR DEFAULTS
# ==============================================================================
MONITOR_DEFAULTTONULL    = 0x00000000
MONITOR_DEFAULTTOPRIMARY = 0x00000001
MONITOR_DEFAULTTONEAREST = 0x00000002

# ==============================================================================
# DPI AWARENESS
# ==============================================================================
DPI_AWARENESS_INVALID           = -1
DPI_AWARENESS_UNAWARE           = 0
DPI_AWARENESS_SYSTEM_AWARE      = 1
DPI_AWARENESS_PER_MONITOR_AWARE = 2

# ==============================================================================
# SYSTEM METRICS (SM_)
# ==============================================================================
SM_CXSCREEN             = 0   # Width of screen
SM_CYSCREEN             = 1   # Height of screen
SM_CXVSCROLL            = 2
SM_CYHSCROLL            = 3
SM_CYCAPTION            = 4
SM_CXBORDER             = 5
SM_CYBORDER             = 6
SM_CXDLGFRAME           = 7
SM_CYDLGFRAME           = 8
SM_CYVTHUMB             = 9
SM_CXHTHUMB             = 10
SM_CXICON               = 11
SM_CYICON               = 12
SM_CXCURSOR             = 13
SM_CYCURSOR             = 14
SM_CYMENU               = 15
SM_CXFULLSCREEN         = 16
SM_CYFULLSCREEN         = 17
SM_CYKANJIWINDOW        = 18
SM_MOUSEPRESENT         = 19
SM_CYVSCROLL            = 20
SM_CXHSCROLL            = 21
SM_DEBUG                = 22
SM_SWAPBUTTON           = 23
SM_RESERVED1            = 24
SM_RESERVED2            = 25
SM_RESERVED3            = 26
SM_RESERVED4            = 27
SM_CXMIN                = 28
SM_CYMIN                = 29
SM_CXSIZE               = 30
SM_CYSIZE               = 31
SM_CXFRAME              = 32
SM_CYFRAME              = 33
SM_CXMINTRACK           = 34
SM_CYMINTRACK           = 35
SM_CXDOUBLECLK          = 36
SM_CYDOUBLECLK          = 37
SM_CXICONSPACING        = 38
SM_CYICONSPACING        = 39
SM_MENUDROPALIGNMENT    = 40
SM_PENWINDOWS           = 41
SM_DBCSENABLED          = 42
SM_CMOUSEBUTTONS        = 43
SM_CXFIXEDFRAME         = SM_CXDLGFRAME
SM_CYFIXEDFRAME         = SM_CYDLGFRAME
SM_CXSIZEFRAME          = SM_CXFRAME
SM_CYSIZEFRAME          = SM_CYFRAME
SM_SECURE               = 44
SM_CXEDGE               = 45
SM_CYEDGE               = 46
SM_CXMINSPACING         = 47
SM_CYMINSPACING         = 48
SM_CXSMICON             = 49
SM_CYSMICON             = 50
SM_CYSMCAPTION          = 51
SM_CXSMSIZE             = 52
SM_CYSMSIZE             = 53
SM_CXMENUSIZE           = 54
SM_CYMENUSIZE           = 55
SM_ARRANGE              = 56
SM_CXMINIMIZED          = 57
SM_CYMINIMIZED          = 58
SM_CXMAXTRACK           = 59
SM_CYMAXTRACK           = 60
SM_CXMAXIMIZED          = 61
SM_CYMAXIMIZED          = 62
SM_NETWORK              = 63
SM_CLEANBOOT            = 67
SM_CXDRAG               = 68
SM_CYDRAG               = 69
SM_SHOWSOUNDS           = 70
SM_CXMENUCHECK          = 71
SM_CYMENUCHECK          = 72
SM_SLOWMACHINE          = 73
SM_MIDEASTENABLED       = 74
SM_MOUSEWHEELPRESENT    = 75
SM_XVIRTUALSCREEN       = 76
SM_YVIRTUALSCREEN       = 77
SM_CXVIRTUALSCREEN      = 78
SM_CYVIRTUALSCREEN      = 79
SM_CMONITORS            = 80
SM_SAMEDISPLAYFORMAT    = 81

# ==============================================================================
# WINDOW ACTIVATION (WA_)
# ==============================================================================
WA_INACTIVE    = 0
WA_ACTIVE      = 1
WA_CLICKACTIVE = 2

# ==============================================================================
# SIZE MESSAGE PARAMETERS (SIZE_)
# ==============================================================================
SIZE_RESTORED  = 0
SIZE_MINIMIZED = 1
SIZE_MAXIMIZED = 2
SIZE_MAXSHOW   = 3
SIZE_MAXHIDE   = 4

# ==============================================================================
# HIT TEST RESULTS (HT_)
# ==============================================================================
HTERROR       = -2
HTTRANSPARENT = -1
HTNOWHERE     = 0
HTCLIENT      = 1
HTCAPTION     = 2
HTSYSMENU     = 3
HTGROWBOX     = 4
HTSIZE        = HTGROWBOX
HTMENU        = 5
HTHSCROLL     = 6
HTVSCROLL     = 7
HTMINBUTTON   = 8
HTMAXBUTTON   = 9
HTLEFT        = 10
HTRIGHT       = 11
HTTOP         = 12
HTTOPLEFT     = 13
HTTOPRIGHT    = 14
HTBOTTOM      = 15
HTBOTTOMLEFT  = 16
HTBOTTOMRIGHT = 17
HTBORDER      = 18
HTREDUCE      = HTMINBUTTON
HTZOOM        = HTMAXBUTTON
HTSIZEFIRST   = HTLEFT
HTSIZELAST    = HTBOTTOMRIGHT
HTOBJECT      = 19
HTCLOSE       = 20
HTHELP        = 21

# ==============================================================================
# CLIPBOARD FORMATS (CF_)
# ==============================================================================
CF_TEXT         = 1
CF_BITMAP       = 2
CF_METAFILEPICT = 3
CF_SYLK         = 4
CF_DIF          = 5
CF_TIFF         = 6
CF_OEMTEXT      = 7
CF_DIB          = 8
CF_PALETTE      = 9
CF_PENDATA      = 10
CF_RIFF         = 11
CF_WAVE         = 12
CF_UNICODETEXT  = 13
CF_ENHMETAFILE  = 14
CF_HDROP        = 15
CF_LOCALE       = 16
CF_DIBV5        = 17
CF_MAX          = 18

# ==============================================================================
# PROCESS DPI AWARENESS
# ==============================================================================
PROCESS_DPI_UNAWARE           = 0
PROCESS_SYSTEM_DPI_AWARE      = 1
PROCESS_PER_MONITOR_DPI_AWARE = 2

# ==============================================================================
# INPUT TYPE (INPUT structure)
# ==============================================================================
INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

# ==============================================================================
# WINDOW FLASHING (FW_)
# ==============================================================================

FLASHW_STOP       = 0x00000000
FLASHW_CAPTION    = 0x00000001
FLASHW_TRAY       = 0x00000002
FLASHW_ALL        = (FLASHW_CAPTION | FLASHW_TRAY)
FLASHW_TIMER      = 0x00000004
FLASHW_TIMERNOFG  = 0x00000008

# ==============================================================================
# WINDOW CLASS STYLES (CS_)
# ==============================================================================
CS_VREDRAW          = 0x0001
CS_HREDRAW          = 0x0002
CS_DBLCLKS          = 0x0008
CS_OWNDC            = 0x0020
CS_CLASSDC          = 0x0040
CS_PARENTDC         = 0x0080
CS_NOCLOSE          = 0x0200
CS_SAVEBITS         = 0x0800
CS_BYTEALIGNCLIENT  = 0x1000
CS_BYTEALIGNWINDOW  = 0x2000
CS_GLOBALCLASS      = 0x4000
CS_IME              = 0x00010000

# ==============================================================================
# CREATE WINDOW CONSTANTS (CW_)
# ==============================================================================
CW_USEDEFAULT       = 0x80000000

# ==============================================================================
# WINDOW STYLES (WS_) - Often used alongside window creation
# ==============================================================================
WS_OVERLAPPED       = 0x00000000
WS_POPUP            = 0x80000000
WS_CHILD            = 0x40000000
WS_MINIMIZE         = 0x20000000
WS_VISIBLE          = 0x10000000
WS_DISABLED         = 0x08000000
WS_CLIPSIBLINGS     = 0x04000000
WS_CLIPCHILDREN     = 0x02000000
WS_MAXIMIZE         = 0x01000000
WS_CAPTION          = 0x00C00000
WS_BORDER           = 0x00800000
WS_DLGFRAME         = 0x00400000
WS_VSCROLL          = 0x00200000
WS_HSCROLL          = 0x00100000
WS_SYSMENU          = 0x00080000
WS_THICKFRAME       = 0x00040000
WS_GROUP            = 0x00020000
WS_TABSTOP          = 0x00010000
WS_MINIMIZEBOX      = 0x00020000
WS_MAXIMIZEBOX      = 0x00010000
WS_OVERLAPPEDWINDOW = (WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX)

if not hasattr(wintypes, 'LRESULT'):
    wintypes.LRESULT = wintypes.LPARAM
if not hasattr(wintypes, 'HICON'):
    wintypes.HICON = wintypes.HANDLE
if not hasattr(wintypes, 'HBRUSH'):
    wintypes.HBRUSH = wintypes.HANDLE
if not hasattr(wintypes, 'HCURSOR'):
    wintypes.HCURSOR = wintypes.HANDLE

# ==============================================================================
# COMMON STRUCTURES
# ==============================================================================
class RECT(ctypes.Structure):
    """Rectangle structure"""
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long)
    ]

class POINT(ctypes.Structure):
    """Point structure"""
    _fields_ = [
        ("x", ctypes.c_long),
        ("y", ctypes.c_long)
    ]

class MSG(ctypes.Structure):
    """Message structure"""
    _fields_ = [
        ("hwnd", wintypes.HWND),
        ("message", wintypes.UINT),
        ("wParam", wintypes.WPARAM),
        ("lParam", wintypes.LPARAM),
        ("time", wintypes.DWORD),
        ("pt", POINT)
    ]

class WINDOWPLACEMENT(ctypes.Structure):
    """Window placement structure"""
    _fields_ = [
        ("length", wintypes.UINT),
        ("flags", wintypes.UINT),
        ("showCmd", wintypes.UINT),
        ("ptMinPosition", POINT),
        ("ptMaxPosition", POINT),
        ("rcNormalPosition", RECT)
    ]
    
class WNDCLASSEX(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.UINT),
        ("style", wintypes.UINT),
        ("lpfnWndProc", ctypes.WINFUNCTYPE(wintypes.LRESULT, wintypes.HWND, 
                                          wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)),
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", wintypes.HINSTANCE),
        ("hIcon", wintypes.HICON),
        ("hCursor", wintypes.HCURSOR),
        ("hBrush", wintypes.HBRUSH),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
        ("hIconSm", wintypes.HICON),
    ]
class MINMAXINFO(ctypes.Structure):
    """Min/max size info"""
    _fields_ = [
        ("ptReserved", POINT),
        ("ptMaxSize", POINT),
        ("ptMaxPosition", POINT),
        ("ptMinTrackSize", POINT),
        ("ptMaxTrackSize", POINT)
    ]

class KEYBDINPUT(ctypes.Structure):
    """Keyboard input structure"""
    _fields_ = [
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(wintypes.ULONG))
    ]

class MOUSEINPUT(ctypes.Structure):
    """Mouse input structure"""
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(wintypes.ULONG))
    ]

class HARDWAREINPUT(ctypes.Structure):
    """Hardware input structure"""
    _fields_ = [
        ("uMsg", wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD)
    ]

class _INPUTunion(ctypes.Union):
    """Union for INPUT structure"""
    _fields_ = [
        ("mi", MOUSEINPUT),
        ("ki", KEYBDINPUT),
        ("hi", HARDWAREINPUT)
    ]

class INPUT(ctypes.Structure):
    """Generic input structure"""
    _fields_ = [
        ("type", wintypes.DWORD),
        ("union", _INPUTunion)
    ]

class BLENDFUNCTION(ctypes.Structure):
    _fields_ = [
        ("BlendOp", ctypes.c_byte),
        ("BlendFlags", ctypes.c_byte),
        ("SourceConstantAlpha", ctypes.c_byte),
        ("AlphaFormat", ctypes.c_byte)
    ]

class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ("biSize", wintypes.DWORD),
        ("biWidth", wintypes.LONG),
        ("biHeight", wintypes.LONG),
        ("biPlanes", wintypes.WORD),
        ("biBitCount", wintypes.WORD),
        ("biCompression", wintypes.DWORD),
        ("biSizeImage", wintypes.DWORD),
        ("biXPelsPerMeter", wintypes.LONG),
        ("biYPelsPerMeter", wintypes.LONG),
        ("biClrUsed", wintypes.DWORD),
        ("biClrImportant", wintypes.DWORD)
    ]

class BITMAPINFO(ctypes.Structure):
    _fields_ = [
        ("bmiHeader", BITMAPINFOHEADER),
        ("bmiColors", wintypes.DWORD * 3)
    ]

class FLASHWINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.UINT),
        ("hwnd", wintypes.HWND),
        ("dwFlags", wintypes.DWORD),
        ("uCount", wintypes.UINT),
        ("dwTimeout", wintypes.DWORD)
    ]

# ==============================================================================
# COMMON USER32 FUNCTIONS (Pre-configured with correct types)
# ==============================================================================
user32=ctypes.windll.user32
dwmapi=ctypes.windll.dwmapi
kernel32=ctypes.windll.kernel32
gdi32 = ctypes.windll.gdi32

gdi32.GetStockObject.argtypes = [ctypes.c_int]
gdi32.GetStockObject.restype = wintypes.HGDIOBJ

# Message box
user32.MessageBoxW.argtypes = [wintypes.HWND, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.UINT]
user32.MessageBoxW.restype = ctypes.c_int

# Window functions
user32.FindWindowW.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]
user32.FindWindowW.restype = wintypes.HWND

user32.GetWindowLongW.argtypes = [wintypes.HWND, ctypes.c_int]
user32.GetWindowLongW.restype = wintypes.LONG

user32.SetWindowLongW.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.LONG]
user32.SetWindowLongW.restype = wintypes.LONG

user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, ctypes.c_int, ctypes.c_int, 
                                ctypes.c_int, ctypes.c_int, wintypes.UINT]
user32.SetWindowPos.restype = wintypes.BOOL

user32.ShowWindow.argtypes = [wintypes.HWND, ctypes.c_int]
user32.ShowWindow.restype = wintypes.BOOL

user32.SetLayeredWindowAttributes.argtypes = [wintypes.HWND, wintypes.COLORREF, 
                                              wintypes.BYTE, wintypes.DWORD]
user32.SetLayeredWindowAttributes.restype = wintypes.BOOL

user32.GetForegroundWindow.argtypes = []
user32.GetForegroundWindow.restype = wintypes.HWND

user32.SetForegroundWindow.argtypes = [wintypes.HWND]
user32.SetForegroundWindow.restype = wintypes.BOOL

user32.GetWindowRect.argtypes = [wintypes.HWND, ctypes.POINTER(RECT)]
user32.GetWindowRect.restype = wintypes.BOOL

user32.MoveWindow.argtypes = [wintypes.HWND, ctypes.c_int, ctypes.c_int, 
                               ctypes.c_int, ctypes.c_int, wintypes.BOOL]
user32.MoveWindow.restype = wintypes.BOOL

# Add these to win_constants.py
user32.EnumWindows.argtypes = [ctypes.c_void_p, wintypes.LPARAM]
user32.EnumWindows.restype = wintypes.BOOL

user32.GetWindowTextLengthW.argtypes = [wintypes.HWND]
user32.GetWindowTextLengthW.restype = ctypes.c_int

user32.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
user32.GetWindowTextW.restype = ctypes.c_int

user32.IsWindowVisible.argtypes = [wintypes.HWND]
user32.IsWindowVisible.restype = wintypes.BOOL

# Input functions
user32.SendInput.argtypes = [wintypes.UINT, ctypes.POINTER(INPUT), ctypes.c_int]
user32.SendInput.restype = wintypes.UINT

user32.keybd_event.argtypes = [wintypes.BYTE, wintypes.BYTE, wintypes.DWORD, wintypes.ULONG]
user32.keybd_event.restype = None

user32.mouse_event.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.DWORD, 
                                wintypes.DWORD, wintypes.ULONG]
user32.mouse_event.restype = None

# Hotkey functions
user32.RegisterHotKey.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.UINT, wintypes.UINT]
user32.RegisterHotKey.restype = wintypes.BOOL

user32.UnregisterHotKey.argtypes = [wintypes.HWND, ctypes.c_int]
user32.UnregisterHotKey.restype = wintypes.BOOL

# System metrics
user32.GetSystemMetrics.argtypes = [ctypes.c_int]
user32.GetSystemMetrics.restype = ctypes.c_int

# Window flashing
user32.FlashWindowEx.argtypes = [ctypes.POINTER(FLASHWINFO)]
user32.FlashWindowEx.restype = wintypes.BOOL

# Window creation
user32.RegisterClassExW.argtypes = [ctypes.POINTER(WNDCLASSEX)]
user32.RegisterClassExW.restype = wintypes.ATOM

user32.CreateWindowExW.argtypes = [
    wintypes.DWORD, wintypes.LPCWSTR, wintypes.LPCWSTR, wintypes.DWORD,
    ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
    wintypes.HWND, wintypes.HMENU, wintypes.HINSTANCE, wintypes.LPVOID
]
user32.CreateWindowExW.restype = wintypes.HWND

user32.DefWindowProcW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
user32.DefWindowProcW.restype = wintypes.LRESULT

user32.PostQuitMessage.argtypes = [ctypes.c_int]
user32.PostQuitMessage.restype = None
