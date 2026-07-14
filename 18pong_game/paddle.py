from turtle import Turtle


class Paddle:
    def __init__(self, x, y):

        self.paddle = Turtle("square")
        self.paddle.hideturtle()
        self.paddle.shapesize(1, 3)
        self.paddle.color("white")

        self.paddle.penup()
        self.paddle.right(90)
        self.paddle.goto(x, y)
        self.paddle.showturtle()

    def move_up(self):
        if self.paddle.ycor() < 270:
            self.paddle.sety(self.paddle.ycor() + 20)

    def move_down(self):
        if self.paddle.ycor() > -270:
            self.paddle.sety(self.paddle.ycor() - 20)
