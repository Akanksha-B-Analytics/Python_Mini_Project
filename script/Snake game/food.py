# Food Class
# A Turtle Graphics-based food object for a Snake Game.
# The food appears at random positions with random
# colors and relocates whenever the snake consumes it.
# This project demonstrates object-oriented programming,
# inheritance, Turtle Graphics, and random number
# generation in Python.



import turtle
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.list_color = ["red","green","blue","yellow","orange","purple"]
        self.color(random.choice(self.list_color))
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 270)
        self.goto(rand_x, rand_y)
