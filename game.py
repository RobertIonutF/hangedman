import pygame
from word import Word
from display import Display

import pygame

class Game:
    """
    The Game class represents the game logic and controls the game flow.

    Attributes:
    - word: an instance of the Word class representing the word to be guessed
    - display: an instance of the Display class representing the game display
    """

    def __init__(self):
        """
        Initializes a new instance of the Game class.
        """
        self.word = Word()
        self.display = Display(self.word)

    def play(self):
        """
        Starts the game loop and handles user input.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.display.show()

            if self.word.is_word_complete():
                self.display.show_message("Congratulations! You've guessed the word.", (0, 255, 0))  # Green Color
                pygame.display.flip()
                pygame.time.wait(2000)
                self.word = Word()
                self.display = Display(self.word)
            elif self.display.is_game_over():
                self.display.show_message("Game over! You couldn't guess the word.", (255, 0, 0))  # Red Color
                pygame.display.flip()
                pygame.time.wait(2000)
                self.word = Word()
                self.display = Display(self.word)

            pygame.time.wait(100)

    def handle_click(self, pos):
        """
        Handles a mouse click event.

        Parameters:
        - pos: a tuple representing the position of the mouse click

        Returns:
        - None
        """
        for index, letter in enumerate(self.display.letters):
            letter_pos = self.display.letter_positions[index]
            letter_surface = self.display.letter_font.render(letter, True, self.display.BLACK)
            if letter_surface.get_rect(topleft=letter_pos).collidepoint(pos):
                # Mark the letter as clicked
                self.display.mark_letter_as_clicked(letter)

                # Check if it's a correct guess
                if not self.word.check_guess(letter):
                    self.display.add_wrong_guess()

if __name__ == "__main__":
    game = Game()
    game.play()