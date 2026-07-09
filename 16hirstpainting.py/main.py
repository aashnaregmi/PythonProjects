import colorgram
import random
from turtle import Turtle, Screen, colormode

colormode(255)
colors = colorgram.extract("painting.jpeg", 10)
screen = Screen()
tim = Turtle()
tim.speed("fastest")

rgb_colors = []

for color in colors:  # color = Rgb(r=239, g=230, b=215)
    r = color.rgb.r  # r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    rgb_colors.append((r, g, b))

total_dots = 100
count = 0

for _ in range(100):
    tim.dot(10, random.choice(rgb_colors))
    count += 1
    tim.penup()
    tim.forward(30)
    tim.pendown()
    if count % 10 == 0:
        tim.penup()
        tim.hideturtle()
        tim.left(90)
        tim.forward(30)
        tim.left(90)
        tim.forward(300)
        tim.setheading(0)
        tim.pendown()
        tim.showturtle()


screen.exitonclick()
