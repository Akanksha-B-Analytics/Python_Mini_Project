# U.S. States Guessing Game
# An interactive geography game built with Python,
# Turtle Graphics, and Pandas. Players guess the names
# of U.S. states and see their locations displayed on
# a map. The game tracks correct guesses and saves
# unguessed states to a CSV file for future learning.
# This project demonstrates data handling, loops,
# conditional statements, and graphical programming.

import turtle
import pandas

screen =turtle.Screen()
screen.title("U.S States Game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()#table column , turned column into a list



guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 U.S State", prompt="What's the name of the state").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data.state== answer_state]
        t.goto(row.x.item() , row.y.item())
        t.write(answer_state) ##when it get to the location it will write the state name

