from turtle import Turtle
import time
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color("black")
        self.goto(-200,250)
        self.hideturtle()


    def print_level(self):
        self.goto(-200,250)
        self.clear()
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)

    def game_over(self, update):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 40, "normal"))
        time.sleep(1)
        self.print_level()
        update()
        self.clear()
    
    def reset_level(self):
        self.level = 0
        self.print_level()
        

    
    
