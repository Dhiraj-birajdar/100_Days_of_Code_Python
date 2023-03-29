import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

t = turtle.Turtle()
t.hideturtle()
t.penup()
# def get_xy(x, y):
#     print(x, y)
# screen.onscreenclick(get_xy)
correct_guess = []
game_on = True
score = 0
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
# print(type(states[0]))
while len(correct_guess) < 50:

    ans = (turtle.textinput(title="Guess the State", prompt="What's another state?")).title()
    # print(states.state[ "state" == ans])
    if ans in states:
        t.goto(int(data[data.state == ans].x), int(data[data.state == ans].x))
        t.write(ans)
    if ans == "Exit":
        break
