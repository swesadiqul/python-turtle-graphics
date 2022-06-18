import turtle


tt = turtle.Turtle()
tt.shape("classic")
tt.color("red")
tt.speed(0)

win = turtle.Screen()
win.bgcolor("black")

def draw_square(side_length):
    for x in range(4):
        tt.fd(side_length)
        tt.lt(90)
def set_pos(x,y):
    tt.penup()
    tt.setpos(x,y)
    tt.down()

draw_square(50)
set_pos(-25,-25)

draw_square(100)
set_pos(-50,-50)

draw_square(150) # calling function
set_pos(-75,-75) # calling function

draw_square(200)
set_pos(-100,-100)

tt.hideturtle() #hide classic shape
turtle.done()
