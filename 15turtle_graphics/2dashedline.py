##draw a dashed line
from turtle import Turtle, Screen

screen = Screen()

tim = Turtle()
tim.color("red")


for _ in range(9):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen.exitonclick()
