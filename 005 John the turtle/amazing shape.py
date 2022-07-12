import turtle as tr
import random

john = tr.Turtle()
colours = ["#33cc8c", "#33b5cc", "#3375cc", "#3345cc", "#ad33cc", "#cc3354", "#adcc33", "#cc8c33"]

def draw_amazing_shape(number_sides):
    angle = 360 / number_sides
    for _ in range(number_sides):
        angle = 360 / number_sides
        john.forward(100)
        john.right(angle)

for n_shape_side in range (5,21):
    john.color(random.choice(colours))
    draw_amazing_shape(n_shape_side)



