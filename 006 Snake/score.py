from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.player_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.player_score += 1
        self.clear()
        self.update_score()

