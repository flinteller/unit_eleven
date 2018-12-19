import pygame, sys
from pygame.locals import *
import brick
import ball
import paddle


def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    pygame.init()
    main_window = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 32, 0)
    pygame.display.set_caption("Breakout")

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    brick_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    x_pos = 0
    y_pos = BRICK_Y_OFFSET

    colors = [RED, ORANGE, YELLOW, GREEN, CYAN]
    for color in colors:
        for y in range(2):
            for z in range(10):
                my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
                brick_group.add(my_brick)
                my_brick.rect.y = y_pos
                my_brick.rect.x = x_pos
                main_window.blit(my_brick.image, my_brick.rect)
                x_pos += (BRICK_SEP + BRICK_WIDTH)
            x_pos = 0
            y_pos += BRICK_HEIGHT + BRICK_SEP

    my_paddle = paddle.Paddle(main_window, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_group.add(my_paddle)
    my_paddle.rect.x = APPLICATION_WIDTH / 2
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET


    my_ball = ball.Ball(RED, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = 200
    my_ball.rect.y = 200

    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                my_paddle.move(pygame.mouse.get_pos())

        main_window.fill(WHITE)

        my_ball.move()
        main_window.blit(my_ball.image, my_ball.rect)

        for a_brick in brick_group:
            main_window.blit(a_brick.image, a_brick.rect)

        my_ball.collide(paddle_group, brick_group)

        main_window.blit(my_paddle.image, my_paddle.rect)

        pygame.display.update()


main()
