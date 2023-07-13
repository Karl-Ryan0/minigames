import random

def hangman():

    word = "apple"
    guesses = []
    tries = len(word)

    while tries > 0:
        guess = input("Enter your choice:")
        if len(guess) == 1:
            if guess not in guesses:
                guesses.append(guess)
                print(guesses)
                tries -= 1
                hangman_board = ""
                for letter in word:
                    if letter in guesses:
                        hangman_board += letter
                    else:
                        hangman_board += "_"
            else:
                print("You already guessed that!")
        else:
            print("You cannot enter more than one letter!")
        print(hangman_board)
        print(f'You have {tries} tries remaining')

hangman()
