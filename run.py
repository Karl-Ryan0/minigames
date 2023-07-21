import random
import os
import time
import string

def clear():
    """
    This will clear the screen and prevent the player from seeing the answer in memory permanently.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def delay_text(text, delay=1):
    """
    This delay text transitioning inside the games.
    """
    time.sleep(delay)
    print(text)


def hangman():
    """
    This is a hangman game the player can choose to play.
    There are a few words programmed in.
    The user has to guess what the word is from the list, and only has so many guesses to get it correct.
    """
    words = ["apple", "banana", "cherry", "orange", "pear", "grape", "watermelon", "strawberry", "avocado", "peach", "blackberry"]
    word = random.choice(words)
    guesses = []
    hangman_board = "_" * len(word)
    tries = len(word) + 2
    delay_text(f'Welcome to hangman! You have {tries} tries to guess the word. You win if you unmask the whole word, and fail if you run out of lives. Good luck!')

    # This continues the game until the player is out of lives.
    while tries > 0:
        guess = input("Enter your choice:").lower()
        # This will end the game if the player chooses.
        if guess == "exit":
            return
        try:
            # Check if the input is a single letter and is an alphabet character.
            if len(guess) == 1 and guess.isalpha():
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
                delay_text("Please enter a single letter!")
        except ValueError:
            delay_text("Invalid input! Please enter a single letter.")

        delay_text(hangman_board)
        delay_text(f'You have {tries} tries remaining')
        # This is the win condition
        if hangman_board == word:
            delay_text(f'Congratulations! You guessed the word {word} correctly!')
            break
    # This is the lose condition
    if tries == 0:
        delay_text(f'Sorry, you did not guess the word! The word was {word}.')


def adventure():
    key1_have = False
    gun_have = False
    delay_text("Welcome to the adventure game! You wake up in a strange room.")

    def room_one():
        nonlocal key1_have
        nonlocal gun_have
        delay_text(
            "You look around and see a door to the right, a door to the left, a bookshelf, and a cabinet.")
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




def memory():
    # Initialize player's lives and the first sequence to memorize
    lives = 3
    sequence = str(random.randint(1, 9))

    # Welcome message and instructions
    print("Welcome to the memory game!")
    print("You'll be presented with a progressively harder number, and only two seconds to memorize it. Good luck!")
    time.sleep(10)

    # Main game loop
    while lives > 0:
        # Display the current sequence to memorize
        print(sequence)
        time.sleep(2)
        clear()
        while True:
            entry = input("Guess here (or type 'exit' to quit): ")
            if entry.lower() == "exit":
                return
            try:
                # Check if the input is a number (digit)
                int(entry)
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

        # Check if the guess is correct
        if entry == sequence:
            print("Correct! Moving to the next level")
            time.sleep(2)
            # Generate the next sequence by adding another digit
            sequence += str(random.randint(1, 9))
        else:
            print("Wrong guess!")
            time.sleep(2)
            lives -= 1

    # Game over message
    print("Game over! You ran out of lives.")




def main():
    while True:
        choice = input(
            "Make your choice. You can choose between hangman, adventure or memory: ").lower()
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


hangman()
