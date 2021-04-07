from turtle import Screen
from board import Board
from game_ball import GameBall
from score import Score
import time

screen = Screen()
screen.setup(800, 700)
screen.bgcolor('black')
screen.title('Ping Pong')
screen.tracer(0)

board_right = Board((350, 0))
board_left = Board((-350, 0))

game_ball = GameBall()

score_1 = Score(50, 280)
score_2 = Score(-50, 280)
score_1.write_score()
score_2.write_score()

screen.listen()
screen.onkeypress(board_right.up, 'Up')
screen.onkeypress(board_right.down, 'Down')
screen.onkeypress(board_left.up, 'w')
screen.onkeypress(board_left.down, 's')


def ball_on_board():
    if game_ball.distance(board_right) < 55 and game_ball.xcor() >= 330 \
            or game_ball.distance(board_left) < 55 and game_ball.xcor() <= -330:
        game_ball.move_on_x()


def score_refresh(score_class):
    score_class.refresh_score()
    time.sleep(1.5)
    game_ball.goto(0, 0)


game_on = True

while game_on:
    screen.update()
    time.sleep(0.03)
    game_ball.ball_move()

    ball_on_board()

    if game_ball.xcor() > 400:
        score_refresh(score_1)
        board_right.goto(350, 0)
        board_left.goto(-350, 0)

    if game_ball.xcor() < -400:
        score_refresh(score_2)
        board_right.goto(350, 0)
        board_left.goto(-350, 0)

screen.exitonclick()
