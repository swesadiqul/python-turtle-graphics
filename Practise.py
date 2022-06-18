import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)




player = turtle.Turtle()

player.penup()
player.setposition(-100,-100)
player.pendown()

player.shape("circle")
player.color("yellow")--
player.fillcolor("green")
player.speed(0)

player.begin_fill()
for x in range(4):
    player.forward(200)
    player.left(90)

player.end_fill()


player.hideturtle()














