import os
from time import sleep
import keyboard

levelList = [["Box1", 7, 5]]

GameVersion = "Pre-Build" + " - " + "0.0.1"
gameOver = False
xpos = 0
ypos = 0
limit = 0
characterLocation = ""
Wall = 0
cheatMode = False
Moveable = [True,True,True,True]


Box1 = ["----------",
        "|@.......|",
        "|........|",
        "|........|",
        "|........|",
        "|........+",
        "|........|",
        "----------"]

def startGame():
    gameInput()
    
def titleScreen():
    print("Game Version: " + str(GameVersion))
    print("\n\n\t\t" + "  Welcome to rogue\n")
    print("\t\t     " + "\u0332".join("Level List:"))
    for level in levelList:
        print("\t\t\t" + str(level[0]))
        
    levelSelect = input("\nPlease enter a level to play: ")
    levelLoader(levelSelect)
    
def levelLoader(levelSelect):
    for level in levelList:
        if str(level[0].lower()) == str(levelSelect.lower()):
            if levelSelect.lower() == "trial":
                print("\n\nLoading Level: Trial\n")

                
def gameInput():
    global Wall, cheatMode
    
    while gameOver == False:
        Draw(Box1)
        if Wall > 0:
            print("\033[1m" + "You hit a wall" + "\033[0m")
            print(characterLocation)
            Wall-=1
        if keyboard.read_key():
            if keyboard.is_pressed('up') and Moveable[0]:  # if key 'q' is pressed
                updateCharecterPos("Up")
            if keyboard.is_pressed('down') and Moveable[1]:  # if key 'q' is pressed
                updateCharecterPos("Down")
            if keyboard.is_pressed('left') and Moveable[2]:  # if key 'q' is pressed
                updateCharecterPos("Left")
            if keyboard.is_pressed('right') and Moveable[3]:  # if key 'q' is pressed
                updateCharecterPos("Right")
            sleep(.10)
       # if movement.lower() == "uuddlrlrab":
            #cheatMode = True
            #pass
            
              
def updateCharecterPos(move):
    global xpos, ypos, Wall, limit, characterLocation
    
    row = xpos + 1
    colum = ypos + 1
    newLevelColum = ""
    if xpos < levelList[0][1] and xpos >= int(limit) and move == "Right" or cheatMode == True and move == "Right":
        levelColum1 = Box1[colum]
        newLevelColum = str(levelColum1[:row]) + ".@" + str(levelColum1[row+2:])
        Box1[colum] = str(newLevelColum)
        xpos+=1
        ChacterLocation = str(xpos) + ":" + str(ypos)
    elif xpos <= levelList[0][1] and xpos > int(limit) and move == "Left" or cheatMode == True and move == "Left":
        levelColum1 = Box1[colum]
        newLevelColum = str(levelColum1[:row-1]) + "@." + str(levelColum1[row+1:])
        Box1[colum] = str(newLevelColum)
        xpos-=1
        ChacterLocation = str(xpos) + ":" + str(ypos)
    elif ypos <= levelList[0][2] and ypos > int(limit) and move == "Up" or cheatMode == True and move == "Up":
        levelColum1 = Box1[colum-1]
        levelColum2 = Box1[colum]
        newLevelColum1 = str(levelColum1[:row]) + "@" + str(levelColum1[row+1:])
        newLevelColum2 = str(levelColum2[:row]) + "." + str(levelColum2[row+1:])
        Box1[colum-1] = str(newLevelColum1)
        Box1[colum] = str(newLevelColum2)
        ypos-=1
        ChacterLocation = str(xpos) + ":" + str(ypos)
    elif ypos < levelList[0][2] and ypos >= int(limit) and move == "Down" or cheatMode == True and move == "Down":
        levelColum1 = Box1[colum]
        levelColum2 = Box1[colum + 1]
        newLevelColum1 = str(levelColum1[:row]) + "." + str(levelColum1[row+1:])
        newLevelColum2 = str(levelColum2[:row]) + "@" + str(levelColum2[row+1:])
        Box1[colum] = str(newLevelColum1)
        Box1[colum+1] = str(newLevelColum2)
        ypos+=1
        ChacterLocation = str(xpos) + ":" + str(ypos)
    else:
        Wall+=1
    

def Draw(item):
    global ypos

    os.system("cls")
    if item == Box1:
        for item in Box1:
            print(str(item))

startGame()