import time
import win32api


def glide_to(x,y,timeAmount):
    x0,y0 = win32api.GetCursorPos()
    dx = x - x0
    dy = y - y0
    steps = int(timeAmount/0.01)
    for i in range(steps):
        win32api.SetCursorPos((int(x0 + dx * i / steps), int(y0 + dy * i / steps)))
        time.sleep(0.01)
    win32api.SetCursorPos((x,y))

def set_to(x,y):
    win32api.SetCursorPos((x,y))