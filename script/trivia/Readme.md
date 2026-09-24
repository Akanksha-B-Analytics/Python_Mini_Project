Hope you enjoy playing it as much as enjoy making it :)

# Trivia Quiz Application

A command-line quiz application developed in Python using Object-Oriented Programming (OOP) principles. The program presents a series of True/False questions, evaluates user responses, tracks scores, and displays the final result upon completion.

## Features

- Interactive command-line quiz experience
- Object-oriented design using classes and objects
- Automatic score tracking
- Question progression management
- Modular and maintainable project structure
- Separation of data, logic, and application flow

## Project Structure

```
trivia/
│
├── data/
│   └── data.py
│
├── models/
│   ├── question_model.py
│   └── quiz_brain.py
│
├── main.py
└── README.md
```

## Components

### data.py
Contains the quiz question dataset and serves as the data source for the application.

### question_model.py
Defines the Question class used to create question objects that store question text and correct answers.

### quiz_brain.py
Manages the quiz flow, handles user input, validates answers, tracks scores, and controls question progression.

### main.py
Acts as the entry point of the application. It initializes required objects and starts the quiz execution.

## Workflow

1. Question data is loaded from `data.py`.
2. Each question is converted into a `Question` object.
3. All question objects are stored in a question bank.
4. A `QuizBrain` object is created to manage the quiz.
5. Questions are displayed one by one.
6. User answers are validated and scores are updated.
7. Final score is displayed after all questions are completed.

## OOP Concepts Demonstrated

- Classes and Objects
- Constructors (`__init__`)
- Encapsulation
- Object Composition
- Modular Programming

## How to Run

```bash
python main.py
```

## Sample Output

```
Q.1: Nova Scotia is on the east coast of Canada. (True/False): True

Correct!
Your current score: 1/1
```

## Author

Developed as a Python mini project to practice Object-Oriented Programming concepts, class design, and application structuring in Python.
