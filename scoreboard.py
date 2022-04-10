import turtle as t

FONT = ('Arial', 18, 'normal')

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
        self.level = 1

    def update_scoreboard(self):
        self.clear()
        self.goto(0,270)
        self.write(f'Space Invaders Score: {self.score}', align = 'center', font  = FONT)

    def add_score(self):
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=FONT)
