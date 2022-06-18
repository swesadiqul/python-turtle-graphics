import turtle




tt = turtle.Turtle()
list1 = ["purple","red","orange","blue","green"]


rap = turtle.Screen()
rap.bgcolor("black")

tt.speed(6)

for i in range(200):
    tt.color(list1[i%5])
    tt.pensize(i/15+2)
    tt.forward(i)
    tt.left(59)












turtle.done()
