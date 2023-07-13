import random

def hangman():
    word = "apple"
    guesses = []
    tries = 1

    print(f'The word is {word}')
    tries -=1
    print(f'You have {tries} guesses remaining')
hangman()
