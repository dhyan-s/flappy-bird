import pygame

from .bird import Bird
from .pipe import Pipe, PipeManager

class BirdPipeInteractionManager:
    def __init__(self, bird: Bird, pipe_manager: PipeManager):
        self.bird = bird
        self.pipe_manager = pipe_manager
        
        self.passing_pipe: Pipe = None
        self.colliding_pipe: Pipe = None
        
    def check_pass_through(self):
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
                if self.passing_pipe == pipe: continue
                print('pass through')
                self.passing_pipe = pipe
            elif self.passing_pipe == pipe:
                self.passing_pipe = None
    
    def check_collision(self):
        for pipe in self.pipe_manager:
            if self.bird.bird_rect.colliderect(pipe.top_pipe) or self.bird.bird_rect.colliderect(pipe.bottom_pipe):
                if self.colliding_pipe == pipe: continue
                self.colliding_pipe = pipe
                print('collision')
            elif self.colliding_pipe == pipe:
                self.colliding_pipe = None
    
    def handle_interactions(self):      
        self.check_collision()
        self.check_pass_through()