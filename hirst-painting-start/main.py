# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

art_colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

timmy = Turtle()
turtle.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.setpos((-200, -200))
numbers = 100

for i in range(1, numbers+1):
    timmy.dot(20, random.choice(art_colors))
    timmy.forward(50)
    if i % 10 == 0:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.setheading(0)
timmy.hideturtle()

screen = Screen()
screen.exitonclick()


