import turtle

tt = turtle.Turtle()
tt.color("red")
tt.shape("triangle")
tt.pensize(3)
tt.speed(0)


win = turtle.Screen()
win.bgcolor("lightblue")
win.title("Turtle begineer")



for x in range(50):
    for y in ["green","black","red"]:
        tt.color(y)
        tt.fd(x)
        tt.circle(100,steps=3)
        
        tt.lt(120)






tt.hideturtle()
turtle.exitonclick()


