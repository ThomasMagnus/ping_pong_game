from turtle import Turtle
from typing import final


class Score(Turtle):
    FONT: final(tuple) = ('Arial', 40, 'normal')

    def __init__(self, goto_x, goto_y):
        super().__init__()
        self.score = 0
        self.goto_x = goto_x
        self.goto_y = goto_y

        self.color('white')
        self.up()
        self.goto(self.goto_x, self.goto_y)
        self.hideturtle()

    def write_score(self):
        self.write(arg=f'{self.score}', font=self.FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write_score()
