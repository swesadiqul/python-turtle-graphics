import turtle
from random import randint

turtle.Screen() # open a new window
turtle.bgcolor("black") # change the background color of screen
turtle.speed(0) # how quickly the star is down
turtle.pencolor("yellow") # choose a color for the pen


# the code to draw a single star
def draw_star():
    turns = 5
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    while turns>0:
        turtle.fd(25)
        turtle.lt(145)
        turns -=1
    turtle.end_fill()

# code to draw 50 stars
num_star = 0
while num_star<50:
    x = randint(-500,500)
    y = randint(-500,500)
    draw_star()
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    num_star = num_star + 1


draw_star()

turtle.hideturtle()
turtle.exitonclick() # close the window when clicked
