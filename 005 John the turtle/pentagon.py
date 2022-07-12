import turtle as tr

john = tr.Turtle()

number_of_sides = 5

for _ in range(number_of_sides):
    angle = 360 / number_of_sides
    john.forward(100)
    john.right(angle)
