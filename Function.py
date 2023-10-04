import random


def hangman():
    list1 = ["python", "hangman", "computer", "programming", "gaming", "hello", "world"]
    sec_word = random.choice(list1)
    guessed = []
    tries = 6
    print("Welcome to Hangman game!")
    print("Try to guess the secret word.")
    while tries > 0:
        dis_word = "".join(
            [letter if letter in guessed else "_" for letter in sec_word]
        )
        print("Word:", dis_word)

        if dis_word == sec_word:
            print("Congratulations! You guessed the word:", sec_word)
            return
