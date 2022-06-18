import turtle

turtle.Screen()
turtle.bgcolor("black")
turtle.speed(10)
turtle.color("white")

for x in range(10):
    turtle.fd(25)
    turtle.up()
    turtle.fd(10)
    turtle.down()


turtle.done()
