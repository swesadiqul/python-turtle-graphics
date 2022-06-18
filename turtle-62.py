import turtle
import random

tt = turtle.Turtle()
tt.color("yellow")
tt.shape("turtle")
tt.width(5)
tt.speed(0)

win = turtle.Screen()
win.bgcolor("black")
win.title("Turtle Beginner.")

for i in range(5):
    for p in ["yellow","blue","green","red","cyan","purple","lightblue"]:
        tt.color(p)
        x=random.randint(-300,300)
        y=random.randint(-300,300)
        tt.penup()
        tt.setpos(x,y)
        tt.pendown()
        for j in range(4):
            tt.fd(50) # change the system and see ..
            tt.lt(90)



tt.hideturtle()
turtle.done()
