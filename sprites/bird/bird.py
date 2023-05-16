import pygame
import os

class Bird:
    def __init__(self, display: pygame.Surface) -> None:
        self.display = display
        self.moving: bool = False
        
        self.bird_frames: list[pygame.Surface]
        self.bird_index: int
        self.bird: pygame.Surface
        self.bird_rect: pygame.Rect
        
        self.x_pos: int = 200
        self.y_pos: int = 300
        
        self.velocity: int | float = 0
        self.rotation: int | float = 3
        self.gravity: int | float = 0.25
        
        self.jump_velocity: int | float = 8.5
        self.max_rotation: int | float = 75
        
        self.load_frames()
        self.update_bird()
        
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
        self.bird_frames = [pygame.transform.rotozoom(bird, 0, 1.15) for bird in self.bird_frames]
        self.bird_index = 0
    
    def update_bird(self):
        self.bird = self.bird_frames[self.bird_index]
        self.bird = pygame.transform.rotate(self.bird, min(-self.velocity * self.rotation, self.max_rotation))
        self.bird_rect = self.bird.get_rect(center = (self.x_pos, self.y_pos))
        
    def flap(self) -> None:
        if self.bird_index < 2:
            self.bird_index += 1
        else:
            self.bird_index = 0
        self.update_bird()
        
    def jump(self):
        self.velocity = -self.jump_velocity
    
    def apply_gravity(self):
        self.velocity += self.gravity
        self.y_pos += self.velocity
        self.update_bird()
        
    def render(self) -> None:
        if self.moving:
            self.apply_gravity()
        self.display.blit(self.bird, self.bird_rect)
        