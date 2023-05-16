import pygame
from pygame.locals import  *
import sys

from sprites.bird import Bird
from sprites.pipe import Pipe

pygame.init()

FPS = 120
SCREENWIDTH = 700
SCREENHEIGHT = 1024

display = pygame.display.set_mode((SCREENWIDTH , SCREENHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird By Dhyanesh")

bird = Bird(display)
bird.start()

BIRD_FLAP = pygame.USEREVENT
pygame.time.set_timer(BIRD_FLAP, 100)

ADDPIPE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDPIPE, 900)

pipe = Pipe(display, 800, 400)
pipe.start()

while True:
    display.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or event.type == pygame.MOUSEBUTTONDOWN:
            bird.jump()
        if event.type == BIRD_FLAP:
            bird.flap()
        if event.type == ADDPIPE:
            pipe = Pipe(display, 800, 400)
            pipe.start()
    pipe.render()
    bird.render()
    pygame.display.update()
    clock.tick(FPS)