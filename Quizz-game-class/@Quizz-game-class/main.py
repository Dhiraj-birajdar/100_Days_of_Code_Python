from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain
question_bank = []

for i in question_data:
    question_bank.append(Question(i['question'], i['correct_answer']))
    # question_bank.append(Question(i['text'], i['answer']))
    # qn = Question(i['text'], i['answer'])
    # question_bank.append(qn)

# print(question_bank[0].qns)
quizz = QuizzBrain(question_bank)
while quizz.still_has_qn():
    quizz.next_qns()
    print(f"Score = {quizz.score}/{quizz.qnu}\n\n")

print("You've completed quiz 👍")
print(f"Your final score is {quizz.score}/{quizz.qnu}")
