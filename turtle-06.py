import turtle

tip = turtle.Turtle()
tip.getscreen().bgcolor("#994444")
tip.speed(50)


# for i in range(5):
# tip.forward(10)
# tip.left(216)

tip.penup()
tip.goto((-200,100))
tip.pendown()

def star(turtle,size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        
        for i in range(5):
            tip.forward(size)
            star(turtle,size/3)
            turtle.left(216)
        turtle.end_fill()
            



star(tip,360)



turtle.done()
