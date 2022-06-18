import turtle

win = turtle.Screen()
win.bgcolor("black")
win.tracer(8,25)



tt = turtle.Turtle()
tt.shape("classic")
tt.resizemode("auto")
tt.color("blue")


jarry = 2
for i in range(200):
    tt.fd(jarry)
    tt.lt(90)
    jarry += 3
    
turtle.done()


