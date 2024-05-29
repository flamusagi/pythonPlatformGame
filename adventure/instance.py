import pygame


from setup import *
from button import Button
from coin import Coin

blob_group = pygame.sprite.Group()
switch_group = pygame.sprite.Group()
door_group=pygame.sprite.Group()
lava_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()

# 按钮
restart_button = Button(300, 350, restart_img)
start_button = Button(300, 300, start_img)
menu_button = Button(300, 375, menu_img)
exit_button = Button(300, 450, exit_img)

# 关卡选择
level1=Button(100,200,level1_img)
level2=Button(300,200,level2_img)
level3=Button(500,200,level3_img)

# 显示虚拟硬币
score_coin = Coin(tile_size // 2, tile_size // 2)
coin_group.add(score_coin)

