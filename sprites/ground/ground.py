import pygame
import os

class Ground:
    def __init__(self, display: pygame.Surface) -> None:
        self.display = display
        self._move: bool = False
        
        self.move_velocity: int | float = 6.1
        
        self.load_image()
        
    def load_image(self) -> None:
        cur_dir = os.path.dirname(__file__)
        self.ground = pygame.image.load(f"{cur_dir}/ground_lines.png")
        self.ground = pygame.transform.scale(self.ground, (self.display.get_width(), 200))
        
        self.ground1 = self.ground.get_rect(topleft=(0, self.display.get_height()-200))
        self.ground2 = self.ground.get_rect(topleft=(self.ground1.right-0.5, self.display.get_height()-200))
        self.ground3 = self.ground.get_rect(topleft=(self.ground2.right-0.5, self.display.get_height()-200))
        
    def start(self) -> None:
        self._move = True
        
    def stop(self) -> None:
        self._move = False
        
    def move(self) -> None:
        self.ground1.x -= self.move_velocity
        self.ground2.x -= self.move_velocity
        self.ground3.x -= self.move_velocity
        if self.ground1.right <= 0:
            self.ground1.left = self.ground3.right-0.5
        if self.ground2.right <= 0:
            self.ground2.left = self.ground1.right-0.5
        if self.ground3.right <= 0:
            self.ground3.left = self.ground2.right-0.5
        
    def render(self) -> None:
        if self._move:
            self.move()
        self.display.blit(self.ground, self.ground1)
        self.display.blit(self.ground, self.ground2)
        self.display.blit(self.ground, self.ground3)