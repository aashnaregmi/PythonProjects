from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")


timmy_the_turtle.speed("fastest")


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


total_angle = 0


def size_of_gap(size):
    for _ in range(int(360 / size)):
        color = randomcolor()
        timmy_the_turtle.color(color)
        timmy_the_turtle.circle(100)
        current_heading = timmy_the_turtle.heading()
        current_heading += size
        timmy_the_turtle.setheading(current_heading)


size_of_gap(5)


screen.exitonclick()
