import pygame
import sys
import os

from sprites.ground import Ground

class HomeScreen:
    def __init__(self, display: pygame.Surface) -> None:
        self.display = display
        
    def load(self) -> None:
        cur_dir = os.path.dirname(__file__)
        self.background = pygame.image.load(f"{cur_dir}/background.png")
        self.background = pygame.transform.scale(self.background, (self.display.get_width(), self.display.get_height()))
        
        self.message = pygame.image.load(f"{cur_dir}/message.png")
        self.ground = Ground(self.display)
        
    def render(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.message, (self.display.get_width() // 2 - self.message.get_width() // 2, self.display.get_height() // 2 - self.message.get_height() // 2))
        self.ground.render()