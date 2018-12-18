import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, window_width, window_height, radius):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.color = color
        self.radius = radius
        self.window_width = window_width
        self.window_height = window_height

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface((radius, radius * 2))
        self.rect = self.image.get_rect()
        self.speedx = 5
        self.speedy = 3
        # Add a circle to represent the ball to the surface just created.
        pygame.draw.circle(self.image, color, (5, 5), radius, 0)

    def move(self):
        self.rect.top += self.speedy
        self.rect.left += self.speedx

        if self.rect.top < 0 or self.rect.bottom > self.window_height:
            self.speedy = -self.speedy
        elif self.rect.left < 0 or self.rect.right > self.window_width:
            self.speedx = -self.speedx

    def collide(self, brick_group):
        if pygame.sprite.spritecollide(self, brick_group, True):
            self.x_speed = -self.x_speed
            self.y_speed = -self.y_speed