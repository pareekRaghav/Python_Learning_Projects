import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make a bet.', prompt="Who will win the race? ")
colors = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']
speed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turtles = []
x = -235
y = -160
for color in colors:
    turtle_color = color
    color = Turtle(shape='turtle')
    turtles.append(color)
    color.color(turtle_color)
    color.penup()
    y += 50
    color.goto(x, y)



def race():
    race_on = True
    while race_on:
        for turtle in turtles:
            if turtle.xcor() > 220:
                winning_color = turtle.pencolor()
                race_on = False
                print(winning_color)
                if user_bet == winning_color:
                    print("You win!!!")
                else:
                    print("You lose!!")
            else:
                random_distance = random.randint(0, 10)
                turtle.forward(random_distance)


screen.listen()
screen.onkey(fun=race, key='space')
screen.exitonclick()
