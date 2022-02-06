from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("black")
        self.goto(-270, 250)
        self.lvl_nr = 0
        self.lvl()

    def lvl_up(self):
        self.lvl_nr += 1
        self.lvl()


    def lvl(self):
        self.clear()
        self.write(arg=f"Level {self.lvl_nr}" ,font=FONT)



    def game_over(self):
        self.game_over = Turtle()
        self.game_over.penup()
        self.game_over.ht()
        self.game_over.color("black")

        self.game_over.write(arg=f"GAME OVER",align= "center" , font=FONT)


