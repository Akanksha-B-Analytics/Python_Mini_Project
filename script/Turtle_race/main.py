# Turtle Racing Game
# A Python Turtle Graphics game where players bet on
# the color of a turtle and watch a randomized race
# to see which turtle reaches the finish line first.
# This project demonstrates graphics programming,
# loops, user input, random number generation, and
# basic game development concepts.

from turtle import Turtle , Screen
import random

screen = Screen()
is_game_on=False
screen.setup(width=500,height=400)
user_input= screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Choose any color:")
colour=["Violet","blue","green","yellow","orange","red"]
y_cordinates = [-70, -40,-10,20,50,80]
turtle_list = []
for _ in range(0,6):
    new_name = Turtle(shape='turtle')
    new_name.penup()
    new_name.color(colour[_])
    new_name.goto(x=-230, y=y_cordinates[_])
    turtle_list.append(new_name)

if user_input:
    is_game_on= True


while is_game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            win = turtle.pencolor()
            if win==user_input:
                print(f"You win! the winner is {win}")
            else:
                print(f"You lose! The winning color is {win}")
                is_game_on=False
        rand_distance= random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
