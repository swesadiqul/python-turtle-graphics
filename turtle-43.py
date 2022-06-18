import turtle
from random import randint

win = turtle.Screen()
win.bgcolor("black")




game = turtle.Turtle()
game.color("yellow")
game.shape("turtle")
game.penup()
game.goto(-100,120)
game.pendown()

game1 = turtle.Turtle()
game1.color("blue")
game1.shape("turtle")
game1.penup()
game1.goto(-100,100)
game1.pendown()


game2 = turtle.Turtle()
game2.color("green")
game2.shape("turtle")
game2.penup()
game2.goto(-100,140)
game2.pendown()


game3= turtle.Turtle()
game3.color("orange")
game3.shape("turtle")
game3.penup()
game3.goto(-100,80)
game3.pendown()


game4 = turtle.Turtle()
game4.color("cyan")
game4.shape("turtle")
game4.penup()
game4.goto(-100,60)
game4.pendown()


for x in range(200):
    game.fd(randint(1,7))
    game1.fd(randint(1,6))
    game2.fd(randint(1,10))
    game3.fd(randint(1,9))
    game4.fd(randint(1,13))




turtle.done()

    








