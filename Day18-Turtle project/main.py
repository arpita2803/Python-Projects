import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("yellow green")

# for _ in range(0, 4):
#    timmy.forward(100)
#    timmy.right(90)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# colors = ["purple", "blue", "deep sky blue", "green", "yellow", "orange", "red", "brown"]
# for i in range(3, 11):
#    timmy.pen(pencolor=random.choice(colors))
#    angle = 360 / i
#    for j in range(i):
#        timmy.forward(100)
#        timmy.right(angle)

# colors = ["purple", "blue", "deep sky blue", "green", "yellow", "orange", "red", "brown"]
# angle = [0, 90, 180, 270]
timmy.speed("fastest")
# timmy.pensize(15)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# for _ in range(0, 200):
#     timmy.pencolor(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(angle))

for _ in range(0, 361, 5):
    timmy.pencolor(random_color())
    timmy.circle(100)
    timmy.setheading(_)

screen = Screen()
screen.exitonclick()
