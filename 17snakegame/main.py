from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # hide drawing animation


s = Snake()


screen.listen()
screen.onkey(fun=s.right, key="Right")
screen.onkey(fun=s.down, key="Down")
screen.onkey(fun=s.up, key="Up")
screen.onkey(fun=s.left, key="Left")


game_on = True
while game_on:

    time.sleep(0.15)  # Stop the program for 0.15 sec
    s.control_snake_body()  # 3--control movement--
    s.bodyofsnake[0].forward(20)  # 2--move--
    screen.update()

screen.exitonclick()
