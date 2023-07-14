import random

def hangman():

    words = ["apple", "banana", "cherry", "orange", "pear"]
    word = random.choice(words)
    guesses = []
    tries = len(word)

    while tries > 0:
        guess = input("Enter your choice:").lower()
        if guess == "exit":
            return
        if len(guess) == 1:
            if guess not in guesses:
                guesses.append(guess)
                print(guesses)
                if guess not in word:
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

        if hangman_board == word:
            print(f'Congratultions! You guessed the word {word} correctly!')
            break

    if tries == 0:
        print(f'Sorry, you did not guess the word! The word was {word}.')

def main():
    while True:
        choice = input("Make your choice. You can choose between hangman, adventure or memory: ").lower()
        if choice == "hangman":
            hangman()
            break
        elif choice == "adventure":
            print("Adventure chosen")
            break
        elif choice == "memory":
            print("Memory chosen")
            break
        else:
            print("Not a valid selection!")
main()