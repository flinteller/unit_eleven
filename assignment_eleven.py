import pygame
import sys
from pygame.locals import *

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((500, 500), 0, 32)
    pygame.display.set_caption("Breakout")
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    block = pygame.surface((50, 50))
    ball = block.get_rect()
    block.fill(BLACK)
    speedx = 5
    speedy = 5






    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        main_surface.fill(WHITE)
        rect.top += speedy
        rect.left += speedx
        if rect.top < 0 or rect.bottom > 500:
            speedy = -speedy
        if 

