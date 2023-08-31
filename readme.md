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

### External Testing
* My code was sent to friends and family for feedback and testing.
* All user input is error checked to prevent improper input from the user.
* As the game was built using a Windows 11 PC, the majority of the testing was done using this machine and VS Code on gitpod, as well as on Heroku.

### Internal Testing / Bugs found
Code was mostly tested on VS Code and PythonTutor with regular PEP8 checks.

#### Hangman
* Case sensitivity
  * Initially the game was case sensitive and a user could fail for trying to spell BANANA instead of banana. There's a check implemented that will force the user input to lowercase, preventing this.
* Use of special characters and numbers
  * These were allowed initially and I could add them as my guess. This would not crash the game as it was not looking for anything specific, but it would cost the user a guess. This was corrected by using a catchall if statement to ensure the entry was a letter.
* Multiple characters
  * If a user attempted to enter multiple characters, the game would initially interpret the first letter as the guess, for example 'potato' would return 'p' as the guess. I couldn't figure out why this was, so instead of investigating it and trying to make a single word solve the puzzle, I added it to the above catchall.

#### Memory
* Display issues
  * Initally the game would not attempt to clear the screen and would constantly display the number in question, making the game almost impossible to lose. This was rectified by adding the clear function, which resulted in another error below.
* Nothing on screen
  * After resolving the above, now the code executed as intended, but wiped the screen instantly, meaning that the user would never actually see the number that was generated, making the game impossible to solve. This was countered by adding a timer that would clear the screen after 2 seconds, allowing the player to see the number before it disappeared.

#### Adventure
* Repeating patterns
  * At first the game would allow the same actions to be taken over and over again which would still display the same text, possibly making the player think that they had several of the same item. This was resolved with a simple check for variables when a player takes an action and respond appropriately if the player has already done this. For example, instead of finding a gun in the bookshelf over and over, the player will be told that there is nothing therre anymore.
* Variables between areas
  * Because variables were initially defined in the subfunctions, they would not carry over between other subfunctions and this would cause the game to crash. For example, the gun is needed to get the good ending, but the check in room 2 did not know of any variables and this would cause the game to hang. I had to use nonlocal on the variables to prevent this from happening.

#### General
* Game running constantly
  * Initially there was no way to leave a game that had been started. Added a listener for the word 'exit' converted to lowercase to allow the player to leave the game. On top of this, the game would just stop on completion and need to be restarted, this was resolved using a simple endgame function that will stop the code running.

## Deployment
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