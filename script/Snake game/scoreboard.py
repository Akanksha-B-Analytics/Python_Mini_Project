# Scoreboard Class
# A Turtle Graphics-based scoreboard for the Snake
# Game that displays the current score, updates it
# whenever the player earns points, and shows a game
# over message when the game ends. This project
# demonstrates object-oriented programming and text
# rendering with Turtle Graphics.

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        self.score = 0
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("OHHH NOO !!! GAME OVER", align=ALIGNMENT, font=FONT)

