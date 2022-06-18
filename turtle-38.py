import turtle
turtle.Screen()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.pencolor("yellow")
turtle.speed(0)
colors = ["red","blue","cyan","brown","green","yellow","powder blue","orange"]

for i in range(10):
    turtle.color(colors)
    turtle.circle(100)
    turtle.lt(10)
