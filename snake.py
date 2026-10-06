import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")

class GameSprite(pygame.sprite.Sprite):
    def __init__ (self, x, y, image_file):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
        



player = GameSprite(100, 100, "ipruebas/mario.png")



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    player.update()
    screen.blit(player.image, player.rect)
    pygame.display.update()