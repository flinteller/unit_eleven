import pygame
import ball
import breakout
import paddle


class Brick(pygame.sprite.Sprite):

    def __init__(self, surface, height, width, color):
        self.BRICK_HEIGHT = 8


    def draw_bricks(self, x_pos, y_pos):
        pygame.draw.rect(self.main_surface, color, (x_pos, y_pos, self.BRICK_WIDTH, self.BRICK_HEIGHT), 0)

