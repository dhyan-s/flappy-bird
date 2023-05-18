import pygame
import sys
import os

from sprites.ground import Ground
from .display_handler import DisplayHandler

class HomeScreen:
    def __init__(self, display: pygame.Surface, display_handler: DisplayHandler) -> None:
        self.display = display
        self.display_handler = display_handler
        self.display_handler.add_state('home_screen', self)
        
    def load(self) -> None:
        cur_dir = os.path.dirname(__file__)
        self.background = pygame.image.load(f"{cur_dir}/background.png").convert()
        self.background = pygame.transform.scale(self.background, (self.display.get_width(), self.display.get_height()))
        
        self.message = pygame.image.load(f"{cur_dir}/message.png")
        self.ground = Ground(self.display)
        
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