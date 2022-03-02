import tkinter as tk

from Gradient import GradientFrame as GF

window_height = 450
window_width = 600
window_title = "Night Gradient_Script Test"
gradient_top = "midnight blue"
gradient_bottom = "purple"
textColor = "white"
textSize = 50
textFont = "arial"

# Window Set-up
window = tk.Tk()
window.title(str(window_title))
window.iconbitmap("Icons\\under_c.ico")
window.geometry(str(window_width) + "x" + str(window_height))

# Gradient_Script Set-up
gf = GF.GradientFrame(window, colors=(gradient_top, gradient_bottom), width=window_width, height=window_height)
gf.config(direction=gf.top2bottom)
gf.pack()

# Under-Construction Label
uc = tk.Label(window, text="Under Construction", bg=gradient_top, fg=textColor, font=(textFont, textSize)).place(x=5, y=10)


window.resizable(False, False)
window.mainloop()
