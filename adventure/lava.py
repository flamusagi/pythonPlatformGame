import pygame

# 创建熔岩
class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        tile_size = 50
        img = pygame.image.load("img/lava/lava.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

