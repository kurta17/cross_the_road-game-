import turtle as t
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.setheading(90)
        x = self.xcor()
        y = self.ycor()
        self.goto(x,y + MOVE_DISTANCE)
        

