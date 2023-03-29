from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        # self.shapesize(1.2, 1.2)
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
