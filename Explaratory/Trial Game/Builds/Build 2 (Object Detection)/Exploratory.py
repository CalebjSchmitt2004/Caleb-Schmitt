import os
from time import sleep
import keyboard

levelList = [["Box1", 7, 5]]
itemList = [["Stick", "-1", 5, 5, 3]]
entityList = [["Plant", "Berries", "+3", 1, 2, 4]]
playerInventory = []

GameVersion = "Pre-Build" + " - " + "0.0.1"
gameOver = False
xpos = 0
ypos = 0
limit = 0
characterLocation = ""
Wall = 0
cheatMode = False
Moveable = [True,True,True,True]
itemHotbar = ["No Item Selected","No Item Selected","No Item Selected","No Item Selected","No Item Selected"]
itemInHand = "Empty Hand"
numHearts = 10
numGold = 0
numArmour = 0
Health = ""
for i in range(numHearts):
    Health += "♥"

Box1 = ["----------",
        "|@.......|",
        "|........|",
        "|........|",
        "|.....\..|",
        "|..↑.....+",
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
    global Wall, cheatMode, itemInHand
    
    while gameOver == False:
        Draw(Box1)
        locationCheck()
        if Wall > 0:
            print("\033[1m" + "You hit a wall" + "\033[0m")
            print(characterLocation)
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
        elif xpos -1 == entityList[4]:
            pass
        elif ypos +1 == entityList[5]:
            pass
        elif ypos -1 == entityList[5]:
            pass
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

startGame()