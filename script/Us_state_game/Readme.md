# U.S. States Guessing Game

An interactive geography game built with Python, Turtle Graphics, and Pandas. Test your knowledge of U.S. geography by identifying all 50 states on a blank map of the United States.

## Features

- Interactive map of the United States
- Guess all 50 U.S. states
- Displays correctly guessed state names on the map
- Tracks your progress as you play
- Saves unguessed states to a CSV file
- Helps improve geography knowledge

## Technologies Used

- Python 3
- Turtle Graphics
- Pandas
- CSV File Handling

## Project Structure

```text
us-states-game/
│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
├── states_to_learn.csv
└── README.md
```

**File descriptions:**

- `main.py` — Contains the main game logic.
- `50_states.csv` — Stores the names and coordinates of the 50 U.S. states.
- `blank_states_img.gif` — Provides the blank map used in the game.
- `states_to_learn.csv` — Stores the names of states you have not guessed yet.
- `README.md` — Documents the project.

## Requirements

Make sure Python 3 is installed on your computer.

Install Pandas using pip:

```bash
pip install pandas
```

The Turtle module is included with most standard Python installations.

## How to Run

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the project directory:

```bash
cd us-states-game
```

3. Run the Python script:

```bash
python main.py
```

## How to Play

1. Launch the game to display the blank map of the United States.
2. Enter the name of a U.S. state in the input box.
3. If your answer is correct, the state's name appears at its location on the map.
4. Continue guessing until you identify all 50 states.
5. Type `Exit` to end the game early.
6. The program saves the states you missed in `states_to_learn.csv`.

## Learning Objectives

This project demonstrates practical applications of:

- Python loops and conditional statements
- Lists and list operations
- Data manipulation using Pandas
- Reading CSV files
- Creating and exporting DataFrames
- Turtle Graphics and screen interaction
- Working with coordinates
- User input and progress tracking

## Future Improvements

- Add a timer to make the game more challenging.
- Display the final score and completion percentage.
- Add hints for difficult states.
- Allow players to review previously missed states.
- Add different difficulty levels.

## Author

Created as a Python learning project to practice data analysis, file handling, and graphical programming.
