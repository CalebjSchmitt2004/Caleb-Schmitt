import random
import os


def run():
    os.system("cls")
    print("If you would like a list of options just type (list_options)")
    start = input("What bridge do you need more help with?: ")

    if start == "list_options":
        print("north, south, both")

    if start == "north":
        for i in range(16):
            north()

    if start == "south":
        for i in range(16):
            south()

    if start == "both":
        for i in range(8):
            north()
            south()


def north():
    key = [["What chip is located at the north end of the board?", "north"], ["What chip is bigger?", "north"],
           ["What chip communicates faster?", "north"], ["What chip is connected directly to the CPU?", "north"],
           ["What chip communicates using FSB?", "north"], ["Which chip controls adapter cards?", "north"],
           ["Which chip is the hub for memory control?", "north"]]
    questions = random.sample(key, len(key))

    q = 0
    a = 0

    while q <= len(questions):
        while a <= len(questions):
            question = questions[q][0]
            print("\n" + question)
            answer = input("")

            if answer == questions[a][1]:
                print("Good job")
            else:
                print("Oops Sorry")
                print("\n Corrects Answer: ")
                print(questions[a][1])

            q += 1
            a += 1


def south():
    key = [["What chip is located at the south end of the board?", "south"], ["What chip is the hub for USB?", "south"],
           ["Which chip manages power?", "south"], ["Which chip has plug and play support?", "south"],
           ["What chip controls IDE and ATA Interfaces?", "south"], ["What chip is smaller?", "south"],
           ["Which chip handles I/O support?", "south"]]
    questions = random.sample(key, len(key))

    q = 0
    a = 0

    while q <= len(questions):
        while a <= len(questions):
            question = questions[q][0]
            print("\n" + question)
            answer = input("")

            if answer == questions[a][1]:
                print("Good job")
            else:
                print("Oops Sorry")
                print("\n Corrects Answer: ")
                print(questions[a][1])

            q += 1
            a += 1


run()
