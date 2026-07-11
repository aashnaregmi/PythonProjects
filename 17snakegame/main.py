from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

screen = Screen()

# Game over message turtle
game_over_text = Turtle()
game_over_text.hideturtle()
game_over_text.penup()
game_over_text.color("white")
score = 0
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"Snake Game")
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
    head.forward(20)
    if (
        head.xcor() > 270
        or head.xcor() < -270
        or head.ycor() > 270
        or head.ycor() < -270
    ):
        game_on = False

        game_over_text.goto(0, 0)
        game_over_text.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    elif head.distance(f.food) < 15:
        score += 1
        screen.title(f"Snake Game -Score:{score}")

        f.add_food()

    screen.update()

screen.exitonclick()
