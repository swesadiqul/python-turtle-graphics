import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("forestgreen","orange")
tim.speed(10)

win = turtle.Screen()
win.bgcolor("white")
win.bgpic("karima.gif")

tim.color("black")
tim.begin_fill()
for x in range(5):
    tim.forward(400)
    tim.left(145)
tim.end_fill()


tim.penup()
tim.backward(300)
tim.pendown()

tim.color("orange")
tim.begin_fill()
for x in range(100):
    tim.forward(300)
    tim.left(145)
tim.end_fill()



turtle.done()
