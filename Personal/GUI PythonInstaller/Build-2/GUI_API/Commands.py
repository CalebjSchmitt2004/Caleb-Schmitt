import subprocess as sb

def Command(command):
    if command == "pythonInstall":
        installer()
    if command == "pythonRepair":
        repairer()
    if command == "pythonUninstall":
        uninstaller()

def installer():
    print("Installing Python Version 3.10:")
    sb.run("mkdir E:\GUI_Builds\GUI_Install_Base\PythonAssets", shell=True)
    sb.run("type nul > E:\GUI_Builds\GUI_Install_Base\PythonAssets\installer.ps1", shell=True)

    install = open("E:\GUI_Builds\GUI_Install_Base\PythonAssets\installer.ps1", 'w')
    install.write("")
    install.write("")
    install.write("")
    install.close()

def repairer():
    print("Repairing Python Version 3.10:")
    sb.run("mkdir E:\GUI_Builds\GUI_Install_Base\PythonAssets", shell=True)
    sb.run("type nul > E:\GUI_Builds\GUI_Install_Base\PythonAssets\\repair.ps1", shell=True)

    repair = open("E:\GUI_Builds\GUI_Install_Base\PythonAssets\\repair.ps1", 'w')
    repair.write("")
    repair.write("")
    repair.write("")
    repair.close()

def uninstaller():
    print("Uninstalling Python Version 3.10:")
    sb.run("mkdir E:\GUI_Builds\GUI_Install_Base\PythonAssets", shell=True)
    sb.run("type nul > E:\GUI_Builds\GUI_Install_Base\PythonAssets\\uninstall.ps1", shell=True)

    uninstall = open("E:\GUI_Builds\GUI_Install_Base\PythonAssets\\uninstall.ps1", 'w')
    uninstall.write("")
    uninstall.write("")
    uninstall.write("")
    uninstall.close()
