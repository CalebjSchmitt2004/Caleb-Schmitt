import datetime
import subprocess
import random

# Player Variables
currentBalance = 100
currentScore = 0
currentBid = 0
currentDeck = []
numOfWins = 0
numOfLoses = 0
PlayerChance = 14
goodStartBid = False
fundsEmpty = False
playerBust = False

# Game Variables
startBid = 0
entryPrice = 0
totalBid = 0
roundNumber = 1
tiedGames = 0
Time = 0
availableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
GameOver = False
gotAce = False
Decided = False

# Computer Variables
computerScore = 0
computerWins = 0
computerLoses = 0
ComputerChance = 14
computerDeck = []
computerBust = False


def start():
    # Imported Variables for the Game
    title = ("title Black Jack     By: Caleb J. Schmitt"+" ---- "+"Build Release Date: 12/8/21")
    subprocess.run(str(title), shell=True)

    global startBid, currentBalance, currentBid, GameOver, currentScore, roundNumber, totalBid, computerLoses, computerWins, numOfWins, goodStartBid, totalBid, entryPrice, fundsEmpty, numOfLoses, gotAce, computerBust, \
        playerBust, ComputerChance, PlayerChance, tiedGames

    # Calculates Computers Score
    computer()

    # Verify player still has money to play
    if currentBalance <= 5:
        fundsEmpty = True

    # Actions if player has no more money
    while fundsEmpty:
        subprocess.run("cls", shell=True)
        print("Current Balance: $" + str(currentBalance))
        print("Not enough funds to play!!")
        print("Sorry")
        command = input("\n$: ")
        if command.lower() == "add funds":
            add = input("How much money would you like to add?: ")
            currentBalance += int(add)
            fundsEmpty = False
        if command.lower() == "wins":
            wins = input("How many wins would you like?: ")
            numOfWins = int(wins)
        if command.lower() == "loses":
            loses = input("How many loses would you like?: ")
            numOfLoses = int(loses)
        if command.lower() == "computer chance":
            cc = input("Enter Chance: ")
            ComputerChance = cc
        if command.lower() == "player chance":
            pc = input("Enter Chance: ")
            PlayerChance = pc
        if command.lower() == "start":
            reset()
            start()

    # Players first to cards
    currentDeck.append(random.randint(1, 14))
    currentDeck.append(random.randint(1, 14))

    # Players first calculated score
    for i in range(len(currentDeck)):
        calcScore(currentDeck[i])

    # Prints game screen
    printScreen()

    # Verify the Player isn't trying to spend more money then they have
    while not goodStartBid:
        startBid = 0
        entryPrice = 0
        currentBid = 0
        totalBid = 0
        startBid = int(input("What is your starting bid?: $"))
        calcEntryPrice(int(startBid))
        currentBid += int(startBid)
        totalBid = currentBid + entryPrice
        if totalBid > currentBalance:
            print("Invalid Bid")
        elif totalBid <= currentBalance:
            goodStartBid = True

    # All the Game Logic
    while not GameOver:
        printScreen()
        nextMove = input("Hit, Stay, Double: ")
        # Auto play
        if nextMove.lower() == "autoplay" or nextMove.lower() == "ap":
            loop = input("How many plays would you like to run though?: ")
            betAmount = input("How much is the play bet amount?: ")
            subprocess.run("cls", shell=True)
            begin = datetime.datetime.now()
            for i in range(int(loop)):
                if i <= int(loop):
                    autoplay(betAmount)
                    print("Playing Round Number: #"+str(roundNumber)+"/#"+str(loop)+"   "+"Percent Done: "+str(round((i/int(loop)*100),2))+"%", end='\r')
            end = datetime.datetime.now() - begin
            total = end.seconds
            timeDone = calcTime(total)
            print("\n\n\nAutoPlay Completed its moves in:\n"+"\nDays: "+str(timeDone[0])+"\nHours: "+str(timeDone[1])+"\nMinutes: "+str(timeDone[2])+"\nSeconds: "+str(timeDone[3])+"\n")
            subprocess.run("pause",shell=True)
        # Player Hit
        if nextMove.lower() == "hit":
            currentDeck.append(random.randint(1, 14))
            calcScore(currentDeck[len(currentDeck) - 1])

        # Player Double
        if nextMove.lower() == "double":
            currentDeck.append(random.randint(1, 14))
            calcScore(currentDeck[len(currentDeck) - 1])
            currentBid += startBid
            totalBid = currentBid + entryPrice

        # Player Stay
        if nextMove.lower() == "stay":
            global Decided
            if computerScore > 21 and not Decided:
                computerBust = True
                Decided = True
                subprocess.run("cls", shell=True)
                print("Game Over!!!")
                print("Computer Busted Congratulations!!")
                print("\nMoney Won!!: $" + str(totalBid))
                print("Player Score: " + str(currentScore))
                print("Computer Score: " + str(computerScore) + "\n")
                again = input("would you like to play again?: ")
                if again == "yes" or again == "y":
                    roundNumber += 1
                    numOfWins += 1
                    currentBalance += totalBid
                    reset()
                    start()
                if again == "no" or again == "n":
                    GameOver = True
                    currentBalance += totalBid
                    numOfWins += 1
                    endGame()
            if currentScore < computerScore and not Decided:
                subprocess.run("cls", shell=True)
                Decided = True
                print("Game Lost")
                print("The Computer Won!!")
                print("\nMoney Lost!!: $" + str(totalBid))
                print("Player Score: " + str(currentScore))
                print("Computer Score: " + str(computerScore) + "\n")
                again = input("would you like to play again?: ")
                if again == "yes" or again == "y":
                    currentBalance -= totalBid
                    roundNumber += 1
                    resetLost()
                    computerWins += 1
                    reset()
                    start()
                if again == "no" or again == "n":
                    GameOver = True
                    currentBalance -= totalBid
                    numOfLoses += 1
                    computerWins += 1
                    endGame()
            if currentScore > computerScore and not Decided:
                subprocess.run("cls", shell=True)
                Decided = True
                print("Game Won!!!")
                print("Congratulations")
                print("\nMoney Won!!: $" + str(totalBid))
                print("Player Score: " + str(currentScore))
                print("Computer Score: " + str(computerScore) + "\n")
                again = input("would you like to play again?: ")
                if again == "yes" or again == "y":
                    currentBalance += totalBid
                    roundNumber += 1
                    resetWon()
                    computerLoses += 1
                    reset()
                    start()
                if again == "no" or again == "n":
                    GameOver = True
                    currentBalance += totalBid
                    numOfWins += 1
                    computerLoses += 1
                    endGame()
            if currentScore == computerScore and not Decided:
                subprocess.run("cls", shell=True)
                Decided = True
                print("Game Tie!!!")
                print("Congratulations")
                print("\nPlayer Score: " + str(currentScore))
                print("Computer Score: " + str(computerScore) + "\n")
                again = input("would you like to play again?: ")
                if again == "yes" or again == "y":
                    roundNumber += 1
                    tiedGames +=1
                    reset()
                    start()
                if again == "no" or again == "n":
                    tiedGames +=1
                    endGame()
                    GameOver = True

        # Auto change Ace from +11 to +1
        if int(currentScore) > 21 and not gotAce:
            for i in range(len(currentDeck)):
                if currentDeck[i] == 14:
                    currentScore -= 10
                    gotAce = True
                    printScreen()
        if int(currentScore) > 21 and not playerBust:
            playerBust = True
            subprocess.run("cls", shell=True)
            print("GameOver!!")
            print("Player Busted")
            print("\nMoney Lost!!: $" + str(totalBid))
            print("Player Ending Score: " + str(currentScore))
            print("Computer Ending Score: " + str(computerScore))
            again = input("\nWould you like to play again?: ")
            if again == "yes" or again == "y":
                currentBalance -= totalBid
                roundNumber += 1
                computerWins += 1
                reset()
                resetLost()
                start()
            if again == "no" or again == "n":
                currentBalance -= totalBid
                computerWins += 1
                endGame()
                GameOver = True


def endGame():
    subprocess.run("cls", shell=True)
    print("Endgame Balance: " + str(currentBalance))
    print("Final Round Number: " + str(roundNumber))
    print("\n\nPlayer Wins: " + str(numOfWins) + "  " + "\nPlayer Loses: " + str(numOfLoses) + "  " + "\nTied: " + str(tiedGames) + "  " + "\nPlayer Ratio: " + str(round(int(numOfWins/roundNumber*100)))+ "%" + " : " + str(round(int(numOfLoses/roundNumber*100)))+ "%"  +" - " + str(round(int(tiedGames/roundNumber*100)))+ "%")
    print("\n\nComputer Wins: " + str(computerWins) + "  " "\nComputer Loses: " + str(computerLoses) + "  " + "\nTied: "+ str(tiedGames) + "  " "\nComputer Ratio: " + str(round(int(computerWins/roundNumber*100)))+ "%"  + " : " + str(round(int(computerLoses/roundNumber*100)))+ "%" + " - "+ str(round(int(tiedGames/roundNumber*100))) + "%")
    print("\n\nPlayer Versus Computer Ratio: " + str(round(int(numOfWins/roundNumber*100)))+ "%" + " : " + str(round(int(computerWins/roundNumber*100)))+ "%"  + " - " + str(round(int(tiedGames/roundNumber*100))) + "%")

    print("\n\n"+str(round(int(numOfWins/roundNumber*100))+round(int(computerWins/roundNumber*100))+round(int(tiedGames/roundNumber*100)))+"% Out of 100%.")
    print(str(100-(round(int(numOfWins/roundNumber*100))+round(int(computerWins/roundNumber*100))+round(int(tiedGames/roundNumber*100))))+"% Lost to rounding.")


def resetLost():
    global numOfLoses
    numOfLoses += 1


def reset():
    global currentScore
    global startBid
    global entryPrice
    global currentBid
    global GameOver
    global totalBid
    global availableNumbers
    global goodStartBid
    global currentDeck
    global computerScore
    global Time
    global computerDeck
    global Decided
    currentScore = 0
    computerScore = 0
    computerDeck = []
    startBid = 0
    totalBid = 0
    entryPrice = 0
    currentBid = 0
    Time = 0
    GameOver = False
    goodStartBid = False
    Decided = False
    availableNumbers = []
    currentDeck = []


def resetWon():
    global numOfWins
    numOfWins += 1


def calcScore(num):
    global currentScore
    if num == 1:
        currentScore += 1
    if num == 2:
        currentScore += 2
    if num == 3:
        currentScore += 3
    if num == 4:
        currentScore += 4
    if num == 5:
        currentScore += 5
    if num == 6:
        currentScore += 6
    if num == 7:
        currentScore += 7
    if num == 8:
        currentScore += 8
    if num == 9:
        currentScore += 9
    if num == 10:
        currentScore += 10
    if num == 11:
        currentScore += 10
    if num == 12:
        currentScore += 10
    if num == 13:
        currentScore += 10
    if num == 14:
        currentScore += 11


def calcScoreComputer(num):
    global computerScore
    if num == 1:
        computerScore += 1
    if num == 2:
        computerScore += 2
    if num == 3:
        computerScore += 3
    if num == 4:
        computerScore += 4
    if num == 5:
        computerScore += 5
    if num == 6:
        computerScore += 6
    if num == 7:
        computerScore += 7
    if num == 8:
        computerScore += 8
    if num == 9:
        computerScore += 9
    if num == 10:
        computerScore += 10
    if num == 11:
        computerScore += 10
    if num == 12:
        computerScore += 10
    if num == 13:
        computerScore += 10
    if num == 14:
        computerScore += 11


def calcEntryPrice(amount):
    global entryPrice

    if amount <= 50:
        entryPrice += 5
    if 50 < amount <= 100:
        entryPrice += 10
    if 100 < amount <= 500:
        entryPrice += 50
    if amount > 500:
        entryPrice += 100


def printScreen():
    subprocess.run("cls", shell=True)
    print("Current Balance: $" + str(currentBalance) + "      " +
          "Round Number: " + str(roundNumber) + "      " +
          "Player Ratio: " + str(round(int(numOfWins/roundNumber*100)))+ "%" + " : " + str(round(int(numOfLoses/roundNumber*100)))+ "%"  +" - " + str(round(int(tiedGames/roundNumber*100)))+ "%"  + "      " +
          "Computer Ratio: " + str(round(int(computerWins/roundNumber*100)))+ "%"  + " : " + str(round(int(computerLoses/roundNumber*100)))+ "%" + " - "+ str(round(int(tiedGames/roundNumber*100))) + "%" + "      " +
          "Current Bid: $" + str(currentBid) + " + $" + str(entryPrice) + " = $" + str(totalBid))

    print("\nCards:")
    for i in range(len(currentDeck)):
        cardDeck(currentDeck[i])

    print("\nCurrent Score: " + str(currentScore) + "\n")


def computer():
    global ComputerChance

    computerDeck.append(random.randint(1, 14))
    computerDeck.append(random.randint(1, 14))

    for i in range(len(computerDeck)):
        calcScoreComputer(computerDeck[i])

    while computerScore <= int(ComputerChance):
        if computerScore <= int(ComputerChance):
            computerDeck.append(random.randint(1, 14))
            calcScoreComputer(computerDeck[len(computerDeck) - 1])


def autoplay(betAmount):
    global numOfLoses, computerWins, currentBalance, numOfWins, computerLoses, roundNumber, decided, tiedGames
    decided = False
    reset()
    computer()

    currentDeck.append(random.randint(1, 14))
    currentDeck.append(random.randint(1, 14))

    for i in range(len(currentDeck)):
        calcScore(currentDeck[i])

    while currentScore <= int(PlayerChance):
        currentDeck.append(random.randint(1, 14))
        calcScore(currentDeck[len(currentDeck) - 1])

    if currentScore > 21 and not decided:
        numOfLoses += 1
        computerWins += 1
        currentBalance -= int(betAmount)
        roundNumber += 1
        decided = True
    elif computerScore > 21 and not decided:
        numOfWins += 1
        computerLoses += 1
        currentBalance += int(betAmount)
        roundNumber += 1
        decided = True
    elif currentScore > computerScore and not decided:
        numOfWins += 1
        computerLoses += 1
        currentBalance += int(betAmount)
        roundNumber += 1
        decided = True
    elif currentScore < computerScore and not decided:
        numOfLoses += 1
        computerWins += 1
        currentBalance -= int(betAmount)
        roundNumber += 1
        decided = True
    else:
        roundNumber += 1
        tiedGames += 1

def calcTime(seconds):
    operation_time = []

    total = seconds
    SecondsLeft = 0
    MinutesLeft = 0
    HoursLeft = 0
    DaysLeft = 0

    while total >=60:
        if total >= 60:
            total -= 60
            MinutesLeft +=1
        if MinutesLeft >= 60:
            MinutesLeft -= 60
            HoursLeft +=1
        if HoursLeft >= 24:
            HoursLeft -= 24
            DaysLeft +=1
    if total < 60:
        SecondsLeft += total

    operation_time.append(DaysLeft)
    operation_time.append(HoursLeft)
    operation_time.append(MinutesLeft)
    operation_time.append(SecondsLeft)

    return operation_time

def cardDeck(card):
    def one():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    1    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def two():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    2    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def three():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    3    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def four():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    4    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def five():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    5    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def six():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    6    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def seven():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    7    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def eight():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    8    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def nine():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    9    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def ten():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    10   |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def jack():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    J    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def queen():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    Q    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def king():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    K    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    def ace():
        print("|---------|")
        print("|         |")
        print("|         |")
        print("|    A    |")
        print("|         |")
        print("|         |")
        print("|---------|")

    if card == 1:
        one()
    if card == 2:
        two()
    if card == 3:
        three()
    if card == 4:
        four()
    if card == 5:
        five()
    if card == 6:
        six()
    if card == 7:
        seven()
    if card == 8:
        eight()
    if card == 9:
        nine()
    if card == 10:
        ten()
    if card == 11:
        jack()
    if card == 12:
        queen()
    if card == 13:
        king()
    if card == 14:
        ace()


start()