import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("turtle crossing")
screen.tracer(0)

player = Player()


level = Scoreboard()
level_number = 1
level.current_level(level_number)

screen.listen()
screen.onkeypress(player.go_forward, 'Up')
screen.onkeypress(player.go_back, "Down")
screen.onkey(player.turn_left, "Left")
screen.onkey(player.turn_right, "Right")


car = CarManager()
car.car_creator()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_car()

    if player.finish():
        level_number += 1
        level.current_level(level_number)
        car.increase_speed()

    if car.collision(player):
        level.game_over()
        game_is_on = False




screen.exitonclick()