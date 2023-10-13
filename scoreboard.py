from turtle import Turtle
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
        self.clear()
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)
        

    
    
