import turtle
from turtle import Turtle

import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv('50_states.csv')

correct_answers= []
score = 0
game_is_on = True

while game_is_on:
    if score == 0:
        answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name?").title()
    elif score > 0:
        answer_state = screen.textinput(title=f'{score}/50 States Correct', prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        missing_states = [state for state in states_data['state'].values if state not in correct_answers] #using list comprehension

        # missing_states = []
        # for state in states_data['state'].values:
        #     if state not in correct_answers:
        #         missing_states.append(state)
        new_data_to_learn = pandas.DataFrame(missing_states)
        new_data_to_learn.to_csv('states to learn.csv')
        break

    if answer_state in states_data['state'].values:
        correct_answers.append(answer_state)
        state = states_data[states_data['state'] == answer_state]
        state_x_pos = state.x.item()    # Using item() method
        state_y_pos = state.y.item()

        # state_list = state.values.tolist() # Using list
        # state_x_pos = state_list[0][1]
        # state_y_pos = state_list[0][2]

        state_name = Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(state_x_pos, state_y_pos)
        state_name.write(arg=answer_state, align='center', font=('Aerial', 10, 'normal'))
        score += 1


# to get all the coordinates of all states by clicking on the screen
# and to manually enter these values in csv file against each state
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()
