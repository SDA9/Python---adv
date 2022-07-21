import turtle as module_trt
import random


# module turtle - config
module_trt.colormode(255)
tom = module_trt.Turtle()
tom.speed(20)
tom.penup()
tom.hideturtle()
colors_list = [(200, 241, 235), (150, 180, 220), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tom.setheading(225)
tom.forward(300)
tom.setheading(0)

# ask person
dots_number = 90

# tom is painter
for count_dot in range(1, dots_number + 1):
    tom.dot(30, random.choice(colors_list))
    tom.forward(50)

    if count_dot % 9 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(450)
        tom.setheading(0)

screen_view = module_trt.Screen()
screen_view.exitonclick()
