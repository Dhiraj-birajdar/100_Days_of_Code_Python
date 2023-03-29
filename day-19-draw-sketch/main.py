from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def clear_screen():
    screen.reset()


def left_turn():
    tim.setheading(tim.heading() + 10)


def right_turn():
    tim.setheading(tim.heading() - 10)


screen.listen()

screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(left_turn, "a")
screen.onkeypress(right_turn, "d")

screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()