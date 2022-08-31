from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST =  20
DIRECTION_UP = 90
DIRECTION_DOWN = 270
DIRECTION_LEFT = 180
DIRECTION_RIGHT = 0

class SnakeActions:
    def __init__(self):
        super().__init__()
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        """Creating snake segments. Specific color"""
        for segment in STARTING_POS:
            self.add_part_of_snake(segment)

    def add_part_of_snake(self, segment):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(segment)
        self.snakes.append(new_snake)

    def groving_snake(self):
        """Add a new segment after eating an apple"""
        self.add_part_of_snake(self.snakes[-1].position())

    def move_snake(self):
        """Moving a snake"""
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def move_up(self):
        if self.head.heading() != DIRECTION_DOWN:
            self.head.setheading(DIRECTION_UP)

    def move_down(self):
        if self.head.heading() != DIRECTION_UP:
            self.head.setheading(DIRECTION_DOWN)

    def move_left(self):
        if self.head.heading() != DIRECTION_RIGHT:
            self.head.setheading(DIRECTION_LEFT)

    def move_right(self):
        if self.head.heading() != DIRECTION_LEFT:
            self.head.setheading(DIRECTION_RIGHT)

