class Player:
    """
    A class representing a player in the hangedman game.
    """
    def guess(self):
        """
        Prompts the player to guess a letter and returns the guessed letter in lowercase.
        """
        letter = input("Guess a letter: ").lower()
        return letter