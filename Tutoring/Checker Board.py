
speed(0)
sq_length = 40

def makeRow(row):
    for i in range(10):
        pendown()
        begin_fill()
        if i%2 == 0 and row % 2 == 0:
            color_value = "red"
        elif i%2 == 1 and row %2 == 0:
            color_value = "black"
        elif i%2 == 0 and row %2 == 1:
            color_value = "black"
        elif i%2 == 1 and row %2 == 1:
            color_value = "red"
        color(color_value)
        makeSquare()
        end_fill()
        penup()
        forward(40)
    moveUp()
   

def makeSquare():
    for i in range(4):
        forward(40)
        left(90)

def moveUp():
    left(90)
    forward(40)
    right(90)
    backward(400)
   
   
penup()
setposition(-200,-200)

for i in range(10):
    makeRow(i)
