import turtle

turtle.Screen()
turtle.bgcolor("black")
turtle.speed(0)

for i in range(100):
    for x in ["navy","mediumpurple","blue","lightgreen","yellow"]:
        turtle.color(x)
        turtle.fd(i*2)
        turtle.fd(5)
        turtle.lt(51)
        
        

turtle.hideturtle()
