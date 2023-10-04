import random


def hangman():
    list1 = ["python", "hangman", "computer", "programming", "gaming", "hello", "world"]
    sec_word = random.choice(list1)
    guessed = []
    tries = 6
    print("Welcome to Hangman game!")
    print("Try to guess the secret word.")
