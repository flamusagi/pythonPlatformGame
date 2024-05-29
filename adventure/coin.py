import pygame

#创建金币
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        tile_size = 50
        img = pygame.image.load("img/coin/coin.png")
        self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)