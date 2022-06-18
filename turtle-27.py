import turtle


tt = turtle.Turtle()

colors = ["orange","red","green","blue","brown","purple"]

tt.width(6)
tt.speed(6)
tt.up()
tt.goto(300,0)
tt.down()
for x in range(6):
    tt.color(colors[x])
    tt.circle(100)
    tt.up()
    tt.bk(50)
    tt.down()
   

















tt.hideturtle()

turtle.done()
