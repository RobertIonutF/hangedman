
# Hangman Game

This project is a simple implementation of the classic Hangman game using the `pygame` library.

## Files Overview:

1. **main.py**: This is the entry point to initiate the game.
2. **game.py**: Contains the `Game` class that manages the game logic and controls the flow.
3. **display.py**: Contains the `Display` class responsible for managing the visual elements of the game.
4. **player.py**: Represents a player in the game. It has an older method to get input from the user, which seems to be unused in the main game loop.
5. **word.py**: Represents a word to be guessed in the game. It has a predefined list of words from which one is chosen randomly each game.

## How to Use:

1. Ensure you have `pygame` installed. If not, you can install it using pip:
```
pip install pygame
```
2. Run the `main.py` script to start the game.
```
python main.py
```
3. Follow on-screen instructions. Click on letters to make guesses.

## How to Adjust:

1. **Adding More Words**: If you want to add more words to the game, you can simply append to the `words` list in the `Word` class inside the `word.py` file.
2. **Change Display Settings**: You can modify the display settings, colors, and fonts in the `Display` class inside the `display.py` file.
3. **Game Logic**: If you want to change the game rules or logic, you'd mostly be working with the `Game` class inside the `game.py` file.

## Note:

The `guess` method in the `Player` class (inside `player.py`) is an older/alternative way of getting input from the user and seems to be unused in the main game loop. You might want to either integrate it or remove it based on your needs.

Enjoy playing!

modify the game logic or add new features, most of the core game logic is found in the `Game` class in the `game.py` file.

4. **Player Input**: Although the game currently relies on mouse clicks for input, if you'd like to revert to or implement keyboard-based input, the `Player` class in the `player.py` file contains a method for this. You'd need to integrate this method into the game loop.

5. **Graphics and Animations**: Enhancements related to graphics, animations, or additional visual effects can be made in the `Display` class in the `display.py` file using `pygame` functionalities.

## Contribution:

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. All contributions are welcome!

## License:

This project is open-source and available under the MIT License.

## Author:

[Your Name Here]

