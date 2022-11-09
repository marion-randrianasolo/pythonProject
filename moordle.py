from quiz import questions


class Moordle:
    MAX_ATTEMPTS = 6
    WORD_LENGHT = 5

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        pass

    def attempt(self, word: str):
        self.attempts.append(word)

    def check_answer(answer, guess):
        if answer == guess:
            print("CORRECT!")
            return 1
        else:
            print("WRONG!")
            return 0

    def load_question_set(path: str):
        with open(path, "r"):
            for key in questions:
                key, questions.get(key)
        return questions

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
        pass
