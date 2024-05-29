import pygame
from setup import *
from instance import *

# 创建玩家
class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        # 人物行走动画
        for num in range(1, 5):
            img_right = pygame.image.load(f"img/guy/guy{num}.png")
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.dead_image = pygame.image.load("img/enemy/ghost.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True

    def control(self,dx):
        # 按键
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.jumped == False and self.in_air == False:
            jump_fx.play()
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_w] == False:
            self.jumped = False
        if key[pygame.K_a]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_d]:
            dx += 5
            self.counter += 1
            self.direction = 1

        if key[pygame.K_a] == False and key[pygame.K_d] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        return dx

    def animation_effect(self):
        # 播放动画
        if self.counter > 5:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

    def gravity(self,dy):
        # 重力 跳跃后 自然下落
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y
        return dy

    def update(self,screen,world,score,game_flag):
        dx = 0
        dy = 0
        # 获取按键事件
        if game_flag==1:
            dx=self.control(dx)
            self.animation_effect()
            dy=self.gravity(dy)
            self.in_air=True
            # 检测玩家与每个泥块与草地的碰撞
            for tile in world.tile_list:
                # 判断玩家在x方向上的碰撞
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # 检测玩家在y方向的碰撞
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # 检测玩家顶部与泥块底部碰撞
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # 检测玩家底部与泥块顶部的碰撞
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air=False
                # 玩家与敌人的碰撞
                if pygame.sprite.spritecollide(self, blob_group, False):
                    # pygame.mixer.music.stop()
                    game_over_fx.play()
                    game_flag = 0

                # 玩家与熔岩的碰撞
                if pygame.sprite.spritecollide(self, lava_group, False):
                    # pygame.mixer.music.stop()
                    game_over_fx.play()
                    game_flag = 0

                # 玩家与出口的碰撞
                if pygame.sprite.spritecollide(self, exit_group, False) and score >= 3:
                    game_flag = 2

                # 玩家与开关的碰撞
                if pygame.sprite.spritecollide(self, switch_group, True):
                    door_group.empty()

            # 玩家与移动平台的碰撞
            for platform in platform_group:
                # 检测玩家与块x方向上的碰撞
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # 检测玩家与块y方向上的碰撞
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # # 检测与顶部的碰撞
                    # if abs((self.rect.top + dy) - platform.rect.bottom) < 15:
                    #     self.vel_y = 0
                    #     dy = platform.rect.bottom - self.rect.top
                    # 检测与底部的碰撞
                    if abs((self.rect.bottom + dy) - platform.rect.top) < 15:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0
                        # 判断是否与平台一起动
                        if platform.move_x != 0:
                            self.rect.x += platform.move_direction
            # 更新玩家的位置
            self.rect.x += dx
            self.rect.y += dy

            #边界
            screen_height = 750
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                dy = 0
            if self.rect.x > screen_height:
                dx = 0
                self.rect.x-=50
            elif self.rect.x<0:
                dx = 0
                self.rect.x+=50
            if self.rect.y > screen_height:
                dy = 0
                self.rect.y -= 50

        # # 玩家死亡的显示
        # elif game_flag == 0:
        #     self.image = self.dead_image
        #     self.rect.y -= 5

        # 把玩家画到屏幕上
        screen.blit(self.image, self.rect)

        return game_flag


