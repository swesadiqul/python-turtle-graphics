import turtle
import math

rap = turtle.Turtle()
rap.color("red","yellow")
rap.speed(10)

rap.begin_fill()
for x in range(100):
    rap.forward(math.sqrt(x)*10)
    rap.left(x%90)
rap.end_fill()
   


turtle.done()
