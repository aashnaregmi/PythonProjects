# drawing diffrent shapes
from turtle import Turtle, Screen
import random

screen = Screen()
colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "black",
]

tim = Turtle()
tim.color("red")

for i in range(3, 10):
    color = random.choice(colors)
    tim.color(color)
    angle = 360 / i
    for _ in range(i):

        tim.right(angle)
        tim.forward(100)


screen.exitonclick()
