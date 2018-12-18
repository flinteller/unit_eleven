import pygame, sys
from pygame.locals import *
import block


pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
X_SPEED = 3
Y_SPEED = 5

main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 32, 0)
pygame.display.set_caption("Animation")

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
WIDTH = 25
HEIGHT = 25

group = pygame.sprite.Group()
my_block = block.Block(main_window, WIDTH, HEIGHT, BLUE)
new_block = block.Block(main_window, WIDTH, HEIGHT, GREEN)
group.add(my_block)
group.add(new_block)

my_block.rect.x = 10
my_block.rect.y = 10
new_block.rect.x = WINDOW_WIDTH - 35
new_block.rect.y = WINDOW_HEIGHT - 35

while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()

    main_window.fill(WHITE)
    for a_brick in group:
        a_brick.move()
        group.remove(a_brick)
        a_brick.collide(group)
        group.add(a_brick)
        main_window.blit(a_brick.image, a_brick.rect)
    
    pygame.display.update()




