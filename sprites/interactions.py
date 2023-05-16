import pygame

from .bird import Bird
from .pipe import Pipe, PipeManager

class BirdPipeInteractionManager:
    def __init__(self, bird: Bird, pipe_manager: PipeManager):
        self.bird = bird
        self.pipe_manager = pipe_manager
        
        self.passing_pipe: Pipe = None
        self.colliding_pipe: Pipe = None
        
        self.on_pass_through = lambda: None
        self.on_collision = lambda: None
    
    def add_pass_through_callback(self, func) -> None:
        self.on_pass_through = func
        
    def remove_pass_through_callback(self) -> None:
        self.on_pass_through = lambda: None
        
    def add_collision_callback(self, func) -> None:
        self.on_collision = func
        
    def remove_collision_callback(self) -> None:
        self.on_collision = lambda: None
        
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
        
    def handle_pass_through(self):
        passing_through, passing_pipe = self.check_pass_through()
        if passing_through and self.passing_pipe != passing_pipe:
            print('pass through')
            self.on_pass_through()
        self.passing_pipe = passing_pipe
        
    def check_collision(self) -> tuple[bool, Pipe]:  # sourcery skip: use-next
        for pipe in self.pipe_manager:
            if self.bird.bird_rect.colliderect(pipe.top_pipe) or self.bird.bird_rect.colliderect(pipe.bottom_pipe):
                return (True, pipe)
        return (False, None)
    
    def handle_collision(self):
        colliding, colliding_pipe = self.check_collision()
        if colliding and self.colliding_pipe != colliding_pipe:
            print('collision')
            self.on_collision()
        self.colliding_pipe = colliding_pipe
    
    def handle_interactions(self):      
        self.handle_collision()
        self.handle_pass_through()