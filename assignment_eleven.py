import pygame
import sys
from pygame.locals import *

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((500, 500), 0, 32)
    pygame.display.set_caption("Breakout")
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    block = pygame.Surface((50, 50))
    rect = block.get_rect()
    pygame.draw.circle(block, RED, (25, 25), 25, 0)
    speedx = 5
    speedy = 3

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
        elif rect.left < 0 or rect.right > 500:
            speedx = -speedx

        main_surface.blit(block, rect)
        pygame.display.update()


main()
