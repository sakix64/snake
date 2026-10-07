import pygame
import time
import random

speed = 15

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)


fps = pygame.time.Clock()

#window size

frame_size_x = 800
frame_size_y = 600


#initialize window
pygame.display.set_caption("Snake game")
window = pygame.display.set_mode((frame_size_x, frame_size_y))


# check error
check_error = pygame.init()
if check_error[1] > 0:
    print("Error"+ check_error[1])
else:
    print("Iniciado correctamente")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    window.update()
    fps.tick(speed)













