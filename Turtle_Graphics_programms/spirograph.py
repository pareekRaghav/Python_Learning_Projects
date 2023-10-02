import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape('arrow')

def choose_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r,g,b)
    return my_color

screen = Screen()
screen.colormode(255)
tim.speed('fastest')
for i in range(120):
    circle_colors = choose_color()
    tim.pencolor(circle_colors)
    tim.circle(-100)
    tim.right(3)


screen.exitonclick()
