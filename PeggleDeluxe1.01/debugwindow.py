import win32gui

import playarea
import getdimensions

window_name = "Peggle Deluxe 1.01"
hwnd = win32gui.FindWindow(None, window_name)

def tkinter_status_window():
    dims = getdimensions.dimensionsClass()
    # create a tkinter window that shows the current mouse position in the play area
    import tkinter as tk
    width = dims.width - 6
    height = dims.height - 34
    root = tk.Tk()
    label = tk.Label(root, text="Mouse position in play area")
    label.pack()
    label2 = tk.Label(root, text="")
    label2.pack()
    root.geometry(f"{width}x{height}")
    def update_label():
        x, y = playarea.get_mouse_in_play_area()
        label2.config(text=f"x: {x:.2f}, y: {y:.2f}")
        root.geometry(f"{width}x{height}")
        root.after(100, update_label)
    update_label()
    root.mainloop()

tkinter_status_window()