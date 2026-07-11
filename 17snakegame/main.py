from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # hide drawing animation

s = Snake()
f = Food()

screen.listen()
screen.onkey(fun=s.right, key="Right")
screen.onkey(fun=s.down, key="Down")
screen.onkey(fun=s.up, key="Up")
screen.onkey(fun=s.left, key="Left")


game_on = True


f.add_food()
while game_on:
    head = s.bodyofsnake[0]
    time.sleep(0.15)

    s.control_snake_body()
    s.bodyofsnake[0].forward(20)

    if s.bodyofsnake[0].distance(f.food) < 15:
        f.add_food()

    screen.update()

screen.exitonclick()
