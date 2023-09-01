import pygame

class Display:
    """
    A class used to represent the display of the Hangman game.

    Attributes
    ----------
    screen : pygame.Surface
        the surface of the game window
    WHITE : tuple
        the RGB color code for white
    BLACK : tuple
        the RGB color code for black
    GRAY : tuple
        the RGB color code for gray
    word_font : pygame.font.Font
        the font used for displaying the word to guess
    letter_font : pygame.font.Font
        the font used for displaying the letters to click
    word : Word
        the word to guess
    hangman_parts : int
        the number of parts of the hangman
    wrong_guesses : int
        the number of wrong guesses
    letters : list
        the list of letters to click
    letter_positions : list
        the list of positions for each letter
    clicked_letters : list
        the list of clicked letters

    Methods
    -------
    get_letter_positions()
        Returns the positions for each letter.
    draw_hangman()
        Draws the hangman parts based on the number of wrong guesses.
    draw_word()
        Draws the word to guess with the guessed letters and underscores.
    draw_letters()
        Draws the letters to click with the clicked letters in gray.
    mark_letter_as_clicked(letter)
        Marks the clicked letter as clicked.
    show()
        Shows the display with the hangman, word, and letters.
    is_game_over()
        Returns True if the game is over (all hangman parts are drawn).
    add_wrong_guess()
        Adds a wrong guess to the number of wrong guesses.
    show_message(message, color)
        Shows a message on the screen with the given color.
    """
class Display:
    def __init__(self, word):
        pygame.init()

        # Window Settings
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Hangman Game')

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)

        # Fonts
        self.word_font = pygame.font.SysFont(None, 36)
        self.letter_font = pygame.font.SysFont(None, 48)

        # Word and Hangman settings
        self.word = word
        self.hangman_parts = 6  
        self.wrong_guesses = 0

        # Letters and their positions
        self.letters = [chr(x) for x in range(97, 123)]  # a to z
        self.letter_positions = self.get_letter_positions()
        self.clicked_letters = []

    def get_letter_positions(self):
        positions = []
        startX, startY = 50, 550
        gap = 35
        for index, letter in enumerate(self.letters):
            x = startX + index * gap
            positions.append((x, startY))
        return positions

    def draw_hangman(self):
        if self.wrong_guesses > 0:
            pygame.draw.circle(self.screen, self.BLACK, (400, 150), 50)  # Head
        if self.wrong_guesses > 1:
            pygame.draw.line(self.screen, self.BLACK, (400, 200), (400, 350), 5)  # Body
        if self.wrong_guesses > 2:
            pygame.draw.line(self.screen, self.BLACK, (400, 220), (350, 300), 5)  # Left arm
        if self.wrong_guesses > 3:
            pygame.draw.line(self.screen, self.BLACK, (400, 220), (450, 300), 5)  # Right arm
        if self.wrong_guesses > 4:
            pygame.draw.line(self.screen, self.BLACK, (400, 350), (350, 450), 5)  # Left leg
        if self.wrong_guesses > 5:
            pygame.draw.line(self.screen, self.BLACK, (400, 350), (450, 450), 5)  # Right leg

    def draw_word(self):
        display_word = ""
        for letter in self.word.current_word:
            if letter in self.word.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        text = self.word_font.render(display_word, True, self.BLACK)
        self.screen.blit(text, (100, 500))

    def draw_letters(self):
        for index, letter in enumerate(self.letters):
            color = self.BLACK if letter not in self.clicked_letters else self.GRAY
            text = self.letter_font.render(letter, True, color)
            self.screen.blit(text, self.letter_positions[index])

    def mark_letter_as_clicked(self, letter):
        if letter not in self.clicked_letters:
            self.clicked_letters.append(letter)

    def show(self):
        self.screen.fill(self.WHITE)
        self.draw_hangman()
        self.draw_word()
        self.draw_letters()
        pygame.display.flip()

    def is_game_over(self):
        return self.wrong_guesses >= self.hangman_parts
    
    def add_wrong_guess(self):
        self.wrong_guesses += 1

    def show_message(self, message, color):
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render(message, True, color)
        text_rect = text_surface.get_rect(center=(400, 50)) 
        self.screen.blit(text_surface, text_rect)