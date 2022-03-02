import tkinter as tk
import subprocess

subprocess.run("cls", shell=True)
cpc = 1
command = ""


def newClick():
    value = int(cookies["text"])
    cookies["text"] = f"{value + cpc}"


def addCPC():
    global cpc
    if int(cookies["text"]) >= 100:
        value1 = int(cookies["text"])
        cookies["text"] = f"{value1 - 100}"
        cpc += 1
        value = int(cpcNum["text"])
        cpcNum["text"] = f"{value + 1}"


def addCPCMAX():
    global cpc
    Cookies = int(cookies["text"])
    Max = int(Cookies / 100)

    if Max >= 1:
        cookies["text"] = f"{Cookies - (100 * Max)}"
        cpc += Max
        value = int(cpcNum["text"])
        cpcNum["text"] = f"{value + Max}"


def cmd():
    global command, cpc
    command = input("Terminal Command: ")
    if command == "cpc":
        value = input("What would you like to increase CPC by?: ")
        num = int(cpcNum["text"])
        cpcNum["text"] = f"{num + int(value)}"
        cpc += int(value)


window = tk.Tk()
background = tk.Frame(master=window, bg="black", height=300, width=300)

cookiesText = tk.Label(text="Cookies:", bg="black", fg="white", width=10)
cookies = tk.Label(text="0", bg="black", fg="white", width=10)
addCookies = tk.Button(text="+PC", master=window, command=newClick, height=0, width=10)

cpcText = tk.Label(text="Cookies Per Click:", bg="black", fg="white", width=15)
cpcNum = tk.Label(text=str(cpc), bg="black", fg="white", width=10)
addCPC = tk.Button(text="+1", master=window, command=addCPC, height=0, width=10)
addCPCMAX = tk.Button(text="Max", master=window, command=addCPCMAX, height=0, width=10)

cmdButton = tk.Button(bg="white", height=0, width=5, command=cmd)

background.pack()
cookiesText.place(x=0, y=0)
cookies.place(x=0, y=20)
addCookies.place(x=0, y=40)
cpcText.place(x=65, y=0)
cpcNum.place(x=80, y=20)
addCPC.place(x=80, y=40)
addCPCMAX.place(x=80, y=60)
cmdButton.place(x=250, y=0)
window.mainloop()
