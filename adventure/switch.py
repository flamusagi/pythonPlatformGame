import pygame

class Switch(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        tile_size = 50
        img = pygame.image.load("img/switch/switch.png")
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        tile_size = 50
        img = pygame.image.load("img/switch/door1.png")
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Doo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        tile_size = 50
        img = pygame.image.load("img/switch/door2.png")
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y