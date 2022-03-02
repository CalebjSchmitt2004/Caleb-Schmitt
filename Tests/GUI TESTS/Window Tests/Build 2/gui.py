import tkinter as tk
window = tk.Tk()

def out():
    print(nameEntry.get())

frame1 = tk.Frame(width=10, height=10)

nameText = tk.Label(text="Please enter your name: ", width=21)
nameEntry = tk.Entry(width=25)
background = tk.Label(master=frame1, fg="white", bg="black", width=250, height=50)

btn_submit = tk.Button(master=window, text="Submit", command=out, height=-1)
btn_submit.place(x=25, y=31)


frame1.pack()
nameText.place(x=0, y=10)
nameEntry.place(x=0, y=31)
background.pack()
window.mainloop()
