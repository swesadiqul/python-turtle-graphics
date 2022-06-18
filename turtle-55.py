import turtle

turtle.Screen()
turtle.speed(0)

for i in range(400):
    for j in range(6):
        turtle.fd(i)
        turtle.lt(45+1)
    turtle.lt(33)

turtle.hideturtle()
