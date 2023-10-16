import turtle as t
from random import random , randint , choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.allcars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.move_count = 0
        self.create_car()
    

    def car_move(self):
        for i in self.allcars:
            i.forward(self.car_speed)  
            self.move_count += 1

    def create_car(self):
        if self.move_count % 15 == 0:
            car = t.Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(300,randint(-250,250))
            self.allcars.append(car)

    def crash_car(self, player_xpos, player_ypos):
        for i in self.allcars:
            if - 20 < i.ycor()  - player_ypos < 20  and -30 < i.xcor() - player_xpos  < 30:
                return True
        return False
    
    def reset_cars(self):
        for car in self.allcars:
            car.hideturtle()
        self.allcars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.move_count = 0

    def incrise_speed(self):
        self.car_speed += 5
                

        

    


    
