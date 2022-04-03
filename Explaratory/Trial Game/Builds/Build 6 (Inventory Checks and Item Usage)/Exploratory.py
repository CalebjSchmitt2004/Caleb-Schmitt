import os
from time import sleep
import keyboard

# Level Variables
levelList = [["Box1", 7, 5]]

# Entity Variables
# ["Magic Door", "Developer Mode", "+∞", 1, 7, 0]
entityList = [["Plant", "Berries", "+3", 1, 2, 4], ["Snake", "Venom", "-3", 1, 7, 5]]

# Item Variables
itemList = [["Stick", "-1", 5, 5, 3]]
craftableItems = [["Poisoned Stick", "-4", 10, "Stick", "Venom"]]

# Player Variables
xpos = 0
ypos = 0
characterLocation = ""
Moveable = [True, True, True, True]
numHearts = 10
numGold = 0
numArmour = 0
Health = ""
playerInventory = []
itemHotbar = ["Empty Hand", "Empty Hand", "Empty Hand", "Empty Hand", "Empty Hand"]
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
        "|.......š|",
        "----------"]


def updateVars():
    global Health

    Health = ""
    for i in range(numHearts):
        Health += "♥"


def startGame():
    # titleScreen()
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

    while not gameOver:
        updateVars()
        Draw(Box1)
        locationCheck()
        if Wall > 0:
            print("\033[1m" + "You hit a wall" + "\033[0m")
            Wall -= 1
        if keyboard.read_key():
            if keyboard.is_pressed('w') and Moveable[0]:  # if key 'q' is pressed
                updateCharacterPos("Up")
            if keyboard.is_pressed('s') and Moveable[1]:  # if key 'q' is pressed
                updateCharacterPos("Down")
            if keyboard.is_pressed('a') and Moveable[2]:  # if key 'q' is pressed
                updateCharacterPos("Left")
            if keyboard.is_pressed('d') and Moveable[3]:  # if key 'q' is pressed
                updateCharacterPos("Right")
            if keyboard.is_pressed('q'):
                openInventory()
            if keyboard.is_pressed('e'):
                openCrafting()
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
        # cheatMode = True
        # pass
        # if keyboard.is_pressed("~"):
        # DeveloperMode()


def updateCharacterPos(move):
    global xpos, ypos, Wall, limit, characterLocation

    row = xpos + 1
    column = ypos + 1
    if levelList[0][1] > xpos >= int(limit) and move == "Right" or cheatMode and move == "Right":
        levelColumn1 = Box1[column]
        newLevelColumn = str(levelColumn1[:row]) + ".@" + str(levelColumn1[row + 2:])
        Box1[column] = str(newLevelColumn)
        xpos += 1
        characterLocation = str(xpos) + ":" + str(ypos)
    elif levelList[0][1] >= xpos > int(limit) and move == "Left" or cheatMode and move == "Left":
        levelColumn1 = Box1[column]
        newLevelColumn = str(levelColumn1[:row - 1]) + "@." + str(levelColumn1[row + 1:])
        Box1[column] = str(newLevelColumn)
        xpos -= 1
        characterLocation = str(xpos) + ":" + str(ypos)
    elif levelList[0][2] >= ypos > int(limit) and move == "Up" or cheatMode and move == "Up":
        levelColumn1 = Box1[column - 1]
        levelColumn2 = Box1[column]
        newLevelColumn1 = str(levelColumn1[:row]) + "@" + str(levelColumn1[row + 1:])
        newLevelColumn2 = str(levelColumn2[:row]) + "." + str(levelColumn2[row + 1:])
        Box1[column - 1] = str(newLevelColumn1)
        Box1[column] = str(newLevelColumn2)
        ypos -= 1
        characterLocation = str(xpos) + ":" + str(ypos)
    elif levelList[0][2] > ypos >= int(limit) and move == "Down" or cheatMode and move == "Down":
        levelColumn1 = Box1[column]
        levelColumn2 = Box1[column + 1]
        newLevelColumn1 = str(levelColumn1[:row]) + "." + str(levelColumn1[row + 1:])
        newLevelColumn2 = str(levelColumn2[:row]) + "@" + str(levelColumn2[row + 1:])
        Box1[column] = str(newLevelColumn1)
        Box1[column + 1] = str(newLevelColumn2)
        ypos += 1
        characterLocation = str(xpos) + ":" + str(ypos)
    else:
        Wall += 1


def locationCheck():
    for item in itemList:
        if item[3] == xpos and item[4] == ypos and item[3] != -1 and item[4] != -1:
            playerInventory.append(item)
            itemList.remove(item)
            print("New Item Obtained")


def openInventory():
    os.system("cls")
    print("     Player Inventory")
    print("Item" + "\tDamage" + "\tDurability\n")
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


def openCrafting():
    global playerInventory

    os.system("cls")
    print("     Crafting Mode")
    print("Item" + "\tDamage" + "\tDurability\n")
    for item in playerInventory:
        print(str(item[0]) + "\t   " + str(item[1]) + "\t   " + str(item[2]))

    print("\n     Available to Craft")
    print("Item" + "\t\tDamage" + "\t\tDurability\n")

    itemThatWork = []

    for Citem in craftableItems:
        part = 0
        for Pitem in playerInventory:
            if Pitem[0] == Citem[3] or Pitem[0] == Citem[4]:
                part += 1
        if part == 2:
            itemThatWork.append(Citem)

    if len(itemThatWork) == 0:
        print("No Craftable Items Available")
    else:
        for item in itemThatWork:
            print(str(item[0]) + "\t   " + str(item[1]) + "\t   " + str(item[2]))

    whatToCraft = input("\n\nWhat Item would you like to craft?: ")

    for item in itemThatWork:
        if whatToCraft == item[0]:
            playerInventory.append([str(item[0]), item[1], item[2]])
            for Pitem in playerInventory:
                if Pitem[0] == item[3]:
                    playerInventory.remove(Pitem)
                if Pitem[0] == item[4]:
                    playerInventory.remove(Pitem)

            print("New Item Crafted: " + str(item[0]))
            sleep(2)


def equip(hotkey):
    global itemHotbar

    itemToAssign = input("\nWhat item would you like to equip to hotkey " + str(hotkey + 1) + "?: ")
    for item in playerInventory:
        if item[0] == itemToAssign:
            itemHotbar[hotkey] = item[0]
            print("New Item " + item[0] + " Assigned to Hotkey " + str(hotkey + 1))
            sleep(.5)


def attack():
    if len(entityList) == 0:
        print("\nAttack with " + str(itemInHand) + " missed entity: Air!")
    else:
        for entity in entityList:
            if entity[0] == "Magic Door":
                print("Developer Mode: Activated")
                print("Use the grave key (~) to use developer mode")
            if xpos + 1 == entity[4] and ypos == entity[5]:
                levelColumn1 = Box1[ypos + 1]
                newLevelColumn1 = str(levelColumn1[:xpos + 2]) + "." + str(levelColumn1[xpos + 3:])
                Box1[ypos + 1] = str(newLevelColumn1)
                addItemToPlayer(str(entity[1]), entity[2], entity[3], entity)
            elif xpos - 1 == entity[4] and ypos == entity[5]:
                levelColumn1 = Box1[ypos + 1]
                newLevelColumn2 = str(levelColumn1[:xpos]) + "." + str(levelColumn1[xpos + 1:])
                Box1[ypos + 1] = str(newLevelColumn2)
                addItemToPlayer(str(entity[1]), entity[2], entity[3], entity)
            elif xpos == entity[4] and ypos + 1 == entity[5]:
                levelColumn1 = Box1[ypos + 2]
                newLevelColumn3 = str(levelColumn1[:xpos + 1]) + "." + str(levelColumn1[xpos + 2:])
                Box1[ypos + 2] = str(newLevelColumn3)
                addItemToPlayer(str(entity[1]), entity[2], entity[3], entity)
            elif xpos == entity[4] and ypos - 1 == entity[5]:
                levelColumn1 = Box1[ypos]
                newLevelColumn4 = str(levelColumn1[:xpos + 1]) + "." + str(levelColumn1[xpos + 2:])
                Box1[ypos] = str(newLevelColumn4)
                addItemToPlayer(str(entity[1]), entity[2], entity[3], entity)
            else:
                print("\nAttack with " + str(itemInHand) + " missed entity: Air!")
    sleep(2)


def addItemToPlayer(entityName, entityDamage, entityDurability, entity):
    global numHearts

    if itemInHand == "Empty Hand":
        numHearts -= 1

    print("You have broken a\\an " + entityName)
    print("From " + entityName + " you have received " + str(entityDamage) + " " + str(entityDurability))
    playerInventory.append([str(entityName), entityDamage, entityDurability])
    entityList.remove(entity)


def Draw(item):
    global ypos

    os.system("cls")
    if item == Box1:
        for item in Box1:
            print(str(item))
        print("\n\n")
        print("Current Item in Hand: " + str(itemInHand) + "\nHealth: " + str(Health) + "\tArmour: " + str(
            numArmour) + "\tGold: " + str(numGold))


def credits():
    os.system("cls")
    print("\t\tRogue Credits\n")
    print("\tIdea for game by: Thomas Evritt")
    print("\tDesigning by: Caleb Schmitt")
    print("\tProgramming by: Caleb Schmitt")
    print("\tSecret Break the Game Cheat Code by: Pedro Reyes")
    print("\tGame Item Ideas from: Caleb Schmitt")
    print("\tGame Entity's from: Caleb Schmitt")


def DeveloperMode():
    global numGold, numHearts, numArmour, playerInventory

    os.system("cls")
    print("\t\tWelcome to Developer Mode")
    print("\n\t\t Commands:")
    print("AddGold")
    print("AddHealth")
    print("AddItem")
    print("AddArmour")

    command = input("Please enter a command: ")

    if command.lower() == "addgold":
        question = input("How much gold would you like to give yourself?: ")
        numGold += int(question)
    if command.lower() == "addhealth":
        question = input("How much health would you like to give yourself?: ")
        numHearts += int(question)
    if command.lower() == "addarmour":
        question = input("How much gold would you like to give yourself?: ")
        numArmour += int(question)
    if command.lower() == "additem":
        question = input("What item would you like to give yourself?: ")
        for item in itemList:
            if item[0] == str(question):
                playerInventory.append(item)
                itemList.remove(item)


startGame()
