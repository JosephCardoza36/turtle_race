from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=400)
player_one = screen.textinput(title="Player 1: Make your bet", prompt="Which turtle will win the race? Enter a color: ")
player_two = screen.textinput(title="Player 2: Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "chocolate", "green", "blue", "purple"]
all_turtles = []

y_axis = -100 

for turtle in range(0, 6):

    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-480,y=y_axis)
    y_axis += 40
    all_turtles.append(new_turtle)

if player_one:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 480:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == player_one:
                print(f"Player 1 won, the winning turtle was {winning_color}")
            
            elif winning_color == player_two:
                print(f"Player two one, the winning turtle was {winning_color}")
                
            else:
                print(f"Everyone lost, the winning turtle was {winning_color}")
             


        random_distance = (random.randint(0, 10))
        turtle.forward(random_distance)








screen.exitonclick()
