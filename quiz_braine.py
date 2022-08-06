class QuizBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        self.question_no += 1
        current_question = self.question_list[self.question_no-1]
        current_question.question
        return input(f"{self.question_no}.{current_question.question} true/false\n").lower()

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def ans_check(self, user_choice):
        return user_choice == self.question_list[self.question_no-1].ans.lower()

    def score_function(self):
        self.score += 1
