import pygame
from pygame.locals import  *
import sys

from sprites.bird import Bird
from sprites.pipe import Pipe, PipeManager
from sprites.interactions import BirdPipeInteractionManager

pygame.init()

FPS = 120
SCREENWIDTH = 700
SCREENHEIGHT = 1024

display = pygame.display.set_mode((SCREENWIDTH , SCREENHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird By Dhyanesh")

crash_sound = pygame.mixer.Sound("assets/sounds/crash.mp3")
point_sound = pygame.mixer.Sound("assets/sounds/point.ogg")
jump_sound = pygame.mixer.Sound("assets/sounds/jump.ogg")

bird = Bird(display)
bird.start()

pipe_manager = PipeManager(display)
pipe_manager.start()

bird_pipe_interaction_manager = BirdPipeInteractionManager(bird, pipe_manager)

BIRD_FLAP = pygame.USEREVENT
pygame.time.set_timer(BIRD_FLAP, 100)

ADDPIPE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDPIPE, 900)

def collision():
    pipe_manager.stop()
    bird.stop()
    crash_sound.play()
    
bird_pipe_interaction_manager.add_collision_callback(collision)
bird_pipe_interaction_manager.add_pass_through_callback(lambda: point_sound.play())

while True:
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (event.type  == pygame.KEYDOWN and event.key == pygame.K_SPACE) or event.type == pygame.MOUSEBUTTONDOWN:
            bird.jump()
            jump_sound.play()
        if event.type == BIRD_FLAP:
            bird.flap()
        if event.type == ADDPIPE:
            pipe_manager.add_pipe()
    pipe_manager.render()
    bird.render()
    bird_pipe_interaction_manager.handle_interactions()
    pygame.display.update()
    clock.tick(FPS)