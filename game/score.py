from dataclasses import dataclass
import pygame

@dataclass
class Score:
    score: int = 0
    high_score: int = 0
    font_path: str = None
    font_size: int = 50
    
    def __post_init__(self):
        self.font = pygame.font.Font(self.font_path, self.font_size) if self.font_path is not None else pygame.font.SysFont("Consolas", self.font_size)
        
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
            