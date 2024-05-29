import pygame

# 创建敌人
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img = pygame.image.load("img/enemy/blob.png")
        self.image=img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.counter=0
        self.direction=1
        self.in_air = True


    def update(self,world):
        self.rect.x+=self.direction
        self.counter+=1
        if abs(self.counter)>50:
            self.direction*=-1
            self.counter*=-1

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img = pygame.image.load("img/enemy/ghost.png")
        self.image=img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x=5
        self.speed_y=5
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.counter=0
        self.direction=1
        self.in_air = True
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def update(self,world):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # If the sprite goes off the edge of the screen,
        # make it move in the opposite direction

        if self.rect.x > 750.0 - self.width:
            self.speed_x = 0.0 - self.speed_x
            self.rect.x = 750.0 - self.width
        elif self.rect.x < 0:
            self.speed_x = -self.speed_x
            self.rect.x = 0
        if self.rect.y > 750.0 - self.height:
            self.speed_y = -self.speed_y
            self.rect.y = 750.0 - self.height
        elif self.rect.y < 0:
            self.speed_y = -self.speed_y
            self.rect.y = 0

class Thorn(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        tile_size=50
        img = pygame.image.load("img/lava/thorn.png")
        self.image=img
        # self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self,world):
        self.rect.y += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
