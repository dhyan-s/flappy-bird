import pygame
import sys
import os

from sprites.ground import Ground
from .display_handler import DisplayHandler
from .score import Score

class HomeScreen:
    def __init__(self, display: pygame.Surface, display_handler: DisplayHandler, score_handler: Score) -> None:
        self.display = display
        self.display_handler = display_handler
        self.display_handler.add_state('home_screen', self)
        self.score_handler = score_handler
        
    def load(self) -> None:
        cur_dir = os.path.dirname(__file__)
        self.background = pygame.image.load(f"{cur_dir}/background.png").convert()
        self.background = pygame.transform.scale(self.background, (self.display.get_width(), self.display.get_height()))
        
        self.message = pygame.image.load(f"{cur_dir}/message.png")
        self.ground = Ground(self.display)
        
    def render_scoreboard(self):
        separator_length = self.display.get_width()
        separator_thickness = 3
        score_separator_y = 80
        high_score_separator_y = 725
        
        score_surface = self.score_handler.font.render(f"SCORE: {self.score_handler.score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(self.display.get_width()//2, 45))
        
        score_separator = pygame.draw.line(self.display, (0,0,0), (0, score_separator_y), (separator_length, score_separator_y), width=separator_thickness)
        
        high_score_surface = self.score_handler.font.render(f"HIGH SCORE: {self.score_handler.high_score}", True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(self.display.get_width()//2, 770))
        
        high_score_separator = pygame.draw.line(self.display, (0,0,0), (0, high_score_separator_y), (separator_length, high_score_separator_y), width=separator_thickness)
        
        self.display.blit(score_surface, score_rect)
        self.display.blit(high_score_surface, high_score_rect)
        
    def render(self) -> None:
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