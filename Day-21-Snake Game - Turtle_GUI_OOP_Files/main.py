from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game V1.0')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with the food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with the wall
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # Detect collision with the tail
    for box in snake.boxes[1:]:
        if snake.snake_head.distance(box) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()




screen.exitonclick()