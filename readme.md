## Minigames
This repository contains three text-based minigames implemented in Python. The games are designed to be simple and fun, suitable for beginners and those who enjoy casual gameplay.

![The opening screen](/assets/images/opening.png)

## Games

### Hangman
![Hangman](/assets/images/hangman.png)

In this game, you have to guess the hidden word within a limited number of tries. Each incorrect guess results in losing a life, and you win by unmasking the entire word. Be careful, though, as running out of lives means game over!

This has been tester for errors. If a user inputs a number, special character or multiple characters in a single guess, the user is alerted to the mistake and allowed to continue the game without the code breaking.

Words are pulled randomly from a simple array for demonstration purposes, and the amount of guesses allowed is the length of the word plus 2.

### Adventure
![Adventure](/assets/images/adventure.png)

Welcome to a mysterious adventure game! You wake up in a strange room and have to explore your surroundings to find items that may help you progress through the game. Make choices wisely, as your decisions will determine the outcome of your adventure.

There is only one clear way to win this game and it does rely on a bit of trial and error from the player, hopefully leading to replayability. All other scenarios end with the player losing and the character dying in various ways.

Error tested, so that any invalid inputs will alert the user without breaking the game.

### Memory
![Memory](/assets/images/memory.png)

Test your memory skills in this fast-paced game. A sequence of numbers will be shown, and you have only two seconds to memorize it. Afterward, you'll be asked to recall the sequence correctly to move to the next level. Each successful round increases the difficulty, so stay focused!

The sequence pulls a random number from 0-9 and adds it to the current number, increasing the numbers by one without changing the previous number to aid in difficulty.

Error tested for letters or special characters.

### User Suggestions
* I would like to be able to exit whenever I want.
  * 'exit' can be typed at any point in the game to quit.
* I would like the hangman game to stop allowing me to make the same guess.
  * This was done using a simple array that captures the user guesses and checks after every guess.
* I would like for the adventure game to stop me repeating actions.
  * Implemented checks to respond if user has already acquired items etc.
* I would like to know how long the string is in the memory game.
  * Not enough time to implement, planned for future revision.
* I would like an inventory display system for the adventure game.
  * This was suggested and will possibly be implemented in future.
* I would like a walkthrough for the adventure game.
  * No, play the game! :)

## Features


### Design
The games are designed to be pick up and play, mostly using interpretations of games that are readily accessible and that the majority of users would be experienced with already. With the adventure game it will repeat the current options in case the user forgets what they're doing.

Among the games included I had hoped to implement a battleship style game, as well as a card match game, but due to time and knowledge restraints, these were ultimately scrapped.

### Technologies Used
* Python 3.8

## Testing
### Validation
* Tested against PEP8 validation for compliance. Several errors around indentation found but these were minor and corrected easily.

### Testing
* My code was sent to friends and family for feedback and testing.
* All user input is error checked to prevent improper input from the user.
* As the game was built using a Windows 11 PC, the majority of the testing was done using this machine and VS Code on gitpod, as well as on Heroku.

## Bugs Found
### Hangman:

* Some words in the word list were too short, causing quick game completions.
  * Solution: Improved the word selection algorithm to ensure a variety of word lengths.
* Issue: The "exit" command didn't work as expected during the game.
  * Solution: Corrected the code to handle the "exit" command and gracefully end the game.
### Adventure:

* The player could access locked rooms without the required items.
  * Added proper checks for inventory items before granting access to certain rooms.
* Certain actions did not update the inventory status correctly.
  * Fixed the inventory update logic to reflect changes accurately.
## Memory:

* The game did not handle invalid input (non-numeric) properly.
  * Implemented a try-except block to catch invalid inputs and prompt the player to enter a number.


### Deployment
1. Navigate to [https://github.com/Karl-Ryan0/minigames](https://github.com/Karl-Ryan0/minigames).
2. You can set up your own repository and copy or clone it, or you fork the repository.
3. `git add`, `git commit` and `git push` to a GitHub repository, if necessary.
4. GitHub pages will update from the master branch by default.
5. Go to the **Settings** page of the repository.
6. Scroll down to the **Github Pages** section.
7. Select the Master Branch as the source and **Confirm** the selection.
8. Wait a minute or two and it should be live for viewing.

Alternatively, the game can be played by navigating to [Heroku](https://minigames-0919640b8832.herokuapp.com/s) where the game is deployed.


### Credits
* All code was freehand however additional thanks for the people at Mammoth Interactive and CI for the great tutorials.
* Images on this readme are my own screenshots.

https://minigames-0919640b8832.herokuapp.com/