## Minigames
This repository contains three text-based minigames implemented in Python. The games are designed to be simple and fun, suitable for beginners and those who enjoy casual gameplay.

### Games
Hangman: In this game, you have to guess the hidden word within a limited number of tries. Each incorrect guess results in losing a life, and you win by unmasking the entire word. Be careful, though, as running out of lives means game over!

Adventure: Welcome to a mysterious adventure game! You wake up in a strange room and have to explore your surroundings to find items that may help you progress through the game. Make choices wisely, as your decisions will determine the outcome of your adventure.

Memory: Test your memory skills in this fast-paced game. A sequence of numbers will be shown, and you have only two seconds to memorize it. Afterward, you'll be asked to recall the sequence correctly to move to the next level. Each successful round increases the difficulty, so stay focused!

Users are able to:
* Battle monsters
* Plan a strategy
* Earn bonuses
* Make different types of attack

### User Suggestions
1. I would like some animation
2. I would like different monsters
3. I would like a visual to see what is happening
4. I would like to be able to change difficulty

## Features


## Design



## Technologies Used
* Python 3.8

## Testing
### Validation
* HTML tested with W3C HTML5 Validator every day.
* CSS has been validated with W3C CSS Validator every day or major change.

### Testing
* My code was sent to friends and family for feedback and testing.
* All user input is error checked to prevent improper input from the user.
* As the site was built using a Windows 11 PC, the majority of the testing was done using this machine and VS Code on gitpod..

### Bugs Found
## Hangman:

Issue: Some words in the word list were too short, causing quick game completions.
Solution: Improved the word selection algorithm to ensure a variety of word lengths.
Issue: The "exit" command didn't work as expected during the game.
Solution: Corrected the code to handle the "exit" command and gracefully end the game.
## Adventure:

Issue: The player could access locked rooms without the required items.
Solution: Added proper checks for inventory items before granting access to certain rooms.
Issue: Certain actions did not update the inventory status correctly.
Solution: Fixed the inventory update logic to reflect changes accurately.
## Memory:

Issue: The game did not handle invalid input (non-numeric) properly.
Solution: Implemented a try-except block to catch invalid inputs and prompt the player to enter a number.


### Deployment
1. Navigate to [https://github.com/Karl-Ryan0/minigames](https://github.com/Karl-Ryan0/minigames).
2. You can set up your own repository and copy or clone it, or you fork the repository.
3. `git add`, `git commit` and `git push` to a GitHub repository, if necessary.
4. GitHub pages will update from the master branch by default.
5. Go to the **Settings** page of the repository.
6. Scroll down to the **Github Pages** section.
7. Select the Master Branch as the source and **Confirm** the selection.
8. Wait a minute or two and it should be live for viewing.




### Credits
* All code was freehand however additional thanks for the people at Mammoth Interactive and CI for the great tutorials.