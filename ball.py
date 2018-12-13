import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, window_width, window_height, radius):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.color = color
        self.radius = radius

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, color, (25, 25), radius, 0)
        self.speedx = 5
        self.speedy = 3
        # Add a circle to represent the ball to the surface just created.

    def move(self):
        self.rect.top += self.speedy
        self.rect.left += self.speedx
        if self.rect.top < 0 or self.rect.bottom > self.window_height:
            self.speedy = -self.speedy
        elif self.rect.left < 0 or self.rect.right > self.window_width:
            self.speedx = -self.speedx
