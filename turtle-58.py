import turtle

turtle.Screen()
turtle.bgcolor("black")
turtle.pensize(5)
turtle.color("white")

def hexagon():
  for _ in range(6):
      turtle.forward(100)
      turtle.left(60)

for _ in range (6):
    hexagon()
    turtle.forward(100)
    turtle.right(60)






turtle.done()
   

