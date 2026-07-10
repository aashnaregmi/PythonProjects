from turtle import Turtle, Screen
import random

number_of_turtle = int(input("Enter the nuber of turtle you want (2-10): "))

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "brown",
    "black",
    "cyan",
]
turtles = []
colorchoosen = []
for i in range(number_of_turtle):
    t = Turtle()
    t.shape("turtle")
    turtlecolor = random.choice(colors)
    while turtlecolor in colorchoosen:
        turtlecolor = random.choice(colors)
    t.color(turtlecolor)
    colorchoosen.append(turtlecolor)
    t.penup()
    t.goto(-200, -100 + (i * 40))
    t.pendown()
    turtles.append(t)
race_on = True
endpoint = 100
while race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= endpoint:
            race_on = False
            print(f"The winner is the {turtle.pencolor()} turtle!")
            break


screen = Screen()


screen.exitonclick()
