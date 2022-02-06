import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.clear()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car = CarManager()
score = Scoreboard()
franklin = Player()

screen.onkeypress(fun=franklin.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.draw_new_car()
    car.remove_car()
    car.move_cars()
    for r in car.carnames:

        if franklin.distance(r) < 23:
            score.game_over()
            game_is_on = False
    if franklin.ycor() > 280:
        score.lvl_up()
        car.lvl_up()
        franklin.lvl_up()


screen.exitonclick()