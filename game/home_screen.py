import pygame
import os, sys

from sprites.ground import Ground
from .display_handler import DisplayHandler
from .score import Score

class HomeScreen:
    """
    Represents the home screen state of the Flappy Bird game.
    """
    
    def __init__(self, display: pygame.Surface, display_handler: DisplayHandler, score_handler: Score) -> None:
        self.display = display
        self.display_handler = display_handler
        self.display_handler.add_state('home_screen', self)
        self.score_handler = score_handler
        
    def load(self) -> None:
        """
        Loads the required images and objects to render the home screen.
        """
        cur_dir = os.path.dirname(__file__)
        self.background = pygame.image.load(f"{cur_dir}/background.png").convert()
        self.background = pygame.transform.scale(self.background, (self.display.get_width(), self.display.get_height()))
        
        self.message = pygame.image.load(f"{cur_dir}/message.png")
        self.ground = Ground(self.display)
        
    def render_scoreboard(self) -> None:
        """
        Renders the score and high score on the home screen.
        """
        separator_length = self.display.get_width()
        separator_thickness = 3
        score_separator_y = 80
        high_score_separator_y = 725
        
        score_separator = pygame.draw.line(self.display, (0,0,0), (0, score_separator_y), (separator_length, score_separator_y), width=separator_thickness)
        self.score_handler.render_score("SCORE: $", y=self.score_handler.in_between(0, score_separator.bottom))
        
        high_score_separator = pygame.draw.line(self.display, (0,0,0), (0, high_score_separator_y), (separator_length, high_score_separator_y), width=separator_thickness)
        self.score_handler.render_high_score("HIGH SCORE: $", y=self.score_handler.in_between(high_score_separator.bottom, self.ground.rect.top+5))
        
    def render(self) -> None:
        """
        Renders the home screen and detects keypress events to initiate the start of the game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or event.type == pygame.MOUSEBUTTONDOWN:
                self.display_handler.set_current_state('game')
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.message, (self.display.get_width() // 2 - self.message.get_width() // 2, self.display.get_height() // 2 - self.message.get_height() // 2))
        self.ground.render()
        self.render_scoreboard()
