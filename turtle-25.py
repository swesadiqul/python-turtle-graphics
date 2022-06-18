import turtle

def rectangle(color):
    jim.begin_fill()
    jim.fillcolor(color)
    for x in range(2):
        jim.forward(400)
        jim.right(90)
        jim.forward(100)
        jim.right(90)
    jim.end_fill()
        
   

jim = turtle.Turtle()
jim.up()
jim.pensize(4)
jim.goto(0,-300)
jim.down()
jim.goto(0,300)
rectangle("#FF9933")


jim.goto(0,200)
jim.forward(200)
jim.color("#000088")
jim.circle(-50)
jim.setheading(270)
jim.forward(50)
jim.setheading(0)
for x in range(24):
    jim.forward(45)
    jim.bk(45)
    jim.left(15)
jim.setheading(90)
jim.forward(50)
jim.setheading(0)



jim.color("black")
jim.forward(200)
jim.right(90)
jim.forward(100)
jim.right(90)
jim.forward(400)
jim.right(90)
jim.forward(100)
jim.right(90)

jim.goto(0,100)
rectangle("#128807")
