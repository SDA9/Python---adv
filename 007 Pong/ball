from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#f2f2ed")
        self.shape("circle")
        self.penup()
        self.x_direction = 10
        self.y_direction = 10
        self.mvspeed = 0.07

    def move(self):
        x_position = self.xcor() + self.x_direction
        y_position = self.ycor() + self.y_direction
        self.goto(x_position, y_position)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1
        self.mvspeed *= 0.95

    def reset_position(self):
        self.goto(0, 0)
        self.mvspeed = 0.07
        self.bounce_x()
