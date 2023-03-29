from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.title("PONG")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
score = Score()

padr = Paddle(350, 0)
padl = Paddle(-350, 0)
screen.listen()
screen.onkey(padr.up, key="Up")
screen.onkey(padr.down, key="Down")
screen.onkey(padl.up, key="w")
screen.onkey(padl.down, key="s")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # top bottom detection and bounce
    if ball.ycor() < -300 or ball.ycor() > 300:
        ball.bounce_y()

    # paddle detection
    if (ball.distance(padr) < 50 and ball.xcor() > 320) or (ball.distance(padl) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # left right miss detection
    if ball.xcor() > 360:
        ball.ball_reset()
        score.l_up()

    if ball.xcor() < -360:
        ball.ball_reset()
        score.r_up()

screen.exitonclick()
