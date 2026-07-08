# draw a square
from turtle import Turtle, Screen

screen = Screen()

tim = Turtle()
tim.color("red")


for _ in range(4):
    tim.left(90)
    tim.forward(100)

screen.exitonclick()
