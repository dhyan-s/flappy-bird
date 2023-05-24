import pygame
import os

class Bird:
    """
    The Bird class encapsulates the behavior and attributes of the bird character
    in the game. It handles the bird's movement, animation, position, and collision
    detection.
    """
    
    def __init__(self, display: pygame.Surface) -> None:
        self.display = display
        self.moving: bool = False
        
        self.bird_frames: list[pygame.Surface]
        self.bird_index: int
        self.bird: pygame.Surface
        self.rect: pygame.Rect
        
        self.x_pos: int = 200
        self.y_pos: int = 300
        
        self.velocity: int | float = 0
        self.rotation: int | float = 3
        self.gravity: int | float = 0.25
        
        self.jump_velocity: int | float = 8.5
        self.max_rotation: int | float = 75
        
        self._jump_sound: pygame.mixer.Sound = None
        
        self.load_frames()
        self.update_bird()
        
    def start(self) -> None:
        """Starts the bird's movement."""
        self.moving = True
        
    def stop(self) -> None:
        """Stops the bird's movement."""
        self.moving = False
        
    def reset(self) -> None:
        """Resets the bird's position and velocity."""
        self.x_pos = 200
        self.y_pos = 300
        self.velocity = 0
        
    def add_jump_sound(self, sound: pygame.mixer.Sound) -> None:
        """Adds a sound effect to play when the bird jumps."""
        self._jump_sound = sound
        
    def remove_jump_sound(self) -> None:
        """Removes the jump sound effect."""
        self._jump_sound = None
        
    def load_frames(self) -> None:
        """Loads the bird animation frames from image files."""
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
    
    @property 
    def mask(self) -> pygame.mask.Mask:
        """Returns a mask of the bird in real time"""
        return pygame.mask.from_surface(self.bird)
    
    def update_bird(self) -> None:
        """Updates the bird's image, rotation, and position."""
        self.bird = self.bird_frames[self.bird_index]
        self.bird = pygame.transform.rotate(self.bird, min(-self.velocity * self.rotation, self.max_rotation))
        self.rect = self.bird.get_rect(center = (self.x_pos, self.y_pos))
        
    def flap(self) -> None:
        """Performs a flap animation."""
        if not self.moving: return
        if self.bird_index < 2:
            self.bird_index += 1
        else:
            self.bird_index = 0
        
    def jump(self) -> None:
        """Makes the bird jump by changing its velocity."""
        self.velocity = -self.jump_velocity
        if self._jump_sound is not None:
            self._jump_sound.play()
    
    def apply_gravity(self) -> None:
        """Applies gravity to the bird's vertical velocity."""
        self.velocity += self.gravity
        self.y_pos += self.velocity
        
    def render(self) -> None:
        """Renders the bird on the display surface"""
        if self.moving:
            self.apply_gravity()
            self.update_bird()
        self.display.blit(self.bird, self.rect)   
