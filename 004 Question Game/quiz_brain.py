class QuizBrain:
    def __init__(self, que_list):
        self.number = 0
        self.list = que_list
        self.score = 0

    def still_has_que(self):
        return self.number < len(self.list)

    def next_question(self):
        current_que = self.list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current_que.text} (True/ False): ")
        self.check_answer(user_answer, current_que.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Tou got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your score is: {self.score}/12 [{round((self.score/12)*100,2)}%] \n")
