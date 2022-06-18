import turtle

tt = turtle.Turtle()
tt.color("yellow")

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart Shape")
tt.fillcolor("red")
tt.begin_fill()
tt.left(140)
tt.forward(180)
tt.circle(-90,200)
# tt.left(120)
tt.setheading(60)
tt.circle(-90,200)
tt.forward(180)
tt.end_fill()
tt.up()
tt.home()

tt.up()
tt.pensize(4)
tt.pencolor("yellow")
tt.goto(-150,0)
tt.down()
tt.left(40)
tt.forward(500)






turtle.done()
