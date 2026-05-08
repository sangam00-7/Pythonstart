import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle setup
t = turtle.Turtle()
t.speed(1)
t.color("red")
t.pensize(4)

# Starting position
start_x = -250
start_y = 0

# Function to move turtle to next letter
def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)   # always face right
    t.pendown()

# D
move_to(start_x, start_y)
t.left(90)
t.forward(100)
t.right(90)
t.circle(-50, 180)

# I
move_to(start_x + 80, start_y)
t.left(90)
t.forward(100)

# P
move_to(start_x + 130, start_y)
t.left(90)
t.forward(100)
t.right(90)
t.circle(-25, 180)

# E
move_to(start_x + 200, start_y)
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.backward(50)

t.right(90)
t.forward(50)
t.left(90)
t.forward(40)
t.backward(40)

t.right(90)
t.forward(50)
t.left(90)
t.forward(50)

# N
move_to(start_x + 280, start_y)
t.left(90)
t.forward(100)

t.right(150)
t.forward(115)

t.left(150)
t.forward(100)

t.hideturtle()
turtle.done()