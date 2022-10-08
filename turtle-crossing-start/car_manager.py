from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-250, 250))
        new_car.setheading(180)
        self.all_cars.append(new_car)

    def car_movement(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def car_speedup(self):
        self.move_speed += MOVE_INCREMENT
