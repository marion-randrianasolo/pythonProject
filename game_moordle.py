from moordle import Moordle
import random


def main():
    question_set = Moordle.load_question_set("quiz.py")

    # print(question_set)
    lyrics = random.choice(list(question_set))
    # print("lyrics : ", lyrics)
    title = question_set.get(lyrics)
    # print("title : ", title)

    print("Hello Moordle!")

    moordle = Moordle(title)

    while moordle.can_attempt:

        print("What song are these lyrics from ? : ", lyrics)

        guess = input("Type your guess : ")
        guess = guess.upper()
        moordle.attempt(guess)

        if title == guess:
            print("Slay")
        else:
            print("Nope")

    print("The answer is : ", title)  # put after when attempts > 5
    print("---------")


if __name__ == '__main__':
    main()
