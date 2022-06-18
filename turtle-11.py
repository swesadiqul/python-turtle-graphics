import turtle

amul = turtle.Turtle()
amul.shape("triangle")
amul.color("Orange","black")


def circle_1():
    amul.begin_fill()
    amul.circle(100)
    amul.end_fill()
circle_1()


amul.color("Blue","red")
amul.begin_fill()
amul.penup()
amul.forward(150)
amul.pendown()
circle_1()
amul.end_fill()

amul.color("Green","forestgreen")
amul.begin_fill()
amul.penup()
amul.left(130)
amul.pendown()
circle_1()
amul.end_fill()

