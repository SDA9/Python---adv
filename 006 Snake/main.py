from turtle import Screen, Turtle
from snake import SnakeActions
from food import Food
from score import Score
import time

game_pattern = Screen()
game_pattern.setup(width=600, height=600)
game_pattern.bgcolor("black")
game_pattern.title("Smacksnake")
game_pattern.tracer(0)
time_parameter = 0.21

snake = SnakeActions()
food = Food()
score = Score()

game_pattern.listen()
game_pattern.onkey(snake.move_up, "Up")
game_pattern.onkey(snake.move_down, "Down")
game_pattern.onkey(snake.move_left, "Left")
game_pattern.onkey(snake.move_right, "Right")



snake_is_alive = True
while snake_is_alive:
    game_pattern.update()
    time.sleep(time_parameter)
    snake.move_snake()

    if snake.head.distance(food) < 16:
        if time_parameter >= 0.05 and score.player_score % 2 == 0:
            time_parameter -= 0.02
        else:
            time_parameter == 0.05
        food.refresh()
        snake.groving_snake()
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake_is_alive = False
        score.game_over()

    for segment in snake.snakes:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake_is_alive = False
            score.game_over()

game_pattern.exitonclick()
