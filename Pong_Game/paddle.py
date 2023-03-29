from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        # pad1.speed(0)
        self.setheading(90)
        self.penup()
        self.goto(x, y)
        self.shapesize(1.2, 6)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)