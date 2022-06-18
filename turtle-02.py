import turtle


win = turtle.Screen()
win.bgcolor("black")

ram = turtle.Turtle()
ram.speed(5)
ram.color("yellow")
ram.shape("triangle")


ram.begin_fill()

for x in range(5):
    ram.forward(100)
    ram.left(144)
ram.end_fill()





ram.hideturtle()
turtle.done()
