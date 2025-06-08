import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkeypress(player.move , 'Up')
    car_manager.create_car()
    car_manager.car_move()
    print(car_manager.car_speed)

    # Detect player position at level finish line
    if player.ycor() >= 280:
        player.start_again()
        scoreboard.update_score()
        car_manager.increase_car_speed()

    # Detect player collision with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
