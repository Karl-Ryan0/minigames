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
    key1_have = False
    gun_have = False
    delay_text("Welcome to the adventure game! You wake up in a strange room.")
    def room_one():
        nonlocal key1_have
        nonlocal gun_have
        delay_text("You look around and see a door to the right, a door to the left, a bookshelf, and a cabinet.")
        delay_text("What would you like to do?") 
        delay_text("1. Open the door to the left")
        print("2. Open the door to the right")
        print("3. Check the bookshelf")
        print("4. Check the cabinet")
        print("5. Wait around to see what happens")

        while True:
            adventure_choice = input(" Enter 1, 2, 3, 4 or 5:")
            if adventure_choice == "1":
                key1_have = True
                delay_text("You find a key")
                delay_text(key1_have)
                return
            elif adventure_choice == "2":
                if key1_have == False:
                    delay_text("This door is locked")
                    return
                else:
                    delay_text("You find another room")
                    return
            elif adventure_choice == "3":
                gun_have = True
                delay_text("You find a gun in the bookshelf")
                return
            elif adventure_choice == "4":
                delay_text("Nothing here")
                return
            elif adventure_choice == "5":
                wait_in_room()
            else:
                print("Please enter a valid selection:")
    
    def wait_in_room():
        delay_text("You wait in the room for 5 minutes. Nothing happens.")
        room_one()
    
    room_one()


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
adventure()