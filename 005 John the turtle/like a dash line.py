import turtle as tr

john = tr.Turtle()

for _ in range(15):
    john.forward(8)
    john.penup()
    john.forward(8)
    john.pendown()
    john.forward(3)
    john.penup()
    john.forward(3)
    john.pendown()

