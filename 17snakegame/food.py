from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


class Snake:

    def __init__(self):
        self.bodyofsnake = []
        self.create_snake()

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]

        for position in starting_positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.bodyofsnake.append(segment)

    def control_snake_body(self):
        for i in range(len(self.bodyofsnake) - 1, 0, -1):
            x = self.bodyofsnake[i - 1].xcor()
            y = self.bodyofsnake[i - 1].ycor()
            self.bodyofsnake[i].goto(x, y)

    def up(self):
        self.bodyofsnake[0].setheading(90)

    def left(self):
        self.bodyofsnake[0].setheading(180)

    def right(self):
        self.bodyofsnake[0].setheading(0)

    def down(self):
        self.bodyofsnake[0].setheading(270)


s = Snake()


screen.listen()
screen.onkey(s.right, "Right")
screen.onkey(s.down, "Down")
screen.onkey(s.up, "Up")
screen.onkey(s.left, "Left")


class Food:
    def __init__(self):
        self.food = Turtle("circle")
        self.food.shapesize(0.5)
        self.food.color("white")
        self.food.penup()

    def add_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)

        self.food.goto(x, y)


f = Food()

f.add_food()


game_on = True
while game_on:

    time.sleep(0.15)

    s.control_snake_body()
    s.bodyofsnake[0].forward(20)

    screen.update()


screen.exitonclick()
