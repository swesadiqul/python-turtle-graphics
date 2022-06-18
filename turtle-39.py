import turtle

tt = turtle.Turtle()
tt.shape("turtle")
tt.pensize(2)
tt.pencolor("yellow")
tt.speed(0)


win = turtle.Screen()
win.bgcolor("black")
win.title("Turtle Begineer.")


tt.fillcolor("green")
tt.begin_fill()

for x in range(4):
    tt.fd(100)
    tt.lt(90)
tt.end_fill()




tt.up()
tt.home()
tt.down()


tt.up()
tt.goto(0,-200)
tt.down()

tt.fillcolor("red")
tt.begin_fill()

for x in range(4):
    tt.fd(100)
    tt.lt(90)

tt.end_fill()


tt.up()
tt.home()
tt.down()


tt.up()
tt.goto(0,200)
tt.down()

tt.fillcolor("blue")
tt.begin_fill()

for x in range(4):
    tt.fd(100)
    tt.lt(90)


tt.end_fill()

tt.up()
tt.home()
tt.down()


tt.up()
tt.goto(200,0)
tt.down()

tt.fillcolor("yellow")
tt.begin_fill()


for x in range(4):
    tt.fd(100)
    tt.lt(90)

tt.end_fill()


tt.up()
tt.home()
tt.down()


tt.up()
tt.goto(-200,0)
tt.down()

tt.fillcolor("cyan")
tt.begin_fill()

for x in range(4):
    tt.fd(100)
    tt.lt(90)


tt.end_fill()






tt.hideturtle()

turtle.exitonclick()
