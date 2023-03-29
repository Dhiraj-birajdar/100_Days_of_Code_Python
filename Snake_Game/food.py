from turtle import Turtle
from random import randint as r


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed(0)
        self.goto(r(-280, 280), r(-280, 270))

    def refresh(self):
        self.goto(r(-280, 280), r(-280, 270))
