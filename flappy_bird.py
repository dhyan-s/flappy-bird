import pygame
from pygame.locals import  *
import sys

from sprites.bird import Bird

pygame.init()

FPS = 120
SCREENWIDTH = 700
SCREENHEIGHT = 1024

display = pygame.display.set_mode((SCREENWIDTH , SCREENHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird By Dhyanesh")

bird = Bird(display)
bird.start()

while True:
    display.fill((0, 0, 0))
    for event in pygame.event.get ():
        if event.type == pygame.QUIT: #To exit program
            pygame.quit()
            sys.exit()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or event.type == pygame.MOUSEBUTTONDOWN:
            bird.jump()
    bird.render()
    pygame.display.update()
    clock.tick(FPS)