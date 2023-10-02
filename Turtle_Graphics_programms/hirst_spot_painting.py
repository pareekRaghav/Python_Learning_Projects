import random
import turtle

import colorgram
from turtle import Turtle, Screen
colors = colorgram.extract('imagejpg.jpg', 30)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

painting_colors = [(240, 234, 83), (209, 159, 99), (185, 11, 67), (114, 177, 205), (26, 115, 166), (217, 131, 165), (173, 170, 30), (167, 78, 34), (131, 185, 147), (223, 60, 105), (10, 28, 72), (176, 48, 96), (34, 134, 80), (235, 76, 44), (234, 229, 4), (234, 164, 192), (78, 11, 59), (11, 49, 29), (25, 167, 209), (19, 43, 131), (58, 167, 100), (11, 100, 60), (134, 214, 228), (84, 25, 11), (135, 32, 20), (161, 211, 176)]

tim = Turtle(visible=False)
tim.penup()
tim.goto(-220,-140)

turtle.colormode(255)
increase = 50
x = -220
y= -280
for i in range(10):
    y += increase
    tim.penup()
    tim.goto(x,y)
    for j in range(10):
        tim.dot(20,random.choice(painting_colors))
        tim.penup()
        tim.forward(50)









screen = Screen()
screen.exitonclick()