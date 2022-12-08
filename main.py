import pygame
import sys

def main():
    pygame.init()

    # display size
    width, height = 1440, 890
    size = (width, height)

    # movement speed
    speed = [1, 1]

    black = 0, 0, 0

    # display (surface)
    screen = pygame.display.set_mode(size)

    # TODO: load snake image (rectangle)
    #snake = pygame.image.load("intro_ball.gif")

    color = (255, 0, 0)

    # snake location
    snake_x, snake_y = 50, 50

    # snake size
    snake_width, snake_height = 10, 10

    rect = pygame.Rect(snake_x, snake_y, snake_width, snake_height)

    snake = pygame.draw.rect(screen, color, rect)
    
    # get image into rectangle
    #ballrect = ball.get_rect()

    # FPS
    while True:
        # Monitoring events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("Key Q has been pressed")
                    pygame.quit()
                    sys.exit()

                # TODO: snake collision with own tail
                # TODO: snake collision with edge of display
                # pygame.draw.rect(screen,color,[200,150,10,10])

        pygame.display.update(snake)

    #     ballrect = ballrect.move(speed)
    #
    #     # collision within x axis
    #     if ballrect.left < 0 or ballrect.right > width:
    #         # direction
    #         speed[0] = -speed[0]
    #
    #     # collision within y axis
    #     if ballrect.top < 0 or ballrect.bottom > height:
    #         # direction
    #         speed[1] = -speed[1]
    #
    #     # randomly create food (circles)
    #     # when head of snake eats food, grow +1
    #
        # screen.fill(black)
        # screen.blit(screen, snake)
        # pygame.display.flip()


if __name__ == "__main__":
    main()
