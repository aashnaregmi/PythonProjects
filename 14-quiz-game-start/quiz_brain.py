from data import question_data

      
class QuizBrain:
    def __init__(self,q_list):
      self.question_no=0
      self.q_list=q_list
      self.score=0
    def still_has_question(self):
      return self.question_no<len(self.q_list)
       
        
    def check_answer(self,user_ans,correct_ans):
      if user_ans.lower()==correct_ans.lower():
         print("You got it right")
         self.score += 1
      else:
        print("You are wrong")
      print(f"The correct ans is {correct_ans}")
      print(f"Your score is {self.score}/{self.question_no}")
       
    def askque(self):
      question=self.q_list[ self.question_no].que
      correct_ans=self.q_list[ self.question_no].ans
      self.question_no+=1
      user_ans=input(f"Q{self.question_no}:{question} ")
      self.check_answer(user_ans,correct_ans)
      
    
        
        
      
      
      
      
      