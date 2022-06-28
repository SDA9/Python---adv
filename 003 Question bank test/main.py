from question_model import Question
from data import question_data

i = 0

question_bnk = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bnk.append(new_question)

for que in question_data:
    print(f"The question is: {question_bnk[i].text}")
    print(f"The answer is: {question_bnk[i].text}")
    i += 1
