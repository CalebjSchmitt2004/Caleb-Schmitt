from GUI_API import API
import time

def Command(command):
    if command == "login":
        login()
    if command == "next":
        next()

def next():
    API.next()

def login():
    username = API.getEntry()
    password = API.getPass()

    info = [str(username) + " : " + str(password)]
    result = checkUser(info)

    API.loginMessage(result, username)


def checkUser(login):
    users = open("E:\Tkinter Projects\GUI MapleTronics (Light)\Build-1\GUI_API\System_Attibutes\\Users.txt", 'r')
    UserList = users.readlines()

    print(login)
    print(UserList)

    for users in UserList:
        print(users)
        if users == login:
            return True
        else:
            return False

