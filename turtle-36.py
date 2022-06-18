import turtle

demo = turtle.Turtle()
demo.color("blue","powder blue")
demo.speed(0) # turtle shape speed
demo.shape("classic") # "classic" is a turtle shape name


pip = turtle.Screen() # show the new screen
pip.bgcolor("black") # show the new screen background color
pip.title("Turtle Graphics Beginner") # Change the new screen title name


demo.fillcolor("orange")
demo.begin_fill() # begin_fill and end_fill  by the two function is a field color

win = 0
while win<50:
    for x in ["green","red","yellow","blue","orange"]:
        demo.color(x)
        demo.forward(150)
        demo.left(45)
        demo.forward(100)
        demo.left(90)
        demo.bk(25)
        win +=1
       



demo.hideturtle() # hide the shape of screen

turtle.done()
