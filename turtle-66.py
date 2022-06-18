import turtle

# Window control
win = turtle.Screen()
win.bgcolor("white")
win.title(" Turtle Beginner")
win.bgpic("Karima.gif")
win.clear() # or clearscreen()
#win.resetscreen()/ reset()
#win.screensize(canvwidth=400,canvheight=300)
#win.setworldcoordinates(-50,-7.5,50,7.5)

#for i in range(8):
    #win.lt(45)
    #win.fd(2)

# Turtle motion (move and draw)

jarry = turtle.Turtle()
for x in range(4):
    jarry.rt(90)
    jarry.bk(100)

jarry.up()
jarry.goto(-200,100)
jarry.down()
jarry.seth(360)
jarry.fd(100)
jarry.seth(90)
jarry.fd(100)
jarry.seth(180)
jarry.fd(100)
jarry.seth(270)
jarry.fd(100)

jarry.up()
jarry.setx(300)
jarry.sety(300)
jarry.down()
for  i in range(4):
    jarry.fd(100)
    jarry.lt(90)

jarry.up()
jarry.setpos(300,0)
jarry.down()
jarry.color("lightgreen")
for j in range(4):
    jarry.stamp()
    jarry.fd(100)
    jarry.lt(90)


jarry.clearstamps(100)




















turtle.done()


