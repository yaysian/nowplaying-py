import win32gui
import re
from time import sleep

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'YouTube' in win32gui.GetWindowText(hwnd):
            global check 
            check = win32gui.GetWindowText(hwnd)
            check = check[:-26]

current_title = u''
check = u''  
          
#INITIALIZATION          
win32gui.EnumWindows(enumHandler, None)
current_title = check
with open("nowplaying.txt", "wb") as f:
    f.write(check.encode('utf-8'))
f.close()
sleep(5)

#LOOP
while True:
    win32gui.EnumWindows(enumHandler, None)
    if check != current_title:
        current_title = check
        with open("nowplaying.txt", "wb") as f:
            f.write(check.encode('utf-8'))
        f.close()
        sleep(5)
