from turtle import Turtle, Screen

john_the_turtle = Turtle()

jtt_move = 0

john_the_turtle.color("#33cc8c")

while jtt_move < 4:
    john_the_turtle.forward(100)
    john_the_turtle.left(90)
    jtt_move += 1


