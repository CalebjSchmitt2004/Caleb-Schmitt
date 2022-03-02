import tkinter as tk

from Gradient import GradientFrame as GF

window_height = 450
window_width = 600
window_title = "Python Installer"
gradient_top = "midnight blue"
gradient_bottom = "purple"
textColor = "white"
textSize = 45
textFont = "arial"

def Install():
    print("Hello")

def Repair():
    print("Hello")

def Delete():
    print("Hello")

# Window Set-up
window = tk.Tk()
window.title(str(window_title))
window.iconbitmap("Icons\\pythonSnake.ico")
window.geometry(str(window_width) + "x" + str(window_height))


# Gradient_Script Set-up
gf = GF.GradientFrame(window, colors=(gradient_top, gradient_bottom), width=window_width, height=window_height)
gf.config(direction=gf.top2bottom)
gf.pack()

# Title Label
pythonInstaller = tk.Label(window, text="Python Installer", bg=gradient_top, fg=textColor, font=(textFont, textSize)).place(anchor="center", x=270, y=50)

# Python Image
PythonImage = tk.PhotoImage(file='Images\pythonSnake.png')
tk.Label(window, image=PythonImage, bg=gradient_top).place(anchor="center", x=530, y=50)

# Buttons
install = tk.Button(command=Install, width=10, height=1, border=0, state="active").place(anchor="center", x=450, y=150)
repair = tk.Button(command=Repair, width=10, height=1, border=0, bg="grey35", state="disabled").place(anchor="center", x=450, y=250)
delete = tk.Button(command=Delete, width=10, height=1, border=0, bg="grey35", state="disabled").place(anchor="center", x=450, y=350)



window.resizable(False, False)
window.mainloop()
