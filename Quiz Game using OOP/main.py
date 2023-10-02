from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(item['question'],item['incorrect_answers'][0])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the game.")
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")
