# TurtleTest.py
from turtle import*
import time

pen1 = Pen()
pen2 = Pen()


pen1.color("black","green")
pen2.color("red","yellow")

# Write Text on the Screen
pen1.up()
pen1.goto(0,100)
pen1.down()
pen1.write("Hello",False,'center',font=('Cooper black',18,'bold'))

# Pause for 2 seconds
time.sleep(2)
pen1.clear()


# Changing fonts
pen1.write("class",True,'left',font=('Cambria',22,'bold'))

# Drawing arcs
pen2.circle(-50,-90)
pen2.circle(50,-90)

# Adding background images(Your image must be GIF or PNG file.)
#you must save to the same folder as your python file.

# Change direction or heading
pen1.up()
pen1.home()
pen1.down()
pen1.setheading(0)
pen1.shapesize(4,4)
pen1.setheading(45)
pen1.setheading(-45)
pen1.right(89)




pen1.shape("circle")
pen1.shapesize(5,2,None)
pen1.shape("arrow")


