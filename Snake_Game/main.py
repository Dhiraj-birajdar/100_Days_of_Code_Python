from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()

# screen.onkey(start, "Enter")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # Detects food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.grow()
    # Detects wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    # Detects tail/body collision
    for snake_seg in snake.snake_body[1:]:
        if snake.head.distance(snake_seg) < 10:
            snake.reset()
            score.reset()

screen.exitonclick()
