# --------------------------------------------------
# Hangman Game
#
# A simple command-line Hangman game built with Python.
# The program randomly selects a word from a predefined
# list, and the player must guess the word one letter
# at a time before running out of lives.
#
# Features:
# - Random word selection
# - Life tracking system
# - ASCII Hangman visualization
# - Win and lose conditions
# - User-friendly text interface
#
# Concepts Used:
# - Variables and Lists
# - Loops (while, for)
# - Conditional Statements
# - String Manipulation
# - Random Module
#
# --------------------------------------------------
import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel","elephant","juice","tomato"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives-= 1
        if lives == 0:
            game_over = True
            print("You lose.")

        print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win.")

