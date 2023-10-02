import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape('arrow')

distance = 100
angle_moves = [
    {'angle': 120,
     'move': 3},
    {'angle': 90,
     'move': 4},
    {'angle': 72,
     'move': 5},
    {'angle': 60,
     'move': 6},
    {'angle': 51.428,
     'move': 7},
    {'angle': 45,
     'move': 8},
    {'angle': 40,
     'move': 9},
    {'angle': 36,
     'move': 10},
]
colors = ['red', 'green', 'orange', 'purple', 'blue', 'black', 'brown', 'pink']
for i in angle_moves:
    angle = i['angle']
    moves = i['move']
    color = random.choice(colors)
    tim.color(color)
    for j in range(moves):
        tim.forward(distance)
        tim.right(angle)

screen = Screen()
screen.exitonclick()
