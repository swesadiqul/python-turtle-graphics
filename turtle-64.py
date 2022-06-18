import turtle


tt = turtle.Turtle()
tt.lt(90)
tt.speed(10)
tt.color("green")

#recursion
def draw(sight_length):
    if (sight_length<10):
        return
    else:
        tt.fd(sight_length)
        tt.lt(30)
        draw(3*sight_length/4)
        tt.rt(60)
        draw(3*sight_length/4)
        tt.lt(30)
        tt.bk(sight_length)
draw(100)


turtle.done()











