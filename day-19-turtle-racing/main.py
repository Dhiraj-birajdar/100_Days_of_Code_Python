from turtle import Turtle, Screen
from random import randint
screen = Screen()
race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle you want to bet on? Enter color : ")
color = ['red', 'yellow', 'blue', 'green', 'cyan', 'pink']
t_list = []

for i in range(6):
    t_list.append(Turtle(shape='turtle'))
    t_list[i].penup()
    t_list[i].color(color[i])
    t_list[i].setpos(y=105 - 30 * i, x=-230)


# tim = Turtle(shape='turtle')
# tim.penup()
# tim.setpos(x=-230, y=0)

# tim.penup()
# tim.setpos(x=-230, y=0)

if user_bet:
    race_on = True

while race_on:
    for trtl in t_list:
        trtl.forward(randint(1, 10))
        if trtl.xcor() > 220:
            race_on = False
            if trtl.pencolor() == user_bet:
                print(f"You've won! Winner turtle is {trtl.pencolor()}")




screen.exitonclick()