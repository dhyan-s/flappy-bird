import pygame
import random
from typing import Iterable

from .pipe import Pipe

class PipeManager:
    """
    Manages a collection of Pipe() objects in the game.
    """
    
    def __init__(self, display: pygame.Surface, start_x: int | float = 800) -> None:
        self.display = display
        self.moving: bool = False
        
        self.start_x = start_x
        
        self.pipe_list: list[Pipe] = []
        self.pipe_heights = range(350, 700, 50)
        self.pipe_distance = 650
        
    def start(self) -> None:
        """
        Starts the movement of the pipes.
        """
        self.moving = True
        for pipe in self.pipe_list:
            pipe.start()
        
    def stop(self) -> None:
        """
        Stops the movement of the pipes.
        """
        self.moving = False
        for pipe in self.pipe_list:
            pipe.stop()
            
    def reset(self) -> None:
        """
        Resets the pipe list, removing all pipes.
        """
        self.pipe_list.clear()
        
    def __iter__(self) -> Iterable[Pipe]:
        """
        Returns an iterator over the pipe list.
        """
        return iter(self.pipe_list)
        
    def add_pipe(self) -> None:
        """
        - Creates a new Pipe instance with a random height and adds it
        to the pipe list. 
        - If the pipes are currently moving, the new pipe will also start moving.
        """
        pipe = Pipe(self.display, self.start_x, random.choice(self.pipe_heights))
        if self.moving:
            pipe.start()
        self.pipe_list.append(pipe)
        
    def check_add_pipe(self) -> None:
        """
        - Checks if a new pipe should be added based on the distance between
        the last pipe in the list and the starting position.
        - If the distance exceeds the specified pipe distance, a new pipe is added.
        """
        if len(self.pipe_list) == 0:
            self.add_pipe()
        if self.start_x - self.pipe_list[-1].bottom_pipe.centerx >= self.pipe_distance: 
            self.add_pipe()
        
    def remove_pipe(self, pipe: Pipe) -> None:
        """Removes a pipe from the pipe list."""
        self.pipe_list.remove(pipe)
        
    def cleanup(self) -> None:
        """
        Removes pipes that are out of the screen.
        """
        for pipe in self.pipe_list:
            if pipe.x_pos < -200:
                self.remove_pipe(pipe)
    
    def render(self) -> None:
        """
        - Renders the pipes on the display surface.
        - This method checks if a new pipe needs to be added, renders each pipe in the list,
        and performs a cleanup to remove pipes that are out of the screen.
        """
        self.check_add_pipe()
        for pipe in self.pipe_list:
            pipe.render()
        self.cleanup()
