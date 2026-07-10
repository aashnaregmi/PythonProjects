from turtle import Turtle, Screen
import random

number_of_turtle = int(input("Enter the nuber of turtle you want (2-10): "))


turtles = []
for i in range(number_of_turtle):
    t = Turtle()
    t.shape("turtle")
    t.penup()
    t.goto(-200, -100 + (i * 40))
    t.pendown()
    turtles.append(t)


screen = Screen()


screen.exitonclick()
