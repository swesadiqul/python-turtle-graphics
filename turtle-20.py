import turtle


tt = turtle.Turtle() # take the turtle window
tt.shape("classic") # Change the shape name
tt.speed(3) # shape speed

win = turtle.Screen() # take the new screen
win.bgcolor("black") # change the new screen bgcolor
win.title("Turtle Graphics Beginner") # change the title of new screen

tt.color("red","red")
tt.begin_fill()
tt.up()
tt.goto(0,0)
tt.down()
tt.circle(100)
tt.end_fill()


tt.color("green","green")
tt.begin_fill()
tt.up()
tt.goto(100,100)
tt.down()
tt.circle(100)
tt.end_fill()

tt.color("orange","orange")
tt.begin_fill()
tt.up()
tt.goto(-100,100)
tt.down()
tt.circle(100)
tt.end_fill()

tt.color("brown","brown")
tt.begin_fill()
tt.up()
tt.goto(100,-100)
tt.down()
tt.circle(100)
tt.end_fill()

tt.color("blue","blue")
tt.begin_fill()
tt.up()
tt.goto(-100,-100)
tt.down()
tt.circle(100)
tt.end_fill()













tt.hideturtle() # hide the shape
turtle.done()
