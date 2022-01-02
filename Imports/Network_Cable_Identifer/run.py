def run():
    print("Please input all of you answers in lower case and separate all multi answer questions with a comma no space")
    print("If you are confused or need help type list_options")
    answer = input("What cable would you like to practice on?: ")

    if answer == "list_options":
        options = ["strait, cross-over, roll-over"]
        print(options)

    if answer == "strait":
        strait()

    if answer == "cross-over":
        cross_over()

    if answer == "roll_over":
        roll_over()


def strait():
    side_one = ["white-orange", "orange", "white-green", "blue", "white-blue", "green", "white-brown", "brown"]
    side_two = ["white-orange", "orange", "white-green", "blue", "white-blue", "green", "white-brown", "brown"]

    points = 0

    index = 1
    side = 1

    side_one_color_list = []
    side_two_color_list = []

    while index <= 16:
        answer = input("What is the color of side " + str(side) + " pin " + str(index))
        side_one_color_list.append(answer)
        if index <= 8:
            side_one_color_list.append(answer)
        if index == 8:
            print("\n")
            side += 1
        if index > 16 & index <= 16:
            side_two_color_list.append(answer)

    i = 0

    while i <= 7:
        if side_one_color_list[i] == side_one[i]:
            points += 1
        else:
            print(side_one[i])
        if side_two_color_list[i] == side_two[i]:
            points += 1
        else:
            print(side_two[i])

    print("You got " + str(16 - points) + " wrong")
    print("Your finally score is " + str(points) + "/20")


def cross_over():
    side_one = ["white-orange", "orange", "white-green", "blue", "white-blue", "green", "white-brown", "brown"]
    side_two = ["white-green", "green", "white-orange", "blue", "white-blue", "orange", "white-brown", "brown"]

    points = 0

    index = 1
    side = 1

    side_one_color_list = []
    side_two_color_list = []

    while index <= 16:
        answer = input("What is the color of side " + str(side) + " pin " + str(index))
        side_one_color_list.append(answer)
        if index <= 8:
            side_one_color_list.append(answer)
        if index == 8:
            print("\n")
            side += 1
        if index > 16 & index <= 16:
            side_two_color_list.append(answer)

    i = 0

    while i <= 7:
        if side_one_color_list[i] == side_one[i]:
            points += 1
        else:
            print(side_one[i])
        if side_two_color_list[i] == side_two[i]:
            points += 1
        else:
            print(side_two[i])

    print("You got " + str(16 - points) + " wrong")
    print("Your finally score is " + str(points) + "/20")


def roll_over():
    side_one = ["white-orange", "orange", "white-green", "blue", "white-blue", "green", "white-brown", "brown"]
    side_two = ["brown", "white-brown", "green", "white-blue", "blue", "white-green", "orange", "white-orange"]

    points = 0

    index = 1
    side = 1

    side_one_color_list = []
    side_two_color_list = []

    while index <= 16:
        answer = input("What is the color of side " + str(side) + " pin " + str(index))
        side_one_color_list.append(answer)
        if index <= 8:
            side_one_color_list.append(answer)
        if index == 8:
            print("\n")
            side += 1
        if index > 16 & index <= 16:
            side_two_color_list.append(answer)

    i = 0

    while i <= 7:
        if side_one_color_list[i] == side_one[i]:
            points += 1
        else:
            print(side_one[i])
        if side_two_color_list[i] == side_two[i]:
            points += 1
        else:
            print(side_two[i])

    print("You got " + str(16 - points) + " wrong")
    print("Your finally score is " + str(points) + "/20")
