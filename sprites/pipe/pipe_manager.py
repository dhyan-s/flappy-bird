import pygame
import random

from .pipe import Pipe

class PipeManager:
    def __init__(self, display: pygame.Surface, start_x: int | float = 800) -> None:
        self.display = display
        self.moving: bool = False
        
        self.start_x = start_x
        
        self.pipe_list: list[Pipe] = []
        self.pipe_heights = range(350, 700, 50)
        self.pipe_distance = 650
        
    def start(self):
        self.moving = True
        for pipe in self.pipe_list:
            pipe.start()
        
    def stop(self):
        self.moving = False
        for pipe in self.pipe_list:
            pipe.stop()
            
    def reset(self):
        self.pipe_list.clear()
        
    def __iter__(self):
        return iter(self.pipe_list)
        
    def add_pipe(self) -> None:
        pipe = Pipe(self.display, self.start_x, random.choice(self.pipe_heights))
        if self.moving:
            pipe.start()
        self.pipe_list.append(pipe)
        
    def check_add_pipe(self) -> None:
        if len(self.pipe_list) == 0: 
            self.add_pipe()
        if self.start_x - self.pipe_list[-1].bottom_pipe.centerx >= self.pipe_distance: 
            self.add_pipe()
        
    def remove_pipe(self, pipe: Pipe):
        self.pipe_list.remove(pipe)
        
    def cleanup(self) -> None:
        for pipe in self.pipe_list:
            if pipe.x_pos < -200:
                self.remove_pipe(pipe)
    
    def render(self) -> None:
        self.check_add_pipe()
        for pipe in self.pipe_list:
            pipe.render()
        self.cleanup()