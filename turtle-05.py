import turtle
import math

demo=turtle.Turtle()
demo.color("red","yellow")
demo.speed(100)

demo.begin_fill()

for i in range(2000):
    demo.forward(10)
    demo.left(math.sin(i/10)*25)
    demo.left(20)
    
demo.end_fill()














turtle.done()
