def draw_circle(x,y,color,rad):
    tt.goto(x,y)
    tt.down()
    tt.begin_fill()
    tt.fillcolor(color)
    tt.circle(rad)
    tt.end_fill()
    tt.up()
    tt.home()

import turtle
tt = turtle.Turtle()
tt.up()
draw_circle(0,-50,"green",50)
draw_circle(0,300,"green",25)
draw_circle(200,200,"orange",50)
draw_circle(0,-300,"orange",25)
draw_circle(-200,200,"blue",50)
draw_circle(300,0,"blue",25)
draw_circle(-200,-200,"red",-50)
draw_circle(-300,0,"red",25)
draw_circle(200,-200,"yellow",-50)




tt.hideturtle()
turtle.done()
