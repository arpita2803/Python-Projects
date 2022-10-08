import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Please enter a color")
colors = ["purple", "blue", "green", "yellow", "orange", "red"]

turtle.colormode(255)
y_axis = [-75, -45, -15, 15, 45, 75]
all_turtles = []


for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    # new_turtle.speed("slowest")
    new_turtle.goto(x=-230, y=y_axis[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
        else:
            turtle.forward(random.randint(0, 10))

if user_bet == winner:
    print(f"You have won! {winner} Turtle is the winner")
else:
    print(f"You have lost! {winner} Turtle is the winner")

screen.exitonclick()