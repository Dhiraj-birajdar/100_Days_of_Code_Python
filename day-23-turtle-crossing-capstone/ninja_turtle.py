from turtle import Turtle


class Ninja(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.start()

    def start(self):
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(10)
