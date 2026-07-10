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

    turtles.append(t)
race_on = True
endpoint = 200
# hidden turtle
finishline = Turtle()
finishline.penup()
finishline.hideturtle()
finishline.pensize(5)
finishline.goto(200, -300)
finishline.setheading(90)
finishline.pendown()
finishline.forward(770)


while race_on:
    for turtle in turtles:

        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= endpoint:
            race_on = False
            print(f"The winner is the {turtle.pencolor()} turtle!")
            break


screen = Screen()


screen.exitonclick()
