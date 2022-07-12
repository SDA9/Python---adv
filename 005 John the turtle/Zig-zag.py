import turtle as tr
import random

john = tr.Turtle()
colours = ["#33cc8c", "#33b5cc", "#3375cc", "#3345cc", "#ad33cc", "#cc3354", "#adcc33", "#cc8c33"]


john.width(15)
john.shape("turtle")


def rand_move():
    moves = [john.forward(45), john.right(45), john.backward(45), john.left(45)]
    move_ran = moves
    return move_ran


for move in range (1,5):
    john.color(random.choice(colours))
    rand_move()
