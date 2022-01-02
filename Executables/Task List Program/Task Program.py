import subprocess

# , ['', ]
Known = [['chrome.exe', 10], ['svchost.exe', 11], ['Discord.exe', 11], ['Skype.exe', 9], ['mobsync.exe', 11], ['YourPhone.exe', 13], ['RuntimeBroker.exe', 17],
         ['dllhost.exe', 11], ['SearchApp.exe', 13], ['StartMenuExperienceHost.e', 25], ['backgroundTaskHost.exe', 22], ['Spotify.exe', 11],
         ['OverwolfBrowser.exe', 19], ['cmd.exe', 7], ['conhost.exe', 11], ['cncmd.exe', 9], ['OverwolfHelper.exe', 18], ['RadeonSoftware.exe', 18],
         ['smartscreen.exe', 15], ['backgroundTaskHost.exe', 22], ['tasklist.exe', 12], ['notepad++.exe', 13], ['python3.10.exe', 14], ['TextInputHost.exe', 17],
         ['ShellExperienceHost.exe', 23], ['pycharm64.exe', 13], ['OverwolfHelper64.exe', 20], ['explorer.exe', 12], ['GameBar.exe', 11], ['rundll32.exe', 12],
         ['Calculator.exe', 14], ['SystemSettings.exe', 18], ['GameBarFTServer.exe', 19], ['Video.UI.exe', 12], ['QtWebEngineProcess.exe', 22], ['AMDRSSrcExt.exe', 15],
         ['UserOOBEBroker.exe', 18], ['curseforge.exe', 14], ['Overwolf.exe', 12], ['taskhostw.exe', 13], ['dwm.exe', 7], ['atieclxx.exe', 12], ['winlogon.exe', 12],
         ['SettingSyncHost.exe', 19], ['RtkAudUService64.exe', 20], ['csrss.exe', 9], ['fontdrvhost.exe', 15], ['sihost.exe', 10], ['AUEPMaster.exe', 14],
         ['ctfmon.exe', 10], ['AMDRSServ.exe', 13], ['ApplicationFrameHost.exe', 24], ['amdow.exe', 9], ['SecurityHealthSystray.exe', 25], ['LocationNotificationWindo', 25],
         ['TaskListProgram.exe', 19],['notepad.exe', 11], ['SearchProtocolHost.exe', 22], ['OneDrive.exe', 12], ['Microsoft.Photos.exe', 20], ['TaskListProgram (1).exe', 23],
         ['msedge.exe', 10], ['Cortana.exe', 11], ['NVDisplay.Container.exe', 23], ['FileCoAuth.exe', 14], ['py.exe', 6], ['Teams.exe', 9], ['3CXWin8Phone.exe', 16],
         ['MapleTronics.exe', 16], ['python.exe', 10], ['VoicemodDesktop.exe', 19], ['YourPhoneServer.exe', 19], ['ScreenConnect.WindowsClie', 25], ['MusNotifyIcon.exe', 17]]

Flags = [['fsnotifier.exe', 14, 52]]


listOfLocal = []
listOfUnknown = []
listOfKnown = []
listOfFlags = []

subprocess.run("C:",shell=True)
subprocess.run("mkdir Output", shell=True)
subprocess.run("tasklist > Output\LocalTaskList.txt", shell=True)

local = open("Output\LocalTaskList.txt", 'r')

subprocess.run("cls",shell=True)

def start():
    for i in range(getLineCount() + 1):
        current_line = str(local.readline())
        Check(current_line)

    PrintScreen()
    checkUser()


def getLineCount():
    file = open("Output\LocalTaskList.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()

    return line_count

def Check(current_line):
    cont = 0


    if current_line[0:4] == "====":
        return
    if current_line[0:5] == "Image":
        return
    listOfLocal.append(current_line)
    if current_line[61:64] == " 0 ":
        listOfKnown.append(current_line)
        return

    for z in range(len(Flags)):
        if current_line[0:int(Flags[z][1])] == Flags[z][0]:
            listOfFlags.append(current_line)

    for y in range(len(Known)):
        if current_line[0:int(Known[y][1])] != Known[y][0] and len(current_line) != 0:
            cont +=1
    if cont == len(Known):
        listOfUnknown.append(current_line.strip())
    if cont < len(Known):
        listOfKnown.append(current_line.strip())

def PrintScreen():
    subprocess.run("cls", shell=True)
    print("Finished Scanning!\n\n")
    print("Number of Flags: " + str(len(listOfFlags)))
    print("Flags: \n")
    for flags in range(len(listOfFlags)):
        print("\t" + listOfFlags[flags] + "\tPercent of Being Bad :"+ str(Flags[flags][2]) +"%")
    print("\n\n")
    print("Number of Unknown Services: " + str(len(listOfUnknown)-1))
    print("Unknown Services: ")
    for unknown in range(len(listOfUnknown)):
        print("\t" + listOfUnknown[unknown])
    print("\n\n")
    print("Number of Known Services: " + str(len(listOfKnown)))
    print("Number of All Services: " + str(len(listOfLocal)-1))

def checkUser():
    over = False
    out = False
    while not over:
        next = input("\n\nIs there anything else I can help you with today?: ")
        if next.lower() == "kill task":
            while not out:
                after = input("What PID would you like to kill?: ")
                if after.lower() == "exit":
                    out = True
                subprocess.run("taskkill /F /T /PID " + str(after), shell=True)
                PrintScreen()
        if next.lower() == "exit":
            over = True
        if next.lower() == "show known":
            print("\n\n\n")
            for i in range(len(Known)):
                print("Name: " +str(Known[i][0]))
            print("Number of Known Sources: " + str(len(Known)))
        if next.lower() == "show flags":
            print("\n\n\n")
            for i in range(len(Flags)):
                print("Name: " + str(Flags[i][0]) + "     Percent: " + str(Flags[i][2]) + "%")
            print("Number of Flaged Sources: " + str(len(Flags)))

start()