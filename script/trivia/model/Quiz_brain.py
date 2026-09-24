
# Manages the overall quiz functionality.
# Handles question progression, user responses,
# answer validation, and score tracking throughout the quiz.



class Quiz_brain:
##object list se bus que ko nikalne ke liye pehela function
  #1st function
  def __init__(self,q_list):
      self.question_no=0
      self.question_list=q_list
      self.score=0

###2nd fuction
  def next_question(self):
      self.current_question = self.question_list[self.question_no] ##object ki list aa rahi
      self.question_no+=1
      self.ans = input(f"Q.{self.question_no} {self.current_question.text}")
    
##3rd function
  def still_has_question(self):
    return self.question_no < len(self.question_list) ##3<5 return true
                                                      ##6<5 return false
  
#4th function
  def check_answer(self):

      if str(self.ans).lower() == str(self.current_question.answer).lower():
          self.score += 1
          return f"Correct, your score is  {self.score}"
      else:
          self.score
          return f"Wrong, your score is  {self.score}"
