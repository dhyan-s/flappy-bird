from dataclasses import dataclass
import pygame

@dataclass
class Score:
    display: pygame.Surface
    score: int = 0
    high_score: int = 0
    font_path: str = None
    font_size: int = 50
    
    def __post_init__(self):
        self.font = pygame.font.Font(self.font_path, self.font_size) if self.font_path is not None else pygame.font.SysFont("Consolas", self.font_size)
        self.special_character: str = "$"
        
    def reset_score(self): 
        self.score = 0
        
    def reset_high_score(self): 
        self.high_score = 0
        
    def increment_score(self): 
        self.score += 1
        self.update_high_score()
        
    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
    def _render_text(self,
                     value: int,
                     text: str = None,
                     x: int = None,
                     y: int = None,
                     color: str = "white") -> None:
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
        self._render_text(self.score, text, x, y, color)
        
    def render_high_score(self, 
                          text: str = None, 
                          x: int = None, 
                          y: int = None, 
                          color: str = "white") -> None:
        self._render_text(self.high_score, text, x, y, color)
        
            