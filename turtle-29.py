import turtle

turtle.speed(0)
turtle.bgcolor("black")

for i in range(5):
    for colours in ["red","purple","blue","cyan","green","yellow","white"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.lt(12)
        turtle.fd(200)
        turtle.lt(90)
        turtle.fd(200)
        turtle.lt(90)
        turtle.fd(200)
        turtle.lt(90)
        turtle.fd(200)
        turtle.lt(90)
turtle.done()
