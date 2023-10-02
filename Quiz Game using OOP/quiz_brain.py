class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_number+1
        self.question_number += 1
        question = self.question_list[current_question].text
        choice = input(f"Q.{current_question}. {question} (True/False)? ")
        self.check_answer(choice, self.question_list[current_question].answer)
    def still_has_questions(self):
        return  self.question_number < len(self.question_list)

    def check_answer(self, user_choice, correct_answer):
        score = 0
        if user_choice.lower() == correct_answer.lower():
            print("It was correct.")
            self.score+=1
            print("You scored: 1/1")
        else:
            print("wrong")
            print("You scored: 0/1")
        print(f"Correct answer: {correct_answer}")
        print(f"You total score: {self.score}/{self.question_number}")
        print("\n")
