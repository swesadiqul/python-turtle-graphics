import turtle

jerry = turtle.Turtle()
jerry.pensize(4)
jerry.color("orange")
jerry.speed(0)


tom = turtle.Screen()
tom.bgcolor("black")



for x in range(5):
    for i in ["red","green","blue","orange","purple"] :
        
        jerry.color(i)
        jerry.fd(100)
        jerry.lt(45)
        jerry.fd(100)
        jerry.lt(90)
        jerry.fd(100)
        jerry.lt(90)
        jerry.fd(100)
        jerry.lt(90)
        jerry.fd(100)
        jerry.lt(90)
        jerry.fd(100)
        jerry.lt(90)

        jerry.fd(100)
        jerry.lt(90)
        jerry.fd(100)
        jerry.lt(90)

















jerry.hideturtle()


turtle.exitonclick()
