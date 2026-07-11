from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # hide drawing animation

bodyofsnake = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]


for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    bodyofsnake.append(segment)

screen.update()  # show final result

screen.exitonclick()
