import turtle as t
def draw_N_TX(n):
    num = (n-2)*180
    J = num /n
    for i in range(n):
        t.fd(50)
        t.left(180-J)
        t.fd(50)
        t.right(2*(180-J))

draw_N_TX(5)
t.penup()
t.goto(50,0)
t.pendown()
draw_N_TX(5)
t.penup()
t.goto(-50,0)
t.pendown()
draw_N_TX(5)
