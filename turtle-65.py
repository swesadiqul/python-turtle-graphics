import turtle

tt = turtle.Turtle()
tt.penup()
tt.setpos(0,-100)
tt.pendown()

tt.fillcolor("yellow")
tt.begin_fill()
tt.circle(100)
tt.end_fill()


tt.penup()
tt.setpos(-68,-40)
tt.pensize(5)
tt.seth(-60)
tt.down()
tt.circle(80,120)
tt.fillcolor("black")


def draw_circle(x,y):
    tt.penup()
    tt.setpos(x,y)
    tt.pendown()
    tt.fillcolor("black")
    tt.begin_fill()
    tt.circle(10)
    tt.end_fill()

draw_circle(-40,40)
draw_circle(50,40)


tt.hideturtle()
turtle.done















turtle.done()
