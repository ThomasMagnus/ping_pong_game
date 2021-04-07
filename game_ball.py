import time
from turtle import Turtle
import random


class GameBall(Turtle):
    x_move = random.choice([-7, -10, 7, 10])
    y_move = random.choice([-7, -10, 7, 10])

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(0.7)
        self.penup()
        self.goto(0, 0)

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        if self.pos()[1] > 335 or self.pos()[1] < -335:
            self.move_on_y()

    def move_on_y(self):
        self.y_move *= -1

    def move_on_x(self):
        self.x_move *= -1