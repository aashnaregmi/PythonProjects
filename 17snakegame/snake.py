from turtle import Turtle


class Snake:

    def __init__(self):
        self.bodyofsnake = []
        self.add_segment()

    #     self.createsnake()

    # def createsnake(self):

    #     self.add_segment(1)
    #     self.add_segment(1)
    #     self.add_segment(1)

    def add_segment(self, length=1):
        for i in range(length):
            segment = Turtle("square")
            segment.color("white")
            segment.shapesize(stretch_wid=1, stretch_len=1)
            segment.penup()
            if len(self.bodyofsnake) == 0:
                segment.goto(i * -20, 0)
            else:
                segment.goto(self.bodyofsnake[-1].position())

            self.bodyofsnake.append(segment)

    def control_snake_body(self):
        for i in range(len(self.bodyofsnake) - 1, 0, -1):
            x = self.bodyofsnake[i - 1].xcor()
            y = self.bodyofsnake[i - 1].ycor()
            self.bodyofsnake[i].setpos(x, y)

    def up(self):
        if self.bodyofsnake[0].heading() != 270:
            self.bodyofsnake[0].setheading(90)

    def down(self):
        if self.bodyofsnake[0].heading() != 90:
            self.bodyofsnake[0].setheading(270)

    def left(self):
        if self.bodyofsnake[0].heading() != 0:
            self.bodyofsnake[0].setheading(180)

    def right(self):
        if self.bodyofsnake[0].heading() != 180:
            self.bodyofsnake[0].setheading(0)
