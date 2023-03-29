from turtle import Turtle, Screen
from random import randrange as r
# import time


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.clr = Screen()
        self.drive_speed = r(8, 50)
        self.shape("square")
        self.shapesize(1, 2)
        self.clr.colormode(255)
        self.car()

    def car(self):
        self.penup()
        self.hideturtle()
        self.color(r(10, 220, 1), r(10, 220, 1), r(10, 220, 1))
        self.goto(320, r(200, -200, -30))
        self.pendown()
        self.showturtle()
        # self.backward(100)
        # while not (self.xcor() < -320):
        #     self.backward(self.drive_speed)

    def move(self):
        self.backward(self.drive_speed)


class Drive(Cars):
    def __init__(self):
        super().__init__()
        self.drive_speed = 10
        self.cars = []

    def spawn(self):
        if not r(1, 100) % 2:
            car = Cars()
            self.cars.append(car)

    def drive(self):
        for cr in self.cars:
            # cr.backward(self.drive_speed)
            cr.move()

    def collision(self, ninja):
        for i in range(len(self.cars)):
            if self.cars[i].distance(ninja) < 20:
                print("collision")
                return True
        return False
