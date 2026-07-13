from turtle import Turtle, Screen
import random

import time

screen = Screen()
screen.tracer(0)


class Paddle:
    def __init__(self):

        self.paddle = Turtle("square")
        self.paddle.hideturtle()
        self.paddle.shapesize(1, 3)
        self.paddle.color("white")

        self.paddle.penup()
        self.paddle.right(90)
        self.paddle.goto(-270, 270)
        self.paddle.showturtle()

    def move_down(self):
        new_y = self.paddle.ycor() - 10
        self.paddle.sety(new_y)

    def move_up(self):
        new_y = self.paddle.ycor() + 10
        self.paddle.sety(new_y)

    # def up(self):
    #     new_y = self.paddle.ycor() + 10
    #     self.paddle.sety(new_y)

    # def down(self):
    #     self.paddle.setheading(270)


#  y = random.randint(-270, 270)


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"Phong Game")

p = Paddle()


game_on = True
direction = "down"
screen.listen()
screen.onkey(fun=p.move_down, key="Down")
screen.onkey(fun=p.move_up, key="Up")


while game_on:
    time.sleep(0.05)
    screen.update()
    if direction == "down":
        p.move_down()
        if p.paddle.ycor() <= -270:
            direction = "up"
    elif direction == "up":
        p.move_up()

        if p.paddle.ycor() >= 270:
            direction = "down"

screen.exitonclick()
