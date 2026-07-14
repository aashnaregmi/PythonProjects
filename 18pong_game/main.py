from turtle import Turtle, Screen
import random
from paddle import Paddle
import time

screen = Screen()
screen.tracer(0)


# start

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"Phong Game")

p1 = Paddle(-270, 0)
screen.listen()
screen.onkey(fun=p1.move_up, key="s")
screen.onkey(fun=p1.move_down, key="x")


p2 = Paddle(270, 0)
screen.listen()
screen.onkey(fun=p2.move_up, key="Up")
screen.onkey(fun=p2.move_down, key="Down")


game_on = True


while game_on:

    screen.update()


screen.exitonclick()
