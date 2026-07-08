# drawing diffrent shapes
from turtle import Turtle, Screen

screen = Screen()

tim = Turtle()
tim.color("red")

for i in range(3, 10):

    angle = int(360 / i)
    for _ in range(i):
        tim.forward(100)
        tim.right(angle)


screen.exitonclick()
