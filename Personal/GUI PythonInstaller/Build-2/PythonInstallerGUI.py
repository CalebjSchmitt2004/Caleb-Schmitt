from GUI_API import GUI_Installer_API as g

window = ["window", 600, 450, False, True, "midnight blue", "purple", "Python Installer", True,
          "E:\GUI_Builds\GUI_Install_Base\Icons\\pythonSnake.ico"]
button1 = ["button", 1, 10, "light grey", "black", "Install", 450, 150, "pythonInstall", "active"]
button2 = ["button", 1, 10, "light grey", "black", "Repair", 450, 250, "pythonRepair", "active"]
button3 = ["button", 1, 10, "light grey", "black", "Delete", 450, 350, "pythonUninstall", "active"]
text = ["label", "Python Installer", "white", "midnight blue", "arial", 45, "center", 270, 50]
pythonIcon = ["image", "E:\GUI_Builds\GUI_Install_Base\Images\pythonSnake.png", "midnight blue", "center", 530, 50]
installTitle = ["label", "Install:", "white", "midnight blue", "arial", 15, "center", 100, 120]
installText = ["label", "This options will allow you to go through the \ninstall process for Python Version 3.10",
               "white", "midnight blue", "arial", 8, "w", 100, 155]
repairTitle = ["label", "Repair:", "white", "midnight blue", "arial", 15, "center", 100, 220]
repairText = ["label", "This options will allow you to go through the \nrepair process for Python Version 3.10",
              "white", "midnight blue", "arial", 8, "w", 100, 255]
deleteTitle = ["label", "Delete:", "white", "midnight blue", "arial", 15, "center", 100, 320]
deleteText = ["label", "This options will allow you to go through the \nuninstall process for Python Version 3.10",
              "white", "midnight blue", "arial", 8, "w", 100, 355]

package = [window, button1, button2, button3, text, pythonIcon, installTitle, installText, repairTitle, repairText,
           deleteTitle, deleteText]

g.newBuild(package)
print(g.replyOut())
