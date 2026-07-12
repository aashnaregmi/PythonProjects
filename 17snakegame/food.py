from turtle import Turtle, Screen
import random


class Food:
    def __init__(self):
        self.food = Turtle("circle")
        self.food.shapesize(0.5)
        self.food.color("white")
        self.food.penup()
        self.add_food()

    def add_food(self):
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        
        self.food.goto(x, y)
