import turtle


tt = turtle.Turtle()
tt.shape("turtle")
tt.speed(0)

jarry = turtle.Turtle()
jarry.shape("turtle")
jarry.speed(0)

win = turtle.Screen()
win.bgcolor("lightblue")

# 1st part

tt.penup()
tt.goto(0,-50)
tt.down()

tt.circle(100)


#2nd part

jarry.penup()
jarry.goto(0,-100)
jarry.down()

jarry.circle(150)

# 3rd part

tt.penup()
tt.goto(0,-25)
tt.down()

tt.circle(75)


# 4th part

jarry.penup()
jarry.goto(0,-150)
jarry.down()
jarry.pencolor("green")
jarry.fillcolor("green")
jarry.begin_fill()
jarry.circle(200)
jarry.end_fill()


# 5th part

tt.penup()
tt.goto(0,-75)
tt.down()
tt.pencolor("gray45")
tt.fillcolor("gray45")
tt.begin_fill()
tt.circle(125)
tt.end_fill()

# 6th part

jarry.penup()
jarry.goto(0,-125)
jarry.down()

jarry.circle(175)



# 7th part
tt.pencolor("red")
tt.fillcolor("red")
tt.begin_fill()
tt.penup()
tt.goto(0,10)
tt.down()
tt.circle(40)
tt.end_fill()



tt.hideturtle()
jarry.hideturtle()
turtle.exitonclick()
