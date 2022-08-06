import random
from data import question_data
from question import Question
from quiz_braine import QuizBrain

question_bank = list()
for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

start = True
while start:
    random.shuffle(question_bank)
    qz = QuizBrain(question_bank)
    while qz.still_has_questions():
        user_ans = qz.next_question()
        if qz.ans_check(user_ans):
            print('correct answer')
            qz.score_function()
            print(f'your current score is {qz.score}')
        else:
            print('your answer is wrong')
            print(f'your current score is {qz.score}')
    start = input("c for continue and any for exit :").lower()
    if start != 'c':
        start = False


