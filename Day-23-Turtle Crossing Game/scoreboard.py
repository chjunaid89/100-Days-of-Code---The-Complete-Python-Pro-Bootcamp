from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(arg=f'Level: {self.level}', align='left', font=FONT)


    def update_score(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='Game Over!', align='center', font=FONT)