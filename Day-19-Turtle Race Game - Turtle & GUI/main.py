import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your Bet!', prompt='Which color turtle will win the race?')
is_race_on = False

colors = ['red', 'green', 'yellow', 'orange', 'blue', 'brown']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if user_bet == winning_turtle:
                print(f'You won!, The {winning_turtle} turtle is the winner.')
            else:
                print(f'You lose!, The {winning_turtle} turtle is the winner.')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()