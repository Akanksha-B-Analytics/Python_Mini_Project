# Snake Class
# A Turtle Graphics-based Snake Game component that
# controls snake creation, movement, growth, and
# directional input. The snake grows as it consumes
# food and follows classic Snake Game mechanics.
# This project demonstrates object-oriented
# programming, lists, loops, and game movement logic.

from turtle import Turtle

STARTING_POSITION =[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):

        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]
        self.move()

    def create_snake(self): ##creats the default snake
        for position in STARTING_POSITION:
           self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.all_turtles.append(turtle)

    def extend_snake(self):
        self.add_segment(self.all_turtles[-1].position()) ## position of last segment of the list
                 ##this position() comes from the turtle class that give us the position of the segment
    #[(0,0),(-20,0),(-40,0), (-40,0)]
    def move(self):
        for seg_name in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[seg_name - 1].xcor()  ##2nd last object
            new_y = self.all_turtles[seg_name - 1].ycor()
            self.all_turtles[seg_name].goto(new_x, new_y)  ##last object
        self.head.forward(MOVE_DISTANCE)

    def up(self):
       if self.head.heading() != DOWN:
           self.head.setheading(UP)

    def down(self):
      if self.head.heading() !=UP :
        self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)
