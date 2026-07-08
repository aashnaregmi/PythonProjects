# drawing diffrent shapes
from turtle import Turtle, Screen

screen = Screen()

tim = Turtle()
tim.color("red")


for _ in range(3):
    tim.right(120)
    tim.forward(100)


screen.exitonclick()
