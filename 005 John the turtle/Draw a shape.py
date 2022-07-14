import turtle as tr
import random

lot_of_circles = 0
lot_of_squares = 0

john = tr.Turtle()
tr.colormode(255)
john.pensize(1)
john.speed(26)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


figure_selection = input("What do you choose? Many circles or many squares? [c/s/t/6/0]: ")
color_selection = input("What color do you like? r - random / b - blue / g = green: ")


if color_selection == "r":
    john.color(random_color())
elif color_selection == "g":
    john.color(55, 140, 125)
elif color_selection == "b":
    john.color(46, 74, 234)


if figure_selection == "c":
    while lot_of_circles < 100:
        john.circle(85)
        cur_heading = john.heading()
        john.setheading(cur_heading + 10)
        lot_of_circles += 1
elif figure_selection == "t":
    while lot_of_squares < 100:
        for side in range (1,3):
            john.forward(150)
            john.right(360/3)
        cur_heading = john.heading()
        john.setheading(cur_heading + 10)
        lot_of_squares += 1
elif figure_selection == "s":
    while lot_of_squares < 100:
        for side in range (1,3):
            john.forward(150)
            john.right(360/4)
        cur_heading = john.heading()
        john.setheading(cur_heading + 10)
        lot_of_squares += 1
elif figure_selection == "6":
    while lot_of_squares < 100:
        for side in range (1,3):
            john.forward(150)
            john.right(360/6)
        cur_heading = john.heading()
        john.setheading(cur_heading + 10)
        lot_of_squares += 1
else:
    while lot_of_squares < 100:
        for side in range (1,3):
            john.forward(150)
            john.left(45)
        cur_heading = john.heading()
        john.setheading(cur_heading + 10)
        lot_of_squares += 1

screen = tr.Screen()
screen.exitonclick()

