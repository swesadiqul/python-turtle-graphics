import turtle

t = turtle.Turtle()
t.color("Green","green")



t.begin_fill()
t.up()
t.goto(0,-100)
t.down()
t.forward(250)
t.left(90)
t.forward(300)
t.left(90)
t.forward(500)
t.left(90)
t.forward(300)
t.left(90)
t.forward(250)
t.end_fill()

t.color("red","red")
t.begin_fill()
t.up()
t.goto(0,0)
t.down()

t.circle(60)
t.end_fill()


t.hideturtle()














turtle.done()
