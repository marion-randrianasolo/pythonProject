from quiz import questions


class Moordle:

    # Maximum attempts for a question
    MAX_ATTEMPTS = 6

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        pass

    # Attemps to guess
    def attempt(self, word: str):
        self.attempts.append(word)

    # Load data from a py file
    def load_question_set(path: str):
        with open(path, "r"):
            for key in questions:
                key, questions.get(key)
        return questions

    # Returns true if the question is solved
    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    # Returns remaining attempts
    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    # Returns true if able to attempt
    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
        pass
