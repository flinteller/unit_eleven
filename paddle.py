import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.main_surface = main_surface
        self.color = color
        self.width = width
        self.height = height

        # Create a surface with the correct height and width
        self.image = pygame.image.load("Google_logo_small.png")

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        # self.image.fill(color)

    def move_left(self):
        self.rect.x = self.rect.x - 7

        if self.rect.left < 0:
            self.rect.x = 1


    def move_right(self):
        self.rect.x = self.rect.x + 7

        if self.rect.right > 400:
            self.rect.x = 335




