import pygame
import random

from .pipe import Pipe

class PipeManager:
    def __init__(self, display: pygame.Surface, start_x: int | float = 800) -> None:
        self.display = display
        
        self.start_x = start_x
        
        self.pipe_list: list[Pipe] = []
        self.pipe_heights = range(350, 700, 50)
        
    def __iter__(self):
        return iter(self.pipe_list)
        
    def add_pipe(self) -> None:
        pipe = Pipe(self.display, self.start_x, random.choice(self.pipe_heights))
        pipe.start()
        self.pipe_list.append(pipe)
        
    def remove_pipe(self, pipe: Pipe):
        self.pipe_list.remove(pipe)
        
    def cleanup(self) -> None:
        for pipe in self.pipe_list:
            if pipe.x_pos < -200:
                self.remove_pipe(pipe)
    
    def render(self) -> None:
        for pipe in self.pipe_list:
            pipe.render()
        self.cleanup()