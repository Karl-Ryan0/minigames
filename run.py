import random
import os
import time
import string
import sys

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
            endgame()
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
            endgame()
    # This is the lose condition
    if tries == 0:
        delay_text(f'Sorry, you did not guess the word! The word was {word}.')


def adventure():
    """
    This is the adventure game. It features a simple inventory system.
    """
    smallkey_have = False
    largekey_have = False
    gun_have = False
    torch_have = False
    delay_text("Welcome to the adventure game! You wake up in a strange room.")

    def room_one():
        """
        This is the entry room for the game.
        """
        nonlocal smallkey_have
        nonlocal largekey_have
        nonlocal gun_have
        nonlocal torch_have

        delay_text("You look around and see a door to the right, a door to the left, a bookshelf, and a cabinet.")
        delay_text("What would you like to do?")
        delay_text("1. Open the door to the left")
        print("2. Open the door to the right")
        print("3. Check the bookshelf")
        print("4. Check the cabinet")
        print("5. Wait around to see what happens")

        while True:
            adventure_choice = input(" Enter 1, 2, 3, 4 or 5, or 'exit' to quit:")
            # This handles the first player choice.
            if adventure_choice == "1":
                if smallkey_have == False:
                    smallkey_have = True
                    delay_text("You open the door on the right. This room is bare except for a small key.")
                    delay_text("You take the small key and return to the main room.")
                    room_one()
                else:
                    delay_text("This room is now empty")
                    room_one()
            # This handles the second player choice.
            elif adventure_choice == "2":
                if smallkey_have == False:
                    delay_text("This door is locked")
                    room_one()
                else:
                    room_two()
            # This handles the third player choice.
            elif adventure_choice == "3":
                if gun_have == True:
                    delay_text("There's nothing here anymore.")
                    room_one()
                else:
                    gun_have = True
                    delay_text("You find a gun in the bookshelf.")
                    room_one()
            # This handles the fourth player choice.
            elif adventure_choice == "4":
                if torch_have == True:
                    delay_text("There's nothing here anymore.")
                    room_one()
                else:
                    torch_have = True
                    delay_text("You find a torch in the cabinet.")
                    room_one()
            # This handles the fifth player choice.
            elif adventure_choice == "5":
                wait_in_room()
            # This handles the player quitting the game.
            elif adventure_choice.lower() == "exit":
                endgame()
            else:
                print("Please enter a valid selection:")


    # This handles the player choosing to do nothing.
    def wait_in_room():
        delay_text("You wait in the room for 5 minutes. Eventually the water starts to rise, and you struggle against the doors.")
        delay_text("Your vision starts to fade to black but you lose consiousness.")
        endgame()


    def victory():
        delay_text("Congratulations!")
        delay_text("The monster is defeated, and you have earned your freedom.")
        endgame()


    def room_two():
        """
        This function will determine if the player has enough items. He will need both the gun and torch or he will meet his end.
        """
        nonlocal smallkey_have
        nonlocal largekey_have
        nonlocal torch_have
        nonlocal gun_have
        if torch_have == False:
            delay_text("You step into a cold, dark room. You can't see anything, so you turn to leave.")
            delay_text("However, the door has locked behind you.")
            delay_text("You pull on the handle to no avail.")
            delay_text("As you're struggling, you feel a sickening thump behind you.")
            if gun_have == True:
                delay_text("You fire the gun wildly but to no avail.")
            delay_text("You feel one more blow to the back of the head and start to lose consiousness.")
            endgame()
        else:
            delay_text("You step into a cold, dark room. You can't see anything, so you power on your torch.")
            delay_text("There's something in front of you. Something sinister.")
            delay_text("You turn to the door but it has locked behind you.")
            if gun_have == True:
                delay_text("You open fire on the creature.")
                delay_text("After several misses, one of your rounds finally hits it mark.")
                delay_text("The beast staggers, and finally utters one last cry of pain.")
                delay_text("As it falls, you see a door behind it.")
                last_choice = input("Do you attempt to go through it? y/n")
                if last_choice == "y":
                    victory()
                else:
                    wait_in_room()
            else:
                delay_text("The last thing you hear is the wild howlings of a monster.")
                endgame()
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
                    endgame()
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
    """ 
    This is the main function. It will offer the player with a choice of several minigames to choose from.
    """
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
            delay_text("Loading Memory game")
            memory()
            break
        else:
            delay_text("Not a valid selection!")


def endgame():
    # Simple function to end the game at player request or game over
    delay_text("Thanks for playing!")
    sys.exit()

main()
