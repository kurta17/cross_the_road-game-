import turtle as t
from random import random , randint , choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.allcars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        car = t.Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1,stretch_len=2)
        car.color(choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(300,randint(-250,250))
        self.allcars.append(car)

    def car_move(self):
        for i in self.allcars:
            i.forward(self.car_speed)

    


    
