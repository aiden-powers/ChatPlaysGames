import win32gui

window_name = "Peggle Deluxe 1.01"
hwnd = win32gui.FindWindow(None, window_name)

def get_dimensions():
    windowLeft, windowTop, windowRight, windowBottom = 0, 0, 0, 0
    if hwnd:
        windowLeft, windowTop, windowRight, windowBottom = win32gui.GetWindowRect(hwnd)
    return windowLeft, windowTop, windowRight, windowBottom

def get_play_area():
    # play area is the area inside the window with custom margins
    windowLeft, windowTop, windowRight, windowBottom = get_dimensions()
    playAreaLeft = windowLeft + 95
    playAreaTop = windowTop + 95
    playAreaRight = windowRight - 95
    playAreaBottom = windowBottom - 30
    return playAreaLeft, playAreaTop, playAreaRight, playAreaBottom

class dimensionsClass:
    def __init__(self):
        self.windowLeft, self.windowTop, self.windowRight, self.windowBottom = get_dimensions()
        self.playAreaLeft, self.playAreaTop, self.playAreaRight, self.playAreaBottom = get_play_area()
        self.width = self.windowRight - self.windowLeft
        self.height = self.windowBottom - self.windowTop
    windowLeft, windowTop, windowRight, windowBottom = get_dimensions()
    playAreaLeft, playAreaTop, playAreaRight, playAreaBottom = get_play_area()