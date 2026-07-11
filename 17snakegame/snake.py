from turtle import Turtle


class Snake:

    def __init__(self):
        self.bodyofsnake = []
        self.create_snake()

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]

        for position in starting_positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.bodyofsnake.append(segment)

    def control_snake_body(self):
        for i in range(len(self.bodyofsnake) - 1, 0, -1):
            x = self.bodyofsnake[i - 1].xcor()
            y = self.bodyofsnake[i - 1].ycor()
            self.bodyofsnake[i].goto(x, y)

    def up(self):
        self.bodyofsnake[0].setheading(90)

    def left(self):
        self.bodyofsnake[0].setheading(180)

    def right(self):
        self.bodyofsnake[0].setheading(0)

    def down(self):
        self.bodyofsnake[0].setheading(270)
