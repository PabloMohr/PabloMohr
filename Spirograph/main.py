import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.color(random_color())

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
