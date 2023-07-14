import random

import time

def delay_text(text, delay = 1):
    time.sleep(delay)
    print(text)

def hangman():

    words = ["apple", "banana", "cherry", "orange", "pear"]
    word = random.choice(words)
    guesses = []
    tries = len(word) +2
    delay_text(f'Welcome to hangman! You have {tries} tries to guess the word. You win if you unmask the whole word, and fail if you run out of lives. Good luck!')

    while tries > 0:
        guess = input("Enter your choice:").lower()
        if guess == "exit":
            return
        if len(guess) == 1:
            if guess not in guesses:
                guesses.append(guess)
                delay_text(guesses)
                if guess not in word:
                    tries -= 1
                hangman_board = ""
                for letter in word:
                    if letter in guesses:
                        hangman_board += letter
                    else:
                        hangman_board += "_"
            else:
                delay_text("You already guessed that!")
        else:
            delay_text("You cannot enter more than one letter!")
        delay_text(hangman_board)
        delay_text(f'You have {tries} tries remaining')

        if hangman_board == word:
            delay_text(f'Congratultions! You guessed the word {word} correctly!')
            break

    if tries == 0:
        delay_text(f'Sorry, you did not guess the word! The word was {word}.')

def adventure():
   delay_text("Welcome to the adventure game! You wake up in a strange room.")
   delay_text("You look around and see a door to the right, a door to the left, a bookshelf, and a cabinet.")
   delay_text("What would you like to do?") 
   return


def main():
    while True:
        choice = input("Make your choice. You can choose between hangman, adventure or memory: ").lower()
        if choice == "hangman":
            delay_text("Loading Hangman game...")
            hangman()
            break
        elif choice == "adventure":
            delay_text("Loading Adventure game...")
            adventure()
            break
        elif choice == "memory":
            delay_text("Memory chosen")
            break
        else:
            delay_text("Not a valid selection!")
main()