import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)   # ✅ turn off auto screen updates

t = turtle.Turtle()
t.speed(0)
t.color("red")

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, -y

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
    screen.update()   # ✅ update after each layer

t.hideturtle()

turtle.done()