from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake_body = []
position_of_body = [(0, 0), (-20, 0), (-40, 0)]


for i in position_of_body:
    t = Turtle("square")
    t.penup()
    t.color("white")
    t.goto(i)
    snake_body.append(t)


screen.exitonclick()
