import turtle

tom=turtle.Turtle()
tom.color("Orange")
tom.speed(0)


tom.begin_fill()

for x in range(50):
    tom.forward(200)
    tom.left(220)
    
tom.end_fill()





tom.hideturtle()
turtle.done()
