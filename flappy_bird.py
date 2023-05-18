import pygame
from pygame.locals import  *

from game import Game
from game import HomeScreen
from game import DisplayHandler

pygame.init()

FPS = 120
SCREENWIDTH = 700
SCREENHEIGHT = 1024

display = pygame.display.set_mode((SCREENWIDTH , SCREENHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird By Dhyanesh")

display_handler = DisplayHandler()

game = Game(display, display_handler)
game.load()

home_screen = HomeScreen(display, display_handler)
home_screen.load()

display_handler.set_current_state('home_screen')

while True:
    display.fill((0, 0, 0))
    
    display_handler.render()
    
    pygame.display.update()
    clock.tick(FPS)