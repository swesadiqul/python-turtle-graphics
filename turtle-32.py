import turtle
turtle.speed(0)
turtle.bgcolor("black")

turtle.pencolor("blue")

turtle.up()
turtle.setposition(0,-150)
turtle.down()

for x in range(100):
    for i in ["orange","red","blue","green","white","cyan","yellow","purple","powder blue"]:
        turtle.color(i)
        turtle.lt(12)
        turtle.fd(100)
        turtle.lt(45)
        turtle.fd(100)
        turtle.lt(45)
        turtle.fd(100)
        turtle.lt(45)
        turtle.fd(100)






turtle.hideturtle()
turtle.done()
