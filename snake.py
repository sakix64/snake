import random
import sys
import time
import pygame


pygame.init()


frame_size_x = 800
frame_size_y = 600
window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("Snake game")


fps = pygame.time.Clock()
speed = 15

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)


square_size = 20


def init_vars():
    global snake_position, snake_body, food_pos, food_spawn, direction, score
    
    snake_position = [100, 500]
    snake_body = [[100, 500], [80, 500], [60, 500]]

    food_pos = [
        random.randrange(0, (frame_size_x // square_size)) * square_size,
        random.randrange(0, (frame_size_y // square_size)) * square_size,
    ]
    food_spawn = True
    direction = "RIGHT"
    score = 0


init_vars()


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(score), True, color)
    score_rect = score_surface.get_rect()

    if choice == 1:
        score_rect.midtop = (frame_size_x // 10, 15)
    else:
        score_rect.midtop = (frame_size_x // 2, int(frame_size_y / 1.25))

    
    window.blit(score_surface, score_rect)


def game_over():
    my_font = pygame.font.SysFont("arial", 50)
    game_over_surface = my_font.render(
        "GAME OVER - Score: " + str(score), True, red
    )
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x // 2, frame_size_y // 4)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"

    # Movimiento
    if direction == "UP":
        snake_position[1] -= square_size
    elif direction == "DOWN":
        snake_position[1] += square_size
    elif direction == "RIGHT":
        snake_position[0] += square_size
    elif direction == "LEFT":
        snake_position[0] -= square_size

    
    snake_body.insert(0, list(snake_position))

    
    if (
        snake_position[0] == food_pos[0]
        and snake_position[1] == food_pos[1]
    ):
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [
            random.randrange(0, (frame_size_x // square_size)) * square_size,
            random.randrange(0, (frame_size_y // square_size)) * square_size,
        ]
        food_spawn = True

    window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(
            window,
            green,
            pygame.Rect(pos[0], pos[1], square_size - 1, square_size - 1),
        )

    pygame.draw.rect(
        window,
        red,
        pygame.Rect(
            food_pos[0], food_pos[1], square_size - 1, square_size - 1
        ),
    )

    if (
        snake_position[0] <= 0
        or snake_position[0] > frame_size_x
        or snake_position[1] <= 0
        or snake_position[1] > frame_size_y
    ):
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, "arial", 20)
    pygame.display.update()
    fps.tick(speed)

pygame.quit()
sys.exit()