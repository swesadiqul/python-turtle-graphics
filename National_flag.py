import turtle

tt = turtle.Turtle()

win = turtle.Screen()
win.bgcolor("black")

tt.up()
tt.width(4)
tt.color("forestgreen")
tt.goto(0,-300)
tt.down()



tt.fillcolor("green")
tt.begin_fill()
tt.goto(0,300)
tt.forward(400)
tt.right(90)
tt.forward(300)
tt.right(90)
tt.forward(400)
tt.home()
tt.end_fill()


tt.color("red","red")
tt.begin_fill()
tt.up()
tt.goto(200,50)
tt.down()
tt.circle(100)
tt.end_fill()


tt.color("brown")
tt.begin_fill()
tt.up()
tt.goto(0,-300)
tt.down()
tt.circle(50,steps=3)
tt.end_fill()


tt.hideturtle()
























turtle.done()
