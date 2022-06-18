import turtle

turtle.Screen()
turtle.bgcolor("black")
turtle.pensize(5)
turtle.color("white")
turtle.speed(0)

def draw_square(side_height):
    for i in range(4):
        turtle.fd(side_height)
        turtle.lt(90)
def set_pos(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


# 1st part
draw_square(50)
set_pos(125,125)

draw_square(50)
set_pos(100,100)

draw_square(50)
set_pos(75,75)

draw_square(50)
set_pos(50,50)

draw_square(50)
set_pos(25,25)


# 2nd part
draw_square(50)
set_pos(-25,-25)

draw_square(50)
set_pos(-50,-50)

draw_square(50)
set_pos(-75,-75)

draw_square(50)
set_pos(-100,-100)

draw_square(50)
set_pos(-125,-125)



# 3rd part
draw_square(50)
set_pos(-125,125)

draw_square(50)
set_pos(-100,100)

draw_square(50)
set_pos(-75,75)

draw_square(50)
set_pos(-50,50)

draw_square(50)
set_pos(-25,25)


# 4th part
draw_square(50)
set_pos(25,-25)

draw_square(50)
set_pos(50,-50)

draw_square(50)
set_pos(75,-75)

draw_square(50)
set_pos(100,-100)

draw_square(50)
set_pos(125,-125)

draw_square(50)
set_pos(150,-150)




turtle.hideturtle()

