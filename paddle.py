import pygame
import random


class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, height, width):
        """
        This function creates creates a surface using each other params
        :param main_surface:
        :param color:
        :param height:
        :param width:
        """
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.main_surface = main_surface
        self.color = color
        self.height = height
        self.width = width

        # Create a surface with the correct height and width
        self.image = pygame.Surface((width, height))

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        self.image.fill(color)

    def move_left(self):
        """
        This function moves the paddle left and stops the paddle form going off screen
        :return:
        """
        self.rect.x = self.rect.x - 7

        if self.rect.left < 0:
            self.rect.x = 1

    def move_right(self):
        """
        This function moves the paddle right and stops the paddle form going off screen
        :return:
        """
        self.rect.x = self.rect.x + 7

        if self.rect.right > 400:
            self.rect.x = 335

    def resize(self):
        """
        This function creates a new surface with a random size and keeps its color
        :return:
        """
        self.width = random.randint(20, 100)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)



