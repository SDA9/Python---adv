from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

import os


def clear_console(): return os.system('cls')


question_bnk = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bnk.append(new_question)

quiz = QuizBrain(question_bnk)

while quiz.still_has_que():
    quiz.next_question()

clear_console()
print("""                                      
                        88            
                        ""                        
 ,adPPYb,d8 88       88 88 888888888  
a8"    `Y88 88       88 88      a8P"  
8b       88 88       88 88   ,d8P'    
"8a    ,d88 "8a,   ,a88 88 ,d8"       
 `"YbbdP'88  `"YbbdP'Y8 88 888888888  
         88                           
         88                           """)
print("\nYou have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.number} [{round((quiz.score/12)*100,2)}%]")
