# from main import question_bank
# from data import question_data
# from main import answers
class QuizBrian:
    def __init__(self,question_list):
        self.question_no = 0
        self.scores =0
        self.question_list = question_list
    def still_have_question(self):
        return len(self.question_list) > self.question_no
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no +=1
        user_answer=input(f"Q.{self.question_no}{current_question.text} (True/False)")
        self.check(user_answer,current_question.answer)
    def check(self,user_answer,currect_answer):
        if user_answer.lower() == currect_answer.lower():
            self.scores += 1
            print("you Right")
        else:
            print("Wrong Answer")
        print(f"Currect answer{currect_answer}")
        print(f"{self.scores}/{self.question_no}")
        print("\n")
