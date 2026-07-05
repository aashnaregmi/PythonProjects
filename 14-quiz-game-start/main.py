from data import question_data
class Question:
      def __init__(self,question,ans):
            self.que=question
            self.ans=ans
      def askquestion(self):
            user_ans=input(f"{self.que} : ")
            if user_ans==self.ans:
               print("You are correct")
            else:
              print("You are not correct")
            
            
            
q1=Question(question_data[0]["text"],question_data[0]["answer"])
q1.askquestion()
