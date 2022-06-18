import turtle
import random

win = turtle.Screen()
win.bgcolor("black")
win.title("Turtle Beginner")
win.bgpic("Karima.gif")
win.clearscreen()
win.bgcolor("gray12")



jarry = turtle.Turtle()

jarry.shape("turtle")
jarry.color("yellow")

jarry.reset()
jarry.pencolor("lightblue")
jarry.speed(0)
jarry.penup()
jarry.setposition(0,0)
jarry.pendown()

jarry.fillcolor("green")
jarry.begin_fill()
for x in range(4):
    jarry.fd(100)
    jarry.lt(90)
jarry.end_fill()
jarry.hideturtle()

jarry.color("yellow")
jarry.up()
jarry.setpos(-200,-200)
jarry.shape("arrow")
jarry.showturtle()
jarry.down()
jarry.circle(50)


jarry.up()
jarry.home()
jarry.down()

for i in range(50):
    for j in ["yellow","red"]:
        x = random.randint(-600,600)
        y = random.randint(-400,400)
        jarry.color(j)
        jarry.up()
        jarry.setpos(x,y)
        jarry.down()
        jarry.dot(40)



turtle.done()
