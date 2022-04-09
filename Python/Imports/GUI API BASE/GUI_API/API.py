import tkinter as tk
from functools import partial
from Gradient import GradientFrame as GF
import Commands as com

Windows = []
Buttons = []
Labels = []
Images = []


def click(command):
    com.Command(str(command))


def newBuild(Package):
    global Windows, Buttons, Labels
    Windows = Package[0]
    windowAttributes = Windows

    for packages in Package:
        if packages[0] == "button":
            Buttons.append(packages)
        if packages[0] == "label":
            Labels.append(packages)
        if packages[0] == "image":
            Images.append(packages)

    Window = tk.Tk()
    if windowAttributes[8]:
        Window.iconbitmap(windowAttributes[9])
    Window.geometry(str(windowAttributes[1]) + "x" + str(windowAttributes[2]))
    Window.title(str(windowAttributes[7]))

    if windowAttributes[4]:
        gf = GF.GradientFrame(Window, colors=(windowAttributes[5], windowAttributes[6]), width=windowAttributes[1],
                              height=windowAttributes[2])
        gf.config(direction=gf.top2bottom)
        gf.pack()
    if not windowAttributes[4]:
        background = tk.Label(Window, bg=windowAttributes[5], height=windowAttributes[1], width=windowAttributes[2])
        background.pack()

    for Button in Buttons:
        button = tk.Button(command=partial(click, str(Button[8])), text=Button[5], fg=Button[4], bg=Button[3],
                           width=Button[2], height=Button[1], state=Button[9])
        button.place(x=Button[6], y=Button[7])

    for Label in Labels:
        label = tk.Label(Window, text=Label[1], fg=Label[2], bg=Label[3], font=(Label[4], Label[5]))
        label.place(anchor=Label[6], x=Label[7], y=Label[8])

    for Image in Images:
        icon = tk.PhotoImage(file=Image[1])
        image = tk.Label(Window, image=icon, bg=Image[2])
        image.place(anchor=Image[3], x=Image[4], y=Image[5])

    Window.resizable(windowAttributes[3], windowAttributes[3])
    Window.mainloop()


def replyOut():
    return str(Windows) + "\n" + str(Buttons) + "\n" + str(Labels) + "\n" + str(Images)


def newImage(file):
    return tk.PhotoImage(file=str(file))
