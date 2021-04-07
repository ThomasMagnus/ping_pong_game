from turtle import Turtle


class Board(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(pos)

    def up(self):
        if self.ycor() < 300:
            self.goto((self.xcor(), self.ycor() + 20))

    def down(self):
        if self.ycor() > -300:
            self.goto((self.xcor(), self.ycor() - 20))
