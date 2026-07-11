from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # hide drawing animation

bodyofsnake = []  # 1--create a snake body--
starting_positions = [(0, 0), (-20, 0), (-40, 0)]


for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    bodyofsnake.append(segment)

game_on = True
while game_on:
    screen.update()

    for segment in bodyofsnake:
        segment.penup()
        time.sleep(0.15)  # Stop the program for 0.15 sec
        segment.forward(20)  # 2--move--


screen.exitonclick()
