from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#f2f2ed")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.goto(-70, 200)
        self.write(self.left_score, align="center", font=("courier", 80, "normal"))
        self.goto(70, 200)
        self.write(self.right_score, align="center", font=("courier", 80, "normal"))

    def left_point(self):
        self.left_score += 1
        self.scoreboard_update()

    def right_point(self):
        self.right_score += 1
        self.scoreboard_update()
