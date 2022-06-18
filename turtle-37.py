import turtle

turtle.Screen()
turtle.bgcolor("black")
turtle.title("Turtle Graphics Begineer.")
turtle.shape("classic")
turtle.pensize(2)
turtle.pencolor("yellow")
turtle.speed(0)
turtle.up()
turtle.goto(-450,0)
turtle.down()

for x in range(10):
    for y in ["forestgreen","yellow","black","cyan","red","blue","purple","brown","powder blue"]:
        turtle.color(y)
        turtle.circle(100,steps=5)
        turtle.lt(5)


turtle.up()
turtle.home()
turtle.down()

for x in range(10):
    for y in ["forestgreen","yellow","black","cyan","red","blue","purple","brown","powder blue"]:
        turtle.color(y)
        turtle.circle(100,steps=8)
        turtle.lt(5)


turtle.up()
turtle.goto(450,0)
turtle.down()

for x in range(10):
    for y in ["forestgreen","yellow","black","cyan","red","blue","purple","brown","powder blue"]:
        turtle.color(y)
        turtle.circle(100,steps=3)
        turtle.lt(5)

















turtle.done()
