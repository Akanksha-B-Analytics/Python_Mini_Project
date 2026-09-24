# Entry point of the quiz application.
# Initializes question objects, creates the quiz controller,
# and starts the quiz execution from beginning to end.

from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain

### made a list of object
question_bank=[]
for question in question_data:
    question_text= question["question"]
    question_answer= question["correct_answer"]
    new_question= Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = Quiz_brain(question_bank)##Calling first function __init__
while quiz.still_has_question():
       quiz.next_question()## calling 2nd function

       print(quiz.check_answer())
