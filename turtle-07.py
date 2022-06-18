import turtle

tom =turtle.Turtle()
tom.color("black","red")
tom.speed(10)

tom.begin_fill()
for x in range(100):
    tom.forward(200)
    tom.right(145)

tom.end_fill()





turtle.done()
