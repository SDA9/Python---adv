from turtle import Screen, Turtle
from plank import Plank
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("#031f2b")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_plank = Plank((360, 0))
left_plank = Plank((-360, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_plank.go_up, "Up")
screen.onkey(right_plank.go_down, "Down")
screen.onkey(left_plank.go_up, "w")
screen.onkey(left_plank.go_down, "s")

game_pong = True
while game_pong:
    time.sleep(ball.mvspeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_plank) < 50 and ball.xcor() > 330 or ball.distance(left_plank) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
