import turtle
import random


tt = turtle.Turtle()
tt.color("cyan")
tt.shape("triangle")
tt.speed(0)


win = turtle.Screen()
win.bgcolor("black")
win.title("Turtle begineer")


for x in range(10):
    for y in ["red","green","blue","cyan","gray23","purple"]:
        tt.color(y)
        tt.circle(100)
        tt.lt(25)




tt.hideturtle()
turtle.exitonclick()
