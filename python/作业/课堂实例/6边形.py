import turtle as t
t.color('purple','red')
t.begin_fill()
for num in range(6):
    t.fd(50)
    t.left(60)
    t.fd(50)
    t.right(120)
t.end_fill()


t.penup()
t.goto(50,0)

t.color('black','yellow')
t.pendown()
for num in range(6):
    t.fd(50)
    t.right(60)
t.end_fill()
t.done()    
