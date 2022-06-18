import turtle  # input turtle module

tt = turtle.Turtle() # turtle object
tt.shape("circle") # shape formate
tt.pensize(4)
tt.pencolor("green")
tt.speed(10)


win = turtle.Screen() # opne a new window
win.bgcolor("black") # change the bgcolor 

tt.penup()
tt.setpos(300,0)
tt.pendown()
# first etep
first_color = 0
while first_color<5:
    for i in ["red","green","blue","cyan","Purple","white"]:
        tt.color(i)
    
        tt.circle(100,steps=8)
        tt.up()
        tt.bk(100)
        tt.down()
        first_color += 1

tt.penup()
tt.home()
tt.down()


tt.penup()
tt.setpos(100,-100)
tt.pendown()

# second step

second_color = 1
while second_color<2:
   for x in ["orange","brown"]:
        tt.color(x)
        tt.circle(100,steps=8)
        tt.up()
        tt.bk(100)
        tt.down()
        second_color += 1

tt.color("yellow")
tt.penup()
tt.setposition(50,-200)
tt.pendown()
tt.circle(100,steps=8)


tt.hideturtle() # hide the turtle
turtle.done()






















turtle.done()
