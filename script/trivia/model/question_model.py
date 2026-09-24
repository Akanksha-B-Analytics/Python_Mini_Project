# Question class represents a single quiz question.
# Stores the question text and its correct answer.
# Used to convert raw dictionary data into Question objects.

class Question:
    def __init__(self,q_text,q_answer):
        self.text = q_text
        self.answer = q_answer
