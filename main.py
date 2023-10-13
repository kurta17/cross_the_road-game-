import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = CarManager()
player = Player()
level = Scoreboard()

screen.onkey(player.move_up, key="Up")
screen.listen()





game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    level.print_level()
    cars.car_move()
    if cars.crash_car(player_xpos=player.xcor(), player_ypos=player.ycor()) == True:
        screen.tracer(1)
        level.game_over(screen.update)
        player.go_start_pos()
        screen.tracer(0)
        screen.update()

    if player.ycor() > 300:
        level.level += 1
        level.print_level()
        player.go_start_pos()

screen.exitonclick()

