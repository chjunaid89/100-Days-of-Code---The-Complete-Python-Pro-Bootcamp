from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Aerial', 12, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score_update()


    def score_update(self):
        self.clear()
        self.write(arg=f'Score = {self.score}', align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER!', align=ALIGNMENT, font=FONT)
