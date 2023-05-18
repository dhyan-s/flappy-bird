import pygame
from pygame.locals import  *

from game import Game

pygame.init()

FPS = 120
SCREENWIDTH = 700
SCREENHEIGHT = 1024

display = pygame.display.set_mode((SCREENWIDTH , SCREENHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird By Dhyanesh")

game = Game(display)
game.load()

game_started = True
while True:
    display.fill((0, 0, 0))
    
    if game_started:
        game.render()
    
    pygame.display.update()
    clock.tick(FPS)