import sys, pygame

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
    rect = pygame.Rect(30, 30, 80, 80)
    snake = pygame.draw.rect(screen, color, rect)
    
    # get image into rectangle
    #ballrect = ball.get_rect()

    # FPS
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # TODO: snake collision with own tail
                # TODO: snake collision with edge of display
                #pygame.draw.rect(screen,color,[200,150,10,10])
                pygame.display.update(snake)
        sys.exit()      

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
        screen.fill(black)
        screen.blit(screen, snake)
        pygame.display.flip()


if __name__ == "__main__":
    main()
