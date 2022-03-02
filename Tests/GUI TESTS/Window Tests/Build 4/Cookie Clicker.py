import tkinter as tk

window = tk.Tk()
background = tk.Frame(master=window, width=500, height=500, bg="black")
cookie_image = tk.PhotoImage(file="C:\\Users\Caleb\Desktop\GUI Builds\Cookie Clicker\cookie.png")
cookie = tk.Label(master=background, width=10, height=10, bg="grey")


background.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
cookie.place()
window.mainloop()
