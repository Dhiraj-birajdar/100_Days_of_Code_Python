import random
import turtle as t

t.colormode(255)
t.Screen().bgcolor((0, 0, 0))
tim = t.Turtle()


def rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_shape(sides):
    tim.color(rgb())
    for j in range(sides):
        tim.forward(20)
        tim.right(360/sides)


def spirograph(degree_of_turn):
    tim.speed(0)
    tim.pensize(2)
    for _ in range(int(360/degree_of_turn)):
        tim.color(rgb())
        tim.circle(150)
        # draw_shape(8)
        # tim.right(degree_of_turn)
        tim.setheading(tim.heading() + 5)

spirograph(5)
t.Screen().exitonclick()
