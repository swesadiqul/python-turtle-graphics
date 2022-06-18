import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Semi circle")

tom = turtle.Turtle()
tom.shape("circle")
tom.color("yellow")
tom.begin_fill()
tom.right(90)
tom.circle(50,180)
tom.end_fill()

tom.hideturtle()
