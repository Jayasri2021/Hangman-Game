import random

def hangman():
    # List of words for the game
    words = ['python', 'hangman', 'computer', 'programming', 'gaming', 'hello', 'world']

    # Choose a random word from the list
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6  # Number of attempts allowed

    print("Welcome to Hangman!")
    print("Try to guess the secret word.")

    while attempts > 0:
        # Display the current state of the word with blanks for unguessed letters
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
        print("Word:", display_word)

        if display_word == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            return

        print("Attempts left:", attempts)
        print("Guessed letters:", ' '.join(guessed_letters))

        user_guess = input("Enter a letter: ").lower()

        # Check if the input is valid
        if not user_guess.isalpha() or len(user_guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if user_guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(user_guess)

        # Check if the guessed letter is in the secret word
        if user_guess not in secret_word:
            attempts -= 1
            print("Wrong guess!")

    print("Out of attempts! The secret word was:", secret_word)
