import turtle
import random

tt = turtle.Turtle()
tt.color("red")
tt.pensize(5)
tt.speed(0   )


win = turtle.Screen()
win.bgcolor("gray")


for i in range(100):
    tt.fd(50)
    coin = random.randrange(2)
    if coin == 0:
        tt.lt(90)
    else:
        tt.rt(90)




turtle.mainloop()
