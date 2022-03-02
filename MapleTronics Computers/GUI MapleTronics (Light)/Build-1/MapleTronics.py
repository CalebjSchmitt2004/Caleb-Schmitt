from GUI_API import API

window = ["window", 500, 200, False, False, "white", "", "MapleTronics Database", True, "Icons\Maple_icon.ico"]
MapleLogo = ["image", "E:\Tkinter Projects\GUI MapleTronics (Light)\Build-1\Images\\back.png", "midnight blue", "center", 100, 100, 0]
Next = ["button", 1, 10, "light grey", "black", "Next", 270, 150, "next", "active"]
UsernameText = ["label", "Username:", "green", "white", "arial", 15, "center", 250, 55]
UsernameEntry = ["entry", 20, 310, 48, 2]

package = [window, MapleLogo, Next, UsernameText, UsernameEntry]

API.newBuild(package)
