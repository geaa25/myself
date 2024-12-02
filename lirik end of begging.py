import turtle
import time

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("pink")

t = turtle.turtles()
t.hideturtle()
t.speed(3)

def draw_heart(x, y, size, color, thickness):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.pensize(thickness)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(size)

    for _ in range(200):
        t.right(1)
        t.forward(size = 0.009)

    t.left(120)

    for _ in range(200):
        t.right(1)
        t.forward(size = 0.009)
    t.forward(size)
    t.end_fill()
    t.setheading(0)

heart = [
    (0, -150, 300, "#ff9999", 5),
    (0, -135, 270, "#ffcccc", 5),
    (0, -120, 240, "#ffe6e6", 5),
    (0, -105, 210, "ffcccc", 5),
    (0, -90, 180, "#ff99cc", 5),
    (0, -75, 150, "#ffccff", 5),
    (0, -50, 100, "#ff6666", 5),
]

for heart in heart:
    draw_heart(*heart)
    time.sleep(0,5)
    