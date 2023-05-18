import pygame

from sprites.bird import Bird
from sprites.pipe import Pipe, PipeManager
from sprites.ground import Ground


class BirdCollisionManager:
    def __init__(self, bird: Bird, other_sprite) -> None:
        self.bird = bird
        self.other_sprite = other_sprite
        
        self.collided: bool = False
        
        self._on_collision = lambda: None
        self._collision_sound: pygame.mixer.Sound = None
        
    def add_collision_callback(self, func) -> None:
        self._on_collision = func
        
    def remove_collision_callback(self) -> None:
        self._on_collision = lambda: None
        
    def add_collision_sound(self, sound: pygame.mixer.Sound) -> None:
        self._collision_sound = sound
    
    def remove_collision_sound(self) -> None:
        self._collision_sound = None
        
    def check_collision(self) -> bool:
        offset = (self.other_sprite.rect.x - self.bird.bird_rect.x, self.other_sprite.rect.y - self.bird.bird_rect.y)
        return self.bird.mask.overlap(self.other_sprite.mask, offset) or self.bird.bird_rect.y <= -150
        
    def handle_collision(self) -> None:
        if self.check_collision() and not self.collided:
            print('collision')
            self._on_collision()
            if self._collision_sound is not None:
                self._collision_sound.play()
            self.collided = True
        else:
            self.collided = False
            

class BirdPipeInteractionManager(BirdCollisionManager):
    def __init__(self, bird: Bird, pipe_manager: PipeManager):
        self.bird = bird
        self.pipe_manager = pipe_manager
        
        super().__init__(self.bird, None)
        
        self.passing: bool = False
        
        self._on_pass_through = lambda: None
        self._on_collision = lambda: None
        
        self._pass_through_sound: pygame.mixer.Sound = None
        self._collision_sound: pygame.mixer.Sound = None
    
    def add_pass_through_callback(self, func) -> None:
        self._on_pass_through = func
        
    def remove_pass_through_callback(self) -> None:
        self._on_pass_through = lambda: None
        
    def add_pass_through_sound(self, sound: pygame.mixer.Sound) -> None:
        self._pass_through_sound = sound
    
    def remove_pass_through_sound(self) -> None:
        self._pass_through_sound = None
        
    def check_pass_through(self) -> tuple[bool, Pipe | None]:
        for pipe in self.pipe_manager:
            valid_x = (
                self.bird.centerx >= pipe.top_pipe.centerx
                and self.bird.centerx <= pipe.top_pipe.midright[0]
            )
            valid_y = (
                self.bird.top > pipe.top_pipe.midbottom[1]
                and self.bird.bottom < pipe.bottom_pipe.midtop[1]
            )
            if valid_x and valid_y:
                return (True, pipe)
        return (False, None)
        
    def handle_pass_through(self) -> None:
        passing_through, _ = self.check_pass_through()
        if passing_through and not self.passing:
            print('pass through')
            self._on_pass_through()
            if self._pass_through_sound is not None: 
                self._pass_through_sound.play()
            self.passing = True
        self.passing = passing_through
        
    def check_collision(self) -> tuple[bool, Pipe]:  # sourcery skip: use-next
        for pipe in self.pipe_manager:
            top_pipe_offset = (pipe.top_pipe.x - self.bird.bird_rect.x, pipe.top_pipe.y - self.bird.bird_rect.y)
            bottom_pipe_offset = (pipe.bottom_pipe.x - self.bird.bird_rect.x, pipe.bottom_pipe.y - self.bird.bird_rect.y)
            if self.bird.mask.overlap(pipe.mask, top_pipe_offset) or self.bird.mask.overlap(pipe.mask, bottom_pipe_offset):
                return (True, pipe)
        return (False, None)
    
    def handle_collision(self) -> None:
        colliding, _ = self.check_collision()
        if colliding and not self.collided:
            print('collision')
            self._on_collision()
            if self._collision_sound is not None:
                self._collision_sound.play()
            self.collided = True
        self.collided = colliding
    
    def handle_interactions(self):      
        self.handle_collision()
        self.handle_pass_through()