import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

index = 1
game_is_on = True
while game_is_on:
    index += 1
    time.sleep(0.1)
    screen.update()
    if index % 6 == 0:
        car_manager.create_car()
    car_manager.car_movement()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.car_speedup()

screen.exitonclick()
