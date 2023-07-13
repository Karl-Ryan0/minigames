import random

def hangman():
    word = "apple"
    guesses = []
    tries = len(word)

    while tries > 0:
        guess = input("Enter your choice:")
        if guess not in guesses:
            guesses.append(guess)
            tries -= 1
            hangman_board = ""
            for letter in word:
                hangman_board += letter
            else:
                hangman_board += "_"
        else:
            print("You already guessed that!")
hangman()
