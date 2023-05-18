import pygame
import sys

from sprites.bird import Bird
from sprites.pipe import Pipe, PipeManager
from sprites.ground import Ground
from .interactions import BirdPipeInteractionManager

class Game:
    def __init__(self, display: pygame.Surface) -> None:
        self.display = display
        
    def collision(self):
        self.pipe_manager.stop()
        self.bird.stop()
        
    def load(self) -> None:
        self.crash_sound = pygame.mixer.Sound("assets/sounds/crash.mp3")
        self.point_sound = pygame.mixer.Sound("assets/sounds/point.ogg")
        self.jump_sound = pygame.mixer.Sound("assets/sounds/jump.ogg")
        
        self.bird = Bird(self.display)
        self.bird.start()
        self.bird.add_jump_sound(self.jump_sound)

        self.pipe_manager = PipeManager(self.display)
        self.pipe_manager.start()

        self.bird_pipe_interaction_manager = BirdPipeInteractionManager(self.bird, self.pipe_manager)
        self.bird_pipe_interaction_manager.add_collision_callback(self.collision)
        self.bird_pipe_interaction_manager.add_collision_sound(self.crash_sound)
        self.bird_pipe_interaction_manager.add_pass_through_sound(self.point_sound)

        self.ground = Ground(self.display)

        self.BIRD_FLAP = pygame.USEREVENT
        pygame.time.set_timer(self.BIRD_FLAP, 100)

        self.ADDPIPE = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDPIPE, 900)
        
    def render(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type  == pygame.KEYDOWN and event.key == pygame.K_SPACE) or event.type == pygame.MOUSEBUTTONDOWN:
                self.bird.jump()
            if event.type == self.BIRD_FLAP:
                self.bird.flap()
            if event.type == self.ADDPIPE:
                self.pipe_manager.add_pipe()
        self.pipe_manager.render()
        self.bird.render()
        self.bird_pipe_interaction_manager.handle_interactions()
        self.ground.render()