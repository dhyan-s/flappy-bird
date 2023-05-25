import pygame
from typing import Callable

class Score:
    """
    Represents the score and high score display for a game.
    """
    
    def __init__(self, 
                 display: pygame.Surface,
                 score: int = 0,
                 high_score: int = 0,
                 font: pygame.font.Font = None) -> None:
        self.display = display
        self._score = score
        self.high_score = high_score
        self.font = font if font is not None else pygame.font.SysFont("Arial Black", 50)
        
        self.on_new_high_score: Callable = None
        
        self.special_character: str = "$"
        
    @property
    def score(self): 
        return self._score
    
    @score.setter
    def score(self, value: int): 
        """Sets the score value and updates the high score if necessary."""
        self._score = value
        self.update_high_score()
        
    def reset_score(self) -> None: self.score = 0
    def reset_high_score(self) -> None: self.high_score = 0
    def increment_score(self) -> None: self.score += 1
        
    def update_high_score(self) -> None:
        """Updates the high score if the current score is higher."""
        if self.score > self.high_score:
            self.high_score = self.score
            if self.on_new_high_score is not None:
                self.on_new_high_score(self.high_score)
            
    def in_between(self, pos1: int, pos2: int) -> int:
        """Returns the value in between two positions."""
        pos1, pos2 = sorted((pos1, pos2), reverse=True)
        return pos1 + ((pos2-pos1)//2)
            
    def _render_text(self,
                     value: int,
                     text: str = None,
                     x: int = None,
                     y: int = None,
                     color: str = "white") -> None:
        """
        Renders the text on the display surface.

        Args:
            - value: The value to replace with `self.special_character`.
            - text: The text to display (default: None).
            - x: The x-coordinate of the text position (default: None, center of the display).
            - y: The y-coordinate of the text position (default: None, center of the display).
            - color: The color of the text (default: "white").
        """
        if text is None: 
            text = self.special_character
        if x is None: 
            x = self.display.get_width() // 2
        if y is None: 
            y = self.display.get_height() // 2
        
        color = pygame.Color(color)
        
        text = text.replace(self.special_character, str(value))
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        
        self.display.blit(text_surface, text_rect)

    def render_score(self, 
                     text: str = None,
                     x: int = None, 
                     y: int = None, 
                     color: str = "white") -> None:
        """
        Renders the score on the display surface.

        Args:
            - text: The additional text to display (default: None). `self.special_character` in `text` is replaced with `self.score` before rendering.
            - x: The x-coordinate of the score position (default: None, center of the display).
            - y: The y-coordinate of the score position (default: None, center of the display).
            - color: The color of the score text (default: "white").
        """
        self._render_text(self.score, text, x, y, color)
        
    def render_high_score(self, 
                          text: str = None, 
                          x: int = None, 
                          y: int = None, 
                          color: str = "white") -> None:
        """
        Renders the score on the display surface.

        Args:
            - text: The additional text to display (default: None). `self.special_character` in `text` is replaced with `self.high_score` before rendering.
            - x: The x-coordinate of the score position (default: None, center of the display).
            - y: The y-coordinate of the score position (default: None, center of the display).
            - color: The color of the score text (default: "white").
        """
        self._render_text(self.high_score, text, x, y, color)
