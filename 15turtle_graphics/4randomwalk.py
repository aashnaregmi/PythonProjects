from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
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
    "cyan",
]

timmy_the_turtle.speed("fastest")


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]
timmy_the_turtle.pensize(8)
for _ in range(200):
    random_direction = random.choice(direction)
    color = randomcolor()
    timmy_the_turtle.color(color)

    timmy_the_turtle.setheading(random_direction)
    timmy_the_turtle.forward(30)


screen.exitonclick()
