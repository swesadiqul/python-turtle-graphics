import turtle

tt = turtle.Turtle()
tt.shape("turtle")
tt.pencolor("powder blue")
tt.pensize(2)
tt.speed(0)

win = turtle.Screen()
win.bgcolor("black")
win.title("Turtle Begineer")


for x in range(500):
    tt.fd(x)
    tt.lt(91)






tt.hideturtle()
turtle.done()
