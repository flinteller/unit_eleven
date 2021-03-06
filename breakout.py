import pygame
import sys
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
    PADDLE_HEIGHT = 10
    PADDLE_WIDTH = 60
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    BLUE = (30, 144, 255)
    RED = (255, 48, 48)
    YELLOW = (255, 215, 0)
    GREEN =(0, 201, 87)
    WHITE = (255, 255, 255)

    pygame.init()
    main_window = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 32, 0)
    pygame.display.set_caption("AD Blocker")
    pygame.display.update()

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    brick_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    x_pos = 0
    y_pos = BRICK_Y_OFFSET

    # Places bricks with correct colors
    colors = [BLUE, RED, YELLOW, BLUE, GREEN]
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

    # Places ball and passes it parameters
    my_ball = ball.Ball(RED, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = 200
    my_ball.rect.y = 200

    # Places paddle and passes it parameters
    my_paddle = paddle.Paddle(main_window, GREEN, PADDLE_HEIGHT, PADDLE_WIDTH)
    paddle_group.add(my_paddle)
    my_paddle.rect.x = APPLICATION_WIDTH / 2
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    pygame.display.update()

    # Event detection loop
    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()
        if pygame.key.get_pressed()[K_LEFT]:
            my_paddle.move_left()
        if pygame.key.get_pressed()[K_RIGHT]:
            my_paddle.move_right()
        if pygame.key.get_pressed()[K_SPACE]:
            my_paddle.resize()
        if my_ball.rect.bottom > 590:
            NUM_TURNS -= 1
            pygame.mixer.init()
            pygame.init()
            sound = pygame.mixer.Sound("Error_sound.wav")
            sound.play()
            my_ball.rect.x = 200
            my_ball.rect.y = 20

        main_window.fill(WHITE)

        # Prints number of lives
        mouse_font = pygame.font.SysFont("Verdana", 32)
        mouse_label = mouse_font.render("Lives: " + str(NUM_TURNS), 1, BLUE)
        main_window.blit(mouse_label, (30, 30))
        pygame.display.update()

        # Prints message if you win
        if len(brick_group) == 0:
            mouse_font = pygame.font.SysFont("Verdana", 32)
            mouse_label = mouse_font.render("You Win!!!", 1, BLUE)
            main_window.blit(mouse_label, (135, 200))
            pygame.mixer.init()
            pygame.init()
            sound = pygame.mixer.Sound("Win_sound.wav")
            sound.play()
            pygame.display.update()

        if len(brick_group) == 0:
            pygame.time.wait(2000)
            break

        # Prints message if you loose
        if NUM_TURNS == 1 and my_ball.rect.bottom > 585:
            mouse_font = pygame.font.SysFont("Verdana", 32)
            mouse_label = mouse_font.render("Game Over", 1, RED)
            main_window.blit(mouse_label, (135, 200))
            pygame.mixer.init()
            pygame.init()
            sound = pygame.mixer.Sound("Game_over_sound.wav")
            sound.play()
            pygame.display.update()

        if NUM_TURNS == 0:
            pygame.time.wait(2000)
            break

        # Moves and blits ball
        my_ball.move()
        main_window.blit(my_ball.image, my_ball.rect)

        if my_ball.rect.bottom > my_ball.window_height:
            NUM_TURNS -= 1

        # Blits each brick
        for a_brick in brick_group:
            main_window.blit(a_brick.image, a_brick.rect)

        # Calls collision function
        my_ball.collide(paddle_group, brick_group)

        # Blits paddle
        main_window.blit(my_paddle.image, my_paddle.rect)

        pygame.display.update()


main()
