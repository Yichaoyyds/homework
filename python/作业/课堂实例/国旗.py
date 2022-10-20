import turtle as t
t.penup()
t.goto(-200,110)
t.pendown()
t.color("black","red")
t.begin_fill()
t.fd(400)
t.right(90)
t.fd(220)
t.right(90)
t.fd(400)
t.right(90)
t.fd(220)
t.right(90)
t.end_fill()


t.penup()
t.goto(-180,60)
t.pendown()
t.color("yellow","yellow")
t.begin_fill()
for i in range(5):
    t.fd(30)
    t.left(72)
    t.fd(30)
    t.right(144)
t.end_fill()

t.penup()
t.goto(-65,33)#3
t.pendown()
t.begin_fill()
for i in range(5):
    t.fd(10)
    t.left(72)
    t.fd(10)
    t.right(144)
t.end_fill()

t.penup()
t.goto(-65,65)#2
t.pendown()
t.begin_fill()
t.left(15)
for i in range(5):
    t.fd(10)
    t.left(72)
    t.fd(10)
    t.right(144)
t.end_fill()

t.penup()
t.goto(-85,98)#1
t.pendown()
t.right(30)
t.begin_fill()
for i in range(5):
    t.fd(10)
    t.left(72)
    t.fd(10)
    t.right(144)
t.end_fill()


t.penup()
t.goto(-85,10)#4
t.pendown()
t.begin_fill()
for i in range(5):
    t.fd(10)
    t.left(72)
    t.fd(10)
    t.right(144)
t.end_fill()
t.hideturtle()
t.done()
