from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.write(f"Score: {self.level}", align="center", font=("courier", 20, "normal"))
        # self.score_up()

    def score_up(self):
        self.clear()
        self.level += 1
        self.write(f"Score: {self.level}", align="center", font=("courier", 20, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("courier", 20, "normal"))