import turtle

turtle.Screen()
turtle.bgcolor("gray35")
turtle.title("Turtle Shape")


def draw_shape(sides, length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)


def set_pos(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
draw_shape(4,100)
set_pos(-600,0)

draw_shape(3,100)
set_pos(-400,0)

draw_shape(5,100)
set_pos(400,0)

draw_shape(8,100)
set_pos(0,0)

