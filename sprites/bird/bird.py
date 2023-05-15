import pygame
import os

class Bird:
    def __init__(self, display: pygame.Surface) -> None:
        self.display = display
        self.moving: bool = False
        
        self.bird_frames: list[pygame.Surface]
        self.bird_index: int
        
        self.x_pos: int = 200
        self.default_y = 300
        
        self.load_frames()
        
        self.bird: pygame.Surface
        self.bird_rect: pygame.Rect
        self.bird, self.bird_rect = self.get_bird()
        
    def start(self):
        self.moving = True
        
    def stop(self):
        self.moving = False
        
    def load_frames(self) -> None:
        cur_dir = os.path.dirname(__file__)
        
        img_downflap: pygame.Surface = pygame.image.load(f"{cur_dir}/bird_downflap.png")
        bird_downflap: pygame.Surface = pygame.transform.scale(img_downflap , (70 , 55))
        
        img_midflap: pygame.Surface = pygame.image.load(f"{cur_dir}/bird_midflap.png")
        bird_midflap: pygame.Surface = pygame.transform.scale(img_midflap , (70 , 55))
        
        img_upflap: pygame.Surface = pygame.image.load(f"{cur_dir}/bird_upflap.png")
        bird_upflap: pygame.Surface = pygame.transform.scale(img_upflap , (70 , 55))
        
        self.bird_frames = [bird_downflap , bird_midflap , bird_upflap]
        self.bird_index = 0
        
    def get_bird(self) -> tuple[pygame.Surface, pygame.Rect]:
        bird = self.bird_frames[self.bird_index]
        y_pos = self.bird_rect.centery if hasattr(self, 'bird_rect') else self.default_y
        bird_rect = bird.get_rect(center = (self.x_pos, y_pos))
        return bird, bird_rect
        
    def flap(self) -> None:
        if self.bird_index < 2:
            self.bird_index += 1
        else:
            self.bird_index = 0
        self.bird, self.bird_rect = self.get_bird()
        
    def render(self) -> None:
        self.display.blit(self.bird, self.bird_rect)
        