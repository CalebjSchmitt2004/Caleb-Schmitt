import subprocess
import time


CurrentUser = (subprocess.check_output('echo %USERPROFILE%',shell=True)).decode('UTF-8').replace("\r\n",'')
CurrentUserName = (subprocess.check_output('echo %USERNAME%',shell=True)).decode('UTF-8').replace("\r\n",'')

Filename = str(CurrentUser) + "\Desktop\RemoveUsers\AllUsers.txt"
localUsers = str(CurrentUser) + "\Desktop\RemoveUsers\Local.txt"
adminUsers = str(CurrentUser) + "\Desktop\RemoveUsers\Admin.txt"
defaultUsers = str(CurrentUser) + "\Desktop\RemoveUsers\Default.txt"

subprocess.run("mkdir " + str(CurrentUser) + "\Desktop\RemoveUsers", shell=True)
subprocess.run('powershell Get-LocalUser > ' + str(Filename),shell=True)

Localusers = []
Adminusers = []
Defaultusers = []

numTrue = 0

def start():
    global numTrue
    file = open(str(Filename), 'r')

    for i in range(getLineCount()):
        current = file.readline()

        if (str(current))[0:4] == "Name":
            continue
        if (str(current))[0:4] == "----":
            continue
        if (str(current))[0:4] == "Admi":
            Adminusers.append(str(current))
            continue
        if (str(current))[0:4] == "Defa":
            Defaultusers.append(str(current))
            continue
        if (str(current))[0:4] == "Gues":
            Defaultusers.append(str(current))
            continue
        if (str(current))[0:2] == "\n":
            continue
        if (str(current))[0:int(len(CurrentUserName))] == str(CurrentUserName):
            continue
        if (str(current))[19:23] == "True":
            numTrue += 1

        Localusers.append(str(current))

    print(numTrue)

    AppendLocal()
    AppendAdmin()
    AppendDefault()

    DeleteUser(Localusers)

def getLineCount():
    file = open(str(Filename), "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    return line_count


def AppendLocal():
    local = open(str(localUsers), 'w')
    for i in range(len(Localusers)):
        if i > 0:
            local.write("\n")
        local.write(str(Localusers[i])[0:19].replace(" ", ""))

def AppendAdmin():
    local = open(str(adminUsers), 'w')
    for i in range(len(Adminusers)):
        if i > 0:
            local.write("\n")
        local.write(str(Adminusers[i])[0:19].replace(" ", ""))
        
def AppendDefault():
    local = open(str(defaultUsers), 'w')
    for i in range(len(Defaultusers)):
        if i > 0:
            local.write("\n")
        local.write(str(Defaultusers[i])[0:19].replace(" ", ""))

def DeleteUser(local):
    file = open(str(localUsers), 'r')

    for i in range(len(local)):
        current = file.readline()
        subprocess.run('powershell Remove-LocalUser -Name "' + str(current) + '"', shell=True)
        subprocess.run("cd " + str(CurrentUser), shell=True)
        subprocess.run("cd ..",shell=True)
        subprocess.run("echo %CD%",shell=True)
        subprocess.run("rmdir /s /q " + str(current) + "\*", shell=True)
    file.close

    subprocess.run("cls", shell=True)
    print("Number of Users Removed: " + str(len(local)))
    print("\nUsers Removed: ")
    file = open(str(localUsers), 'r')
    for t in range(len(local)):
        current = file.readline()
        print("\n" + str(current))
    subprocess.run("pause", shell=True)

def WarningPage():
    subprocess.run("cls",shell=True)
    print("Warning: \n\nThis program has been designed to remove and delete all local user accounts and data on this machine."
          "\nPlease before continuing verify that you have access to the Default Admin Account or a Domain Admin."
          "\nThis Program will not delete the current logged in user. \nIf you have any qestions on how this program please contact Caleb Schmitt at MapleTronics Computers.\n\n\n\n\n\n\n")
    subprocess.run("pause", shell=True)
    subprocess.run("cls",shell=True)
    passcode = input("Passcode: ")
    if str(passcode) == '4385054631':
        print("\n\nThank you for verifying.")
        print("\nProgram will start in 5 Seconds.")
        time.sleep(5)
        start()

WarningPage()