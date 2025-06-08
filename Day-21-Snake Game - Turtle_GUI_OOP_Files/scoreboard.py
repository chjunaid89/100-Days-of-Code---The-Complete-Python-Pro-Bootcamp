from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Aerial', 12, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score_update()


    def score_update(self):
        self.clear()
        self.write(arg=f'Score = {self.score}  |  High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.score_update()

    def increase_score(self):
        self.score += 1
        self.score_update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg='GAME OVER!', align=ALIGNMENT, font=FONT)
