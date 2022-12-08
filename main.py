import sys, pygame
import time


def main():
    pygame.init()

    # display size
    width, height = 1440, 890
    size = (width, height)

    # movement speed
    speed = [20, 0]

    black = 0, 0, 0

    # display (surface)
    screen = pygame.display.set_mode(size)

    # TODO: load snake image (rectangle)

    # array of snake body parts
    # snake_fig = []
    color = (255, 0, 0)

    def create_snake(snake_length: int = 3):
        """manually trying to append snake two times in below commneted code and it is working"""
        snake_width, snake_height = 15, 15
        snake_x, snake_y = 500, 250

        growth = 20
        snake_array = []
        for _ in range(snake_length):
            rect = pygame.Rect((snake_x + growth, snake_y), (snake_width, snake_height))
            snake_array.append(rect)
            growth += 20

        return snake_array

    # init snake
    snake = []
    snake_array = create_snake()
    for rect in snake_array:
        snake_part = pygame.draw.rect(screen, color, rect)
        snake.append(snake_part) 

    # moved snake
    temp_snake = []

    # FPS
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # TODO: snake collision with own tail
                # TODO: snake collision with edge of display

            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        for rect in snake:
            new_rect = rect.move(speed)
            pygame.draw.rect(screen, (255, 255, 255), new_rect)
            temp_snake.append(new_rect)

        snake = temp_snake
        temp_snake = []

        # render draw stuff
        pygame.display.update(snake)
        time.sleep(1)

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
        # screen.blit(screen, snake)
        pygame.display.flip()



if __name__ == "__main__":
    main()

