import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * \
        math.cos(2*n) - 2 * math.cos(3*n) - \
        math.cos(4*n)
    return y, x  # flip y so heart points upward

t.penup()
for i in range(1, 16):          # start at 1 (size 0 is invisible)
    t.goto(0, 0)
    t.pendown()
    first = True
    for k in range(0, 629):     # 0 to 2π × 100 steps
        x, y = corazon(k / 100) # smooth parametric sampling
        sx, sy = x * i, y * i   # scale by layer index
        if first:
            t.penup()
            t.goto(sx, sy)
            t.pendown()
            first = False
        else:
            t.goto(sx, sy)
    t.penup()

t.hideturtle()
turtle.done()