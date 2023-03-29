import random
import turtle as t

angle = [0, 90, 180, 270]
t.colormode(255)
t.Screen().bgcolor((0,0,0))
tim = t.Turtle()


def rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk(step):
    tim.speed(0)
    tim.pensize(10)
    for _ in range(step):
        tim.color(rgb())
        # tim.setheading(random.choice(angle))
        tim.setheading(random.randint(0, 360))
        tim.forward(30)


random_walk(200)
t.Screen().exitonclick()
