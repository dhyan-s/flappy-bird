import pygame
import os

class Ground:
    """
    Represents the ground sprite in the game.
    """
    
    def __init__(self, display: pygame.Surface) -> None:
        self.display = display
        
        self.load_image()
        
    def load_image(self) -> None:
        """
        Loads the ground image, scales it to fit the display width,
        sets the position of the ground, and creates a collision mask from the image.
        """
        cur_dir = os.path.dirname(__file__)
        self.ground = pygame.image.load(f"{cur_dir}/ground.png")
        self.ground = pygame.transform.scale(self.ground, (self.display.get_width(), 220))
        self.rect = self.ground.get_rect(x=0, y=self.display.get_height()-self.ground.get_height())
        self.mask = pygame.mask.from_surface(self.ground)
        
    def render(self) -> None:
        """Renders the ground on the display surface."""
        self.display.blit(self.ground, self.rect)
