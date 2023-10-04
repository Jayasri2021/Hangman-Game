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

        print("Attempts left:", tries)
        print("Guessed letters:", " ".join(guessed))

        u_guess = input("Enter a letter: ").lower()
        if not u_guess.isalpha() or len(u_guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if u_guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(u_guess)

        if u_guess not in sec_word:
            tries -= 1
            print("Wrong guess!")

    print("Out of attempts! The secret word was:", sec_word)
