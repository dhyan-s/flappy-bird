import pygame
from pygame.locals import  *
import sys

pygame.init()

FPS = 120
SCREENWIDTH = 700
SCREENHEIGHT = 1024

display = pygame.display.set_mode((SCREENWIDTH , SCREENHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird By Dhyanesh")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #To exit program
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(FPS)