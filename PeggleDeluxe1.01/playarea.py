import win32api

import mousehelper
from dimensionhelper import dimensionsClass

def goto_in_play_area(xPercent,yPercent, glideTime=1):
    dims = dimensionsClass()
    x = dims.playAreaLeft + (dims.playAreaRight - dims.playAreaLeft) * xPercent
    y = dims.playAreaTop + (dims.playAreaBottom - dims.playAreaTop) * yPercent
    x = int(x)
    y = int(y)
    mousehelper.glide_to(x, y, glideTime)

def get_mouse_in_play_area():
    dims = dimensionsClass()
    # get the mouse position in the play area, as a percentage
    x0, y0 = win32api.GetCursorPos()
    x = (x0 - dims.playAreaLeft) / (dims.playAreaRight - dims.playAreaLeft)
    y = (y0 - dims.playAreaTop) / (dims.playAreaBottom - dims.playAreaTop)
    return x, y




'''
TESTING FUNCTIONS
TESTING FUNCTIONS
TESTING FUNCTIONS
TESTING FUNCTIONS
'''

def play_area_glide_across_border_TEST():
    glideTime = .5
    dims = dimensionsClass()
    mousehelper.set_to(dims.playAreaLeft, dims.playAreaTop)
    mousehelper.glide_to(dims.playAreaRight, dims.playAreaBottom, glideTime)
    mousehelper.glide_to(dims.playAreaLeft, dims.playAreaBottom, glideTime)
    mousehelper.glide_to(dims.playAreaRight, dims.playAreaTop, glideTime)

def play_area_grid_test():
    for i in range(11):
        for j in range(11):
            goto_in_play_area(i/10,j/10, .1)

def play_area_grid_test_2():
    for i in range(11):
        goto_in_play_area(i/10, i/10, .1)

def goto_top_left():
    goto_in_play_area(0,0)

def goto_bottom_right():
    goto_in_play_area(1,1)