import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

def quit_game():
    print("goodbye")
    screen.bye()

cars = CarManager()
player = Player()
level = Scoreboard()

screen.onkey(player.move_up, key="Up")
screen.onkey(quit_game, key= "q")
screen.listen()





game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    level.print_level()
    cars.car_move()
    cars.create_car()
    if cars.crash_car(player_xpos=player.xcor(), player_ypos=player.ycor()):
        screen.tracer(1)
        level.game_over(screen.update)
        player.go_start_pos()
        screen.tracer(0)
        cars.reset_cars()
        level.reset_level()
        screen.update()
        

    elif player.ycor() > 300:
        level.level += 1
        level.print_level()
        cars.reset_cars()
        player.go_start_pos()
        cars.incrise_speed()

   

    

screen.exitonclick()

