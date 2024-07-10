from turtle import Turtle, Screen
from random import random, randint, choice
import colorgram

tim = Turtle()
tim.shape("triangle")
tim.ht()
tim.pensize(20)
tim.speed("fastest")
# tim.begin_fill()

screen = Screen()
screen.setup(width=800, height=600)
#
canvwidth = screen.window_width() / 2
canvheight = screen.window_height() / 2

screen.colormode(255)

# rgb_colors = [] # # Use of the colorgram library to extract the low image colour scheme
# colors = colorgram.extract('low_image.jpg', 30)
# # print(colors)
# for color in colors:
#     R = color.rgb.r
#     G = color.rgb.g
#     B = color.rgb.b
#     rgb_color = (R, G, B)
#     rgb_colors.append(rgb_color)

rgb_colors = [(200, 172, 110), (155, 180, 195), (192, 162, 176), (152, 185, 174), (214, 204, 115), (208, 179, 196),
              (161, 212, 187), (174, 189, 212), (163, 202, 213), (114, 121, 182), (186, 157, 62), (213, 181, 180),
              (198, 206, 47), (104, 108, 148), (123, 123, 123)]

y = 0
x = 0


def move_right(gap, repetition, dot_size):  # Runs the dots across the x-axis
    for x in range(repetition):
        tim.dot(dot_size, choice(rgb_colors))
        tim.penup()
        tim.forward(gap)
        tim.pendown()


def move_up(gap, repetition, dot_size): # Runs the dot rows across the y-axis
    tim.penup()
    start_point = ((gap * (repetition - 1)) / 2)
    tim.goto(-start_point, -start_point)
    tim.pendown()
    y_coordinate = start_point
    for y in range(10):
        move_right(gap, repetition, dot_size)
        tim.penup()
        y_coordinate -= gap
        tim.goto(-start_point, -y_coordinate)
        tim.pendown()


move_up(50, 10, 20)

# def move_up_snake(gap, repetition, dot_size):  # Function if you want to make the drawing snake upwards
#     tim.penup()
#     start_point = ((gap * (repetition - 1)) / 2)
#     tim.goto(-start_point, -start_point)
#     tim.pendown()
#     for y in range(10):
#         if y % 2 == 0:
#             move_right(gap, repetition, dot_size)
#             tim.setheading(90)
#             tim.penup()
#             tim.forward(50)
#             tim.setheading(180)
#             tim.forward(50)
#             tim.pendown()
#         else:
#             move_right(gap, repetition, dot_size)
#             tim.setheading(90)
#             tim.penup()
#             tim.forward(50)
#             tim.setheading(0)
#             tim.forward(50)
#             tim.pendown()
#
#
# move_up_snake(50, 10, 20)

screen.exitonclick()
