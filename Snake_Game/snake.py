from turtle import Turtle
# MOVE_DISTANCE = 20
# POSITION = [(0, 0), (-20, 0), (-40, 0)] # for setpos line 17
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.setpos(x=0 - 20 * i, y=0)
            self.snake_body.append(snake)
        self.snake_body[0].color("red")

    def grow(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        # snake.setpos(x=0 - 20 * i, y=0)
        snake.goto(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())
        self.snake_body.append(snake)

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto((self.snake_body[i - 1].xcor(), self.snake_body[i - 1].ycor()))
        self.head.forward(20)
        # self.snake_body[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset(self):
        for s in self.snake_body:
            s.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]