from turtle import Turtle, Screen

import random


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
