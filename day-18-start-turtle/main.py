import turtle
from turtle import Turtle, Screen
# from turtle_random_walk import random_walk
from random import choice
# colors = ['cyan', 'lime green', 'brown', 'magenta', 'gold', 'light coral', 'yellow', 'black', 'red', 'blue', 'orange']
colors = ['red', 'green', 'blue', 'magenta', 'yellow', 'cyan']
tim = Turtle()
angle = [90, 270, 360, 180]
tim.shape('turtle')

# print(tim.right(choice(angle)))
# print(choice(angle))
# tim.forward(20)


def random_walk(step):
    for _ in range(step):
        tim.speed(0)
        tim.pensize(5)
        color = choice(colors)
        pcolor = color
        while color == pcolor:
            color = choice(colors)
        tim.color(color)
        tim.setheading(choice(angle))
        tim.forward(30)


screen = Screen()
screen.bgcolor('black')
# turtle.bgcolor('red')
random_walk(100)


def random_walk1(step):
    for i in range(step):
        tim.speed(0)
        tim.pensize(5)
        tim.color(colors[i % 2])
        tim.right(angle[i % 3])
        # tim.right(90)
        tim.forward(i*3)



# random_walk1(200)
# tim.color('red')
# timmy.forward(100)
# timmy.right(90)
# Draw square
def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

# tim.left(90)


# Draw dashed line
def draw_dashed_line():
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


# Draw multiple shapes (triangle to decagon)



def draw_shape(sides):
    tim.color(choice(colors))
    for j in range(sides):
        tim.forward(100)
        tim.right(360/sides)


# for i in range(3, 11):
#     draw_shape(i)


def draw_dual():
    for s in range(3, 11):
        tim.speed(0)
        for j in range(s):
            tim.forward(100)
            tim.right(360/s)
        for j in range(s):
            tim.forward(100)
            tim.left(360/s)

# tim.speed(0)
# tim.penup()
# tim.left(90)
# tim.forward(500)
# tim.right(90)
# tim.pendown()
# draw_3_10()



screen.exitonclick()
