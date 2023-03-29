# import colorgram as cg
# ls = cg.extract('spot_painting.jpg', 30)
# print(ls)
# for clr in ls:
#     colors.append((clr.rgb.r, clr.rgb.g, clr.rgb.b))

import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

colors = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
          (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121),
          (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
          (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]


def paint(size):
    tim.hideturtle()
    tim.penup()
    tim.speed(0)
    for i in range(size):
        tim.setx(-200)
        tim.sety(-200 + (i * 50))
        for j in range(size):
            tim.dot(20, random.choice(colors))
            tim.forward(50)
        tim.goto(0, (i+1) * 50)


# function call
paint(5)
t.Screen().exitonclick()