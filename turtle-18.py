import turtle

turtle.Screen() # Show the new screen
turtle.bgcolor("black") # And change the new screen bgcolor
turtle.color("orange","forestgreen") # First color is a turtle color and the second color is field color



for x in range(4):
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
   
    turtle.end_fill()









turtle.exitonclick() # Anywhere click on the page then exit on the program
