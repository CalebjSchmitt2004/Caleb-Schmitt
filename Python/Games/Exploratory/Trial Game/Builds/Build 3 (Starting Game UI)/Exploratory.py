import os
from time import sleep
import keyboard

# Level Varibles
levelList = [["Box1", 7, 5]]

# Entity Varibles
entityList = [["Plant", "Berries", "+3", 1, 2, 4]]

# Item Varibles
itemList = [["Stick", "-1", 5, 5, 3]]

# Player Varibles
xpos = 0
ypos = 0
characterLocation = ""
Moveable = [True,True,True,True]
numHearts = 10
numGold = 0
numArmour = 0
Health = ""
playerInventory = []
itemHotbar = ["No Item Selected","No Item Selected","No Item Selected","No Item Selected","No Item Selected"]
itemInHand = "Empty Hand"

# Game Information
GameVersion = "Pre-Build" + " - " + "0.0.1"
gameOver = False
limit = 0
Wall = 0
cheatMode = False


Box1 = ["----------",
        "|@.......|",
        "|........|",
        "|........|",
        "|.....\..|",
        "|..↑.....+",
        "|........|",
        "----------"]

def updateVars():
    global Health

    Health = ""
    for i in range(numHearts):
        Health += "♥"

def startGame():
    #titleScreen()
    gameInput()

def titleScreen():
    os.system("cls")
    print("\tWelcome to Rouge")
    print("\n    Start Game - Coming Soon")
    print("\t     Trial")
    print("\t    Credits\n")
    print("\t Game Version: \n       " + str(GameVersion))

    mainScreenSelection = input("\n\nPlease select an option: ")
    if mainScreenSelection.lower() == "trial":
        gameInput()
    elif mainScreenSelection.lower() == "credits":
        credits()
                
def gameInput():
    global Wall, cheatMode, itemInHand
    
    while gameOver == False:
        updateVars()
        Draw(Box1)
        locationCheck()
        if Wall > 0:
            print("\033[1m" + "You hit a wall" + "\033[0m")
            Wall-=1
        if keyboard.read_key():
            if keyboard.is_pressed('w') and Moveable[0]:  # if key 'q' is pressed
                updateCharecterPos("Up")
            if keyboard.is_pressed('s') and Moveable[1]:  # if key 'q' is pressed
                updateCharecterPos("Down")
            if keyboard.is_pressed('a') and Moveable[2]:  # if key 'q' is pressed
                updateCharecterPos("Left")
            if keyboard.is_pressed('d') and Moveable[3]:  # if key 'q' is pressed
                updateCharecterPos("Right")
            if keyboard.is_pressed('q'):
                openInventory()
            if keyboard.is_pressed('space'):
                attack()
            if keyboard.is_pressed('1'):
                itemInHand = itemHotbar[0]
                print("Item Selected:" + str(itemInHand))
                sleep(.2)
            if keyboard.is_pressed('2'):
                itemInHand = itemHotbar[1]
                print("Item Selected:" + str(itemInHand))
                sleep(.2)
            if keyboard.is_pressed('3'):
                itemInHand = itemHotbar[2]
                print("Item Selected:" + str(itemInHand))
                sleep(.2)
            if keyboard.is_pressed('4'):
                itemInHand = itemHotbar[3]
                print("Item Selected:" + str(itemInHand))
                sleep(.2)
            if keyboard.is_pressed('5'):
                itemInHand = itemHotbar[4]
                print("Item Selected:" + str(itemInHand))
                sleep(.2)
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

def locationCheck():
    for item in itemList:
        if item[3] == xpos and item[4] == ypos:
            playerInventory.append(item)
            itemList.remove(item)
            print("New Item Obtained")

def openInventory():
    os.system("cls")
    print("     Player Invintory")
    print("Item" + "\tDamage" + "\tDuriblilty\n")
    for item in playerInventory:
        print(str(item[0]) + "\t   " + str(item[1]) + "\t   " + str(item[2]))

    sleep(.5)
    if keyboard.read_key():
        if keyboard.is_pressed("q"):
            pass
        if keyboard.is_pressed('1'):
            equip(0)
        if keyboard.is_pressed('2'):
            equip(1)
        if keyboard.is_pressed('3'):
            equip(2)
        if keyboard.is_pressed('4'):
            equip(3)
        if keyboard.is_pressed('5'):
            equip(4)

def equip(hotkey):
    global itemHotbar

    itemToAssign = input("\nWhat item would you like to equip to hotkey " + str(hotkey+1) + "?: ")
    for item in playerInventory:
        if item[0] == itemToAssign:
            itemHotbar[hotkey] = item[0]
            print("New Item " + item[0] + " Assiened to Hotkey " + str(hotkey+1))
            sleep(.5)

def attack():
    for entity in entityList:
        if xpos +1 == entity[4]:
            levelColum1 = Box1[ypos+1]
            newLevelColum = str(levelColum1[:xpos+2]) + "." + str(levelColum1[xpos+3:])
            Box1[ypos+1] = str(newLevelColum)
            print("You have broken a\\an " + entity[0])
            print("From " + entity[0] + " you have recived " + str(entity[2]) + " " + str(entity[1]))
            playerInventory.append([str(entity[1]), entity[2], entity[3]])
        elif xpos -1 == entity[4]:
            levelColum1 = Box1[ypos + 1]
            newLevelColum = str(levelColum1[:xpos]) + "." + str(levelColum1[xpos + 1:])
            Box1[ypos + 1] = str(newLevelColum)
            print("You have broken a\\an " + entity[0])
            print("From " + entity[0] + " you have recived " + str(entity[2]) + " " + str(entity[1]))
            playerInventory.append([str(entity[1]), entity[2], entity[3]])
        elif ypos +1 == entity[5]:
            levelColum1 = Box1[ypos + 2]
            newLevelColum = str(levelColum1[:xpos+1]) + "." + str(levelColum1[xpos+2:])
            Box1[ypos + 2] = str(newLevelColum)
            print("You have broken a\\an " + entity[0])
            print("From " + entity[0] + " you have recived " + str(entity[2]) + " " + str(entity[1]))
            playerInventory.append([str(entity[1]), entity[2], entity[3]])
        elif ypos -1 == entity[5]:
            levelColum1 = Box1[ypos]
            newLevelColum = str(levelColum1[:xpos + 1]) + "." + str(levelColum1[xpos + 2:])
            Box1[ypos] = str(newLevelColum)
            print("You have broken a\\an " + entity[0])
            print("From " + entity[0] + " you have recived " + str(entity[2]) + " " + str(entity[1]))
            playerInventory.append([str(entity[1]), entity[2], entity[3]])
        else:
            print("\nAttack with " + str(itemInHand) + " missed entity: Air!")
    sleep(2)

def Draw(item):
    global ypos

    os.system("cls")
    if item == Box1:
        for item in Box1:
            print(str(item))
        print("\n\n")
        print("Current Item in Hand: " + str(itemInHand) + "\nHealth: " + str(Health) + "\tArmour: " + str(numArmour) + "\tGold: " + str(numGold))

def credits():
    os.system("cls")
    print("\t\tRogue Credits\n")
    print("\tIdea for game by: Thomas Evritt")
    print("\tDesigning by: Caleb Schmitt")
    print("\tProgramming by: Caleb Schmitt")
    print("\tSecret Break the Game Cheat Code by: Pedro Reyes")
    print("\tGame Item Ideas from: Caleb Schmitt")
    print("\tGame Entitys from: Caleb Schmitt")


startGame()