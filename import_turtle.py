import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, -y   # correct orientation

t.penup()

for i in range(1, 16):
    t.goto(0, 0)
    t.pendown()
    first = True
    
    for k in range(0, 629):
        x, y = corazon(k / 100)
        sx, sy = x * i, y * i
        
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