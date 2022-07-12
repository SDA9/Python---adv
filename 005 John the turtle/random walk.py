import turtle as tr
import random

john = tr.Turtle()
colours = ["#33cc8c", "#33b5cc", "#3375cc", "#3345cc", "#ad33cc", "#cc3354", "#adcc33", "#cc8c33"]
moves = [0, 90, 180, 270]

john.width(15)
john.shape("turtle")
john.speed(10)

for move in range(1, 180):
    john.color(random.choice(colours))
    john.forward(30)
    john.setheading(random.choice(moves))
