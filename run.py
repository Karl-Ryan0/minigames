import random

def hangman():
    word = "apple"
    guesses = []
    tries = len(word)

    while tries > 0:
        guess = input("Enter your choice:")
        print(f'You guessed {guess} and have {tries} tries left')
        tries -= 1

hangman()
