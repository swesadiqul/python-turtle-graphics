import turtle

tt = turtle.Turtle()
win = turtle.Screen()
win.bgcolor("black")
win.title("Turtle Graphics Begineer")


tt.pensize(8)
tt.color("forestgreen")
tt.speed(0)




tt.color("forestgreen","green")
tt.begin_fill()
tt.left(90)
tt.backward(300)
tt.forward(600)
for x in range(2):
    tt.right(90)
    tt.forward(400)
    tt.right(90)
    tt.forward(200)
tt.home()
tt.end_fill()
tt.color("red","red")
tt.begin_fill()
tt.up()
tt.setpos(200,125)
tt.down()
tt.circle(75)
tt.end_fill()

tt.up()
tt.color("green")
tt.home()
tt.down()

tt.color("brown")
tt.begin_fill()
tt.up()
tt.setpos(0,-350)
tt.down()
tt.circle(50,steps=3)
tt.end_fill()


# part of star
tt.up()
tt.setposition(-300,250)
tt.down()


tt.color("white","white")
tt.begin_fill()
tt.pensize(2)
for x in range(5):
    tt.forward(50)
    tt.left(145)
tt.end_fill()
   

tt.up()
tt.setpos(-400,300)
tt.down()

tt.color("white","white")
tt.begin_fill()
for x in range(5):
    tt.forward(50)
    tt.left(145)
tt.end_fill()   


tt.up() #control the pen and up it
tt.setpos(-500,150)
tt.down() #control the pen and up it

tt.color("white","white")
tt.begin_fill()
for x in range(5):
    tt.forward(50) #distance
    tt.left(145) #angle
tt.end_fill()   


tt.up()
tt.setpos(-600,300)
tt.down()

tt.color("white","white") # pencolor and fillcolor
tt.begin_fill()
for x in range(5):
    tt.forward(100)
    tt.left(145)
tt.end_fill()









tt.hideturtle() # hide turtle

turtle.exitonclick() # exit on click
