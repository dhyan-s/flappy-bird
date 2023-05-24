import pygame
import os

class Ground:
    def __init__(self, display: pygame.Surface) -> None:
        self.display = display
        
        self.load_image()
        
    def load_image(self) -> None:
        cur_dir = os.path.dirname(__file__)
        self.ground = pygame.image.load(f"{cur_dir}/ground.png")
        self.ground = pygame.transform.scale(self.ground, (self.display.get_width(), 220))
        self.rect = self.ground.get_rect(x=0, y=self.display.get_height()-self.ground.get_height())
        self.mask = pygame.mask.from_surface(self.ground)
        
    def render(self) -> None:
        self.display.blit(self.ground, self.rect)
