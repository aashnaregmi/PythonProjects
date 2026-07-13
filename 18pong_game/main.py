from turtle import Turtle, Screen
import random

import time

screen = Screen()


paddle = Turtle("square")
paddle.shapesize(1, 3)
paddle.color("white")

paddle.penup()
paddle.setpos(-270, 270)
paddle.right(90)


#  y = random.randint(-270, 270)


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"Phong Game")
gameon = True


game_on = True
direction = "down"

while game_on:
    time.sleep(0.05)

    if direction == "down":
        paddle.sety(paddle.ycor() - 10)

        if paddle.ycor() <= -270:
            direction = "up"
    elif direction == "up":
        paddle.sety(paddle.ycor() + 10)

        if paddle.ycor() >= 270:
            direction = "down"

screen.exitonclick()
