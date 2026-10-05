# Snake Game Main Controller
# The core file of a Snake Game built with Python
# Turtle Graphics. It manages the game loop, user
# controls, collision detection, score updates, food
# spawning, and game-over conditions. This project
# demonstrates object-oriented programming, event
# handling, animation, and game development concepts.


from turtle import  Screen
from scoreboard import Scoreboard
from snake import Snake
import time
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)
screen.bgcolor("black")

calling_snake = Snake()
calling_snake.create_snake()

food= Food()
scoreboard= Scoreboard()
screen.listen()
screen.onkey(calling_snake.up,"Up")
screen.onkey(calling_snake.down,"Down")
screen.onkey(calling_snake.left,"Left")
screen.onkey(calling_snake.right,"Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    calling_snake.move()
  ##detect collision with food
    if calling_snake.head.distance(food) < 20:
        food.refresh()
        calling_snake.extend_snake()
        scoreboard.increase_score()
    #detect collision with wall
    if calling_snake.head.xcor() >290 or calling_snake.head.xcor() < -290 or calling_snake.head.ycor() > 290 or calling_snake.head.ycor() < -290:
        is_game_on = False
        scoreboard.game_over()
    #detect collision with tail
    for segment in calling_snake.all_turtles[1:]:

        if calling_snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()








