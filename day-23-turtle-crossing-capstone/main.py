from level import Level
from ninja_turtle import Ninja
from time import sleep
from turtle import Screen
from cars import Cars, Drive

car = Drive()
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()
score = Level()
tim = Ninja()

screen.onkeypress(tim.move, key="Up")
game_on = True
while game_on:
    screen.update()
    if tim.ycor() > 260:
        tim.start()
        score.score_up()
    sleep(0.1)
    car.spawn()
    car.drive()
    if car.collision(tim):
        game_on = False
        score.game_over()


screen.exitonclick()
