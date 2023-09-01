import random

import random

class Word:
    """
    A class representing a word to be guessed in the Hangman game.

    Attributes:
    - words (list): a list of words to be randomly chosen from
    - current_word (str): the word to be guessed
    - guessed_letters (list): a list of letters that have been guessed correctly

    Methods:
    - check_guess(guess): checks if the guessed letter is in the current word
    - is_word_complete(): checks if all letters in the current word have been guessed
    """

    def __init__(self):
        """
        Initializes a new instance of the Word class.
        """
        self.words = ["example", "hangman", "python", "programming"]
        self.current_word = random.choice(self.words)
        self.guessed_letters = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the current word.

        Args:
        - guess (str): the letter guessed by the player

        Returns:
        - True if the guessed letter is in the current word, False otherwise
        """
        if guess in self.current_word:
            self.guessed_letters.append(guess)
            return True
        return False

    def is_word_complete(self):
        """
        Checks if all letters in the current word have been guessed.

        Returns:
        - True if all letters in the current word have been guessed, False otherwise
        """
        for letter in self.current_word:
            if letter not in self.guessed_letters:
                return False
        return True