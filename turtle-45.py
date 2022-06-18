import turtle

tt = turtle.Turtle()
tt.shape("turtle")
tt.pencolor("red")
tt.pensize(4)
tt.speed(0)


win = turtle.Screen()
win.bgcolor("cyan")
win.title("Turtle Begineer")


tt.penup()
tt.goto(-100,0)
tt.pendown()


tt.fillcolor("black")
tt.begin_fill()
for x in range(100):
    tt.fd(200)
    tt.lt(91)
    tt.circle(100,steps=3)
    tt.lt(91)
tt.end_fill()



tt.hideturtle()
turtle.done()
