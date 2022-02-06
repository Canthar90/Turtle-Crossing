from turtle import Turtle
import heroes
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.carnames = []
        self.speed = STARTING_MOVE_DISTANCE

    def draw_new_car(self):
        self.draw_chance = random.randint(-1, 5)
        if self.draw_chance == 1:
            self.carnames.append(heroes.gen())
            self.carnames[-1] = Turtle("square")
            self.carnames[-1].penup()
            self.carnames[-1].shapesize(stretch_wid=1, stretch_len=2, outline=None)
            self.carnames[-1].color(random.choice(COLORS))
            self.carnames[-1].goto(320, random.randint(-230, 230))

    def remove_car(self):
        for n in range(len(self.carnames)-1):
            if self.carnames[n].xcor() < -340:
                self.carnames[n].ht()
                self.carnames[n].clear()
                # del self.carnames[n]


    def move_cars(self):
        for l in self.carnames:
            l.goto((l.xcor() - self.speed),l.ycor())



    def lvl_up(self):
        self.speed += MOVE_INCREMENT



