import turtle

turtle.speed(0)
turtle.Screen()
turtle.bgcolor("black")
turtle.pensize(4)
turtle.color("blue")

for x in range(10):
    for i in ["red","forestgreen","brown","blue","green","powder blue","cyan","cyan","pink"]:
        turtle.color(i)
        turtle.fd(300)
        turtle.lt(145)




turtle.hideturtle()
turtle.exitonclick()
