import tkinter as tk
from functools import partial
from Gradient import GradientFrame as GF
import Commands as com
import time

Windows = []
Buttons = []
Labels = []
Images = []
Entrys = []

passbox = ""
loggedIn = False

def click(command):
    com.Command(str(command))


def getEntry():
    string = entry.get()
    return string


def getPass():
    return passbox.get()


def getPassBox():
    global passbox

    PasswordText = ["label", "Password:", "green", "white", "arial", 15, "center", 250, 85]
    PasswordEntry = ["entry", 20, 310, 78, 2]
    entryLen = len(Entrys)
    labelLen = len(Labels)

    Labels.append(PasswordText)
    Entrys.append(PasswordEntry)
    Label = Labels[labelLen]
    label = tk.Label(text=Label[1], fg=Label[2], bg=Label[3], font=(Label[4], Label[5]))
    label.place(anchor=Label[6], x=Label[7], y=Label[8])
    Entry = Entrys[entryLen]
    passbox = tk.Entry(width=Entry[1], borderwidth=Entry[4])
    passbox.place(x=Entry[2], y=Entry[3])


def next():
    Login = ["button", 1, 10, "light grey", "black", "Login", 270, 150, "login", "active"]
    buttonLen = len(Buttons)
    Buttons.append(Login)
    Button = Buttons[buttonLen]
    button = tk.Button(command=partial(click, str(Button[8])), text=Button[5], fg=Button[4], bg=Button[3],
                       width=Button[2], height=Button[1], state=Button[9])
    button.place(x=Button[6], y=Button[7])
    getPassBox()

def loginMessage(result, user):
    global loggedIn
    if result:
        Success = ["label", "Logging in: " + str(user), "green", "white", "arial", 12, "center", 310, 125]
        Labels.append(Success)
        labelLen = len(Labels)
        Label = Labels[labelLen-1]
        label = tk.Label(text=Label[1], fg=Label[2], bg=Label[3], font=(Label[4], Label[5]))
        label.place(anchor=Label[6], x=Label[7], y=Label[8])
        loggedIn = True
    else:
        NotSuccess = ["label", "Login Failed", "red", "white", "arial", 12, "center", 310, 125]
        Labels.append(NotSuccess)
        labelLen = len(Labels)
        Label = Labels[labelLen-1]
        label = tk.Label(text=Label[1], fg=Label[2], bg=Label[3], font=(Label[4], Label[5]))
        label.place(anchor=Label[6], x=Label[7], y=Label[8])


def newBuild(Package):
    global Windows, Buttons, Labels, loggedIn
    Windows = Package[0]
    windowAttributes = Windows

    if loggedIn:
        time.sleep(5)
        exit()

    for packages in Package:
        if packages[0] == "button":
            Buttons.append(packages)
        if packages[0] == "label":
            Labels.append(packages)
        if packages[0] == "image":
            Images.append(packages)
        if packages[0] == "entry":
            Entrys.append(packages)

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
        button = tk.Button(Window, command=partial(click, str(Button[8])), text=Button[5], fg=Button[4], bg=Button[3],
                           width=Button[2], height=Button[1], state=Button[9])
        button.place(x=Button[6], y=Button[7])

    for Label in Labels:
        label = tk.Label(Window, text=Label[1], fg=Label[2], bg=Label[3], font=(Label[4], Label[5]))
        label.place(anchor=Label[6], x=Label[7], y=Label[8])

    for Image in Images:
        icon = tk.PhotoImage(file=Image[1])
        image = tk.Label(Window, image=icon, bg=Image[2], borderwidth=Image[6])
        image.place(anchor=Image[3], x=Image[4], y=Image[5])

    for Entry in Entrys:
        global entry
        entry = tk.Entry(Window, width=Entry[1], borderwidth=Entry[4])
        entry.place(x=Entry[2], y=Entry[3])

    Window.resizable(windowAttributes[3], windowAttributes[3])
    Window.mainloop()


def replyOut():
    return str(Windows) + "\n" + str(Buttons) + "\n" + str(Labels) + "\n" + str(Images)


def newImage(file):
    return tk.PhotoImage(file=str(file))
