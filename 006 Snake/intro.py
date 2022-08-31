from turtle import Screen, Turtle
import snake

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
STARTING_POS_1 = [(-150, 40), (-150, 20), (-150, 0), (-150, -20)]
STARTING_POS_2 = [(-50, 40), (-50, 20), (-50, 0), (-50, -20)]
STARTING_POS_3 = [(50, 40), (50, 20), (50, 0), (50, -20)]
STARTING_POS_4 = [(150, 40), (150, 20), (150, 0), (150, -20)]
DIRECTION_LEFT = 180
DIRECTION_RIGHT = 0
snakes = []
game_pattern = Screen()
game_pattern.setup(width=600, height=600)
game_pattern.bgcolor("black")
game_pattern.title("Smacksnake")
intro_snake = Turtle()


intro_snake.goto(0,120)
intro_snake.color("yellow")
intro_snake.write(f"What kind of color do you prefer?", align=ALIGNMENT, font=FONT)


for segment in STARTING_POS_1:
    intro_snake = Turtle("square")
    intro_snake.shapesize(2)
    intro_snake.color("blue")
    intro_snake.penup()
    intro_snake.goto(segment)
    snakes.append(intro_snake)

for segment in STARTING_POS_2:
    intro_snake = Turtle("square")
    intro_snake.shapesize(2)
    intro_snake.color("white")
    intro_snake.penup()
    intro_snake.goto(segment)
    snakes.append(intro_snake)

for segment in STARTING_POS_3:
    intro_snake = Turtle("square")
    intro_snake.shapesize(2)
    intro_snake.color("red")
    intro_snake.penup()
    intro_snake.goto(segment)
    snakes.append(intro_snake)

for segment in STARTING_POS_4:
    intro_snake = Turtle("square")
    intro_snake.shapesize(2)
    intro_snake.color("green")
    intro_snake.penup()
    intro_snake.goto(segment)
    snakes.append(intro_snake)

game_pattern.tracer(0)

game_pattern.update()

intro_snake.goto(-150, 70)
intro_snake.color("blue")
intro_snake.write(f"blue", align=ALIGNMENT, font=FONT)

intro_snake.goto(-50, 70)
intro_snake.color("white")
intro_snake.write(f"white", align=ALIGNMENT, font=FONT)

intro_snake.goto(50, 70)
intro_snake.color("red")
intro_snake.write(f"red", align=ALIGNMENT, font=FONT)

intro_snake.goto(150, 70)
intro_snake.color("green")
intro_snake.write(f"green", align=ALIGNMENT, font=FONT)

snake_color = input("Podaj jaki kolor Cię interesuje: ")

intro_snake.goto(-10, -150)
intro_snake.color("white")
intro_snake.write(f"You have chosen the color {snake_color}", align=ALIGNMENT, font=FONT)


game_pattern.exitonclick()
