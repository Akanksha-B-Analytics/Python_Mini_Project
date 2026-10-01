# Creates a Hirst-style dot painting using Python Turtle Graphics.
# Generates a grid of colored dots at random from a predefined color palette.
# Uses functions to manage positioning, drawing, and row transitions.

import turtle as t
import random

t.colormode(255)
lucky=t.Turtle()
lucky.shape("turtle")
colour_list=[ (202, 164, 109), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def right_direction():
    lucky.setheading(225)
    lucky.penup()
    lucky.forward(250)
    lucky.pendown()
    lucky.setheading(0)

def dot_line():
    for _ in range(10):
         lucky.dot(20,random.choice(colour_list))
         lucky.penup()
         lucky.forward(50)
         lucky.pendown()

def default_position():
    lucky.penup()
    lucky.setheading(90)
    lucky.forward(50)
    lucky.setheading(180)
    lucky.forward(500)
    lucky.setheading(0)
    lucky.pendown()

right_direction()
for _ in range(10):
    dot_line()
    default_position()

screen = t.Screen()
screen.exitonclick()







