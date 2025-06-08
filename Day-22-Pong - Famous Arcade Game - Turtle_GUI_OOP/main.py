import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the Up & Down walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect collision with the right wall
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    # Detect collision with the left wall
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()