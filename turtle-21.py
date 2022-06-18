import turtle

tk = turtle.Turtle()
list1 = ["yellow","red","blue","green"]
tk.speed(6)
tk.up()
tk.goto(200,0)
for x in range(4):
    tk.down()
    tk.color(list1[x])
    tk.pensize(20)
    tk.circle(100)
    tk.up()
    tk.bk(100)
tk.up()
tk.goto(0,-100)
tk.left(90)
tk.forward(200)
for x in range(4):
    tk.down()
    tk.color(list1[x])
    tk.pensize(20)
    tk.circle(100)
    tk.up()
    tk.bk(100)


tk.up()
tk.goto(200,0)
for x in range(3):
    tk.down()
    tk.color(list1[x])
    tk.pensize(20)
    tk.circle(100)
    tk.up()
    tk.bk(100)


tk.up()
tk.goto(0,-100)
tk.left(90)
tk.forward(200)
for x in range(4):
    tk.down()
    tk.color(list1[x])
    tk.pensize(20)
    tk.circle(100)
    tk.up()
    tk.bk(100)


tk.hideturtle()
turtle.done()
