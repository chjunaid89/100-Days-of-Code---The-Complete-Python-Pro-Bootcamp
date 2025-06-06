#First need to run this code for colors extraction from image.
#Copy colors extracted into a list
# import colorgram
#
# colors_extracted = colorgram.extract("hirst_dot_painting.jpg", 30)
# print(len(colors_extracted))
# color_bank = []
# for color in colors_extracted:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     color_bank.append(rgb)
# print(color_bank)

import random
import turtle
from turtle import Turtle, Screen

def row_of_dots(color_list):
    for i in range(10):
        tim.color(random.choice(color_list))
        tim.dot(15)
        tim.penup()
        tim.forward(50)

colors = [(242, 233, 239), (231, 241, 236), (191, 165, 116), (139, 166, 189), (59, 101, 137), (138, 90, 53), (13, 23, 53), (221, 206, 125), (60, 23, 12), (181, 146, 165), (178, 152, 47), (142, 176, 150), (74, 116, 82), (61, 15, 26), (124, 80, 101), (16, 38, 25), (127, 32, 18), (25, 52, 124), (178, 188, 215), (110, 34, 48), (162, 106, 135), (98, 149, 102), (96, 122, 172), (209, 180, 195), (171, 106, 95), (172, 205, 181), (77, 148, 163), (26, 89, 64)]

tim = Turtle()
turtle.colormode(255)
tim.hideturtle()
tim_x_pos = -225
tim_y_pos = -200
tim.teleport(tim_x_pos, tim_y_pos)

for i in range(10):
    row_of_dots(colors)
    tim_y_pos += 50
    tim.teleport(tim_x_pos, tim_y_pos)


screen = Screen()
screen.exitonclick()