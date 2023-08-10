from turtle import Turtle
import random
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
cars_list = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(random.randrange(0, 750), random.randrange(-250, 250))
        self.setheading(180)
        self.speed = STARTING_MOVE_DISTANCE

    def car_creator(self):
        for i in range(30):
            car = CarManager()
            cars_list.append(car)

    def move_car(self):
        self.forward(self.speed)
        for car in cars_list:
            car.forward(car.speed)
            if car.xcor() < -350:
                car.goto(350, random.randrange(-250, 250))

    def collision(self, player):
        for car in cars_list:
            if player.distance(car) < 24:
                # level.game_over()
                return True

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
        for car in cars_list:
            car.speed = self.speed



