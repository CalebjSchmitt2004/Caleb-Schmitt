import tkinter as tk

window = tk.Tk()
label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=100,
    height=100
)
label1 = tk.Label(text="Python rocks!")
label.pack()
label1.pack()

window.mainloop()
