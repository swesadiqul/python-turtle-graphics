import turtle

jerry = turtle.Turtle()


jerry.up()
jerry.goto(0,-50)
jerry.down()
jerry.begin_fill()
jerry.fillcolor("green")
jerry.circle(50)
jerry.end_fill()
jerry.up()
jerry.home()

jerry.goto(200,200)
jerry.down()
jerry.begin_fill()
jerry.fillcolor("brown")
jerry.circle(50)
jerry.end_fill()
jerry.up()
jerry.home()

jerry.goto(-200,200)
jerry.down()
jerry.begin_fill()
jerry.fillcolor("blue")
jerry.circle(50)
jerry.end_fill()
jerry.up()
jerry.home()

jerry.goto(-200,-200)
jerry.down()
jerry.begin_fill()
jerry.fillcolor("red")
jerry.circle(-50)
jerry.end_fill()
jerry.up()
jerry.home()

jerry.goto(200,-200)
jerry.down()
jerry.begin_fill()
jerry.fillcolor("yellow")
jerry.circle(-50)
jerry.end_fill()
jerry.up()
jerry.home()












jerry.hideturtle()



turtle.done()
