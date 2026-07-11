from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # hide drawing animation

bodyofsnake = []  # 1--create a snake body--
starting_positions = [(0, 0), (-20, 0), (-40, 0)]


for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    bodyofsnake.append(segment)


def control_snake_body():
    for i in range(len(bodyofsnake) - 1, 0, -1):
        x = bodyofsnake[i - 1].xcor()
        y = bodyofsnake[i - 1].ycor()
        bodyofsnake[i].goto(x, y)


def up():
    bodyofsnake[0].setheading(90)


def left():
    bodyofsnake[0].setheading(180)


def right():
    bodyofsnake[0].setheading(0)


def down():
    bodyofsnake[0].setheading(270)


screen.listen()
screen.onkey(fun=right, key="Right")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=up, key="Up")
screen.onkey(fun=left, key="Left")


game_on = True
while game_on:

    time.sleep(0.15)  # Stop the program for 0.15 sec
    control_snake_body()  # 3--control movement--
    bodyofsnake[0].forward(20)  # 2--move--
    screen.update()

screen.exitonclick()
