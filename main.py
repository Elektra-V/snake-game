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
    snake_fig = []
    color = (255, 0, 0)
    snake_width, snake_height = 5, 5
    snake_x, snake_y = 500, 250
    rect = pygame.Rect((snake_x,snake_y),(snake_width, snake_height))
    snake = pygame.draw.rect(screen, color, rect)

    """ manually trying to append snake two times in below commneted code and it is working"""
    # rect2 = pygame.Rect((snake_x+10,snake_y),(snake_width, snake_height))
    # snake2 = pygame.draw.rect(screen, color, rect2)
    # snake_fig.append(snake)
    # snake_fig.append(snake2)

    while len(snake_fig) < 3:
        snake_fig.append(snake)
        snake_x += 10
        print(snake_x)
    return snake_fig

    # get image into rectangle
    #ballrect = ball.get_rect()

    # FPS
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # TODO: snake collision with own tail
                # TODO: snake collision with edge of display
                #pygame.draw.rect(screen,color,[200,150,10,10])    
            if event.type == pygame.KEYDOWN:    
            # checking if key "A" was pressed
                if event.key == pygame.K_q:
                    #print("x is pressed")
                    pygame.quit()
                    sys.exit()
        pygame.display.update(snake_fig)
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
        #screen.fill(black)
        #screen.blit(screen, snake)
        #pygame.display.flip()


if __name__ == "__main__":
    main()
