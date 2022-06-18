import turtle

ima = turtle.Turtle()
ima.pencolor("Green")
ima.pensize(2)
ima.speed(0)



win = turtle.Screen()
win.bgcolor("black")


ima.fillcolor("yellow")
ima.begin_fill()

for x in range(4):
    ima.forward(100)
    ima.left(90)

ima.end_fill()

ima.penup()
ima.forward(150)
ima.pendown()


ima.fillcolor("cyan")
ima.begin_fill()
for y in range(4):
    ima.forward(100)
    ima.left(90)

ima.end_fill()

ima.up()
ima.bk(300)
ima.down()

ima.fillcolor("cyan")
ima.begin_fill()
for y in range(4):
    ima.forward(100)
    ima.left(90)

ima.end_fill()


ima.up()
ima.fd(100)
ima.down()

ima.fillcolor("red")
ima.begin_fill()
for y in range(2):
    ima.forward(50)
    ima.left(90)
    ima.fd(100)
    ima.lt(90)

ima.end_fill()



ima.up()
ima.fd(150)
ima.down()

ima.fillcolor("red")
ima.begin_fill()
for y in range(2):
    ima.forward(50)
    ima.left(90)
    ima.fd(100)
    ima.lt(90)

ima.end_fill()



ima.hideturtle()
turtle.done()
