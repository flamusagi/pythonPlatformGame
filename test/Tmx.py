import os
import pickle

import pygame
import sys
import csv

from pytmx import load_pygame

from adventure.button import Button
from adventure.coin import Coin
from adventure.world import World
from adventure.switch import *
from adventure.platform import Platform
from player import *
from setup import *
from methods import *
from instance import *
pygame.init()

# 刷新关卡
def reset_level(level):
    player.__init__(100, screen_height - 130)
    world=reset(level)
    return world

player = Player(100, screen_height - 130)
score = 0


world_data = load_pygame("img/tsx/tmx/level1.tmx")
world = World(world_data)



run = True
pygame.init()
while run:

        clock.tick(fps)
        # 加载窗口背景
        # screen.blit(pine1_img, (0, 0))
        draw_bg()
        # night.play()
        if page_flag == 0:
            title_img = pygame.image.load("img/button/title.png")
            title_img = pygame.transform.scale(title_img, (700, 150))
            screen.blit(title_img, (17, 90))
            # night.play()
            if exit_button.draw(screen):
                run = False
            if start_button.draw(screen):
                page_flag = 2
            if menu_button.draw(screen):
                page_flag = 1

        elif page_flag == 1:
            screen.fill(BG)
            screen.blit(hint_img, (0, 0))
            draw_text("press space to back the menu", font_score, white, 225, 730)
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                page_flag = 0
        elif page_flag == 2:
            # vahalla.play()
            # 画地图
            world.draw(screen)

            # 显示敌人和岩浆
            if game_flag == 1:
                # 检测玩家与硬币的碰撞
                if pygame.sprite.spritecollide(player, coin_group, True):
                    coin_fx.play()
                    score += 1
                draw_text("X" + str(score), font_score, white, tile_size - 10, 10)
                lava_group.draw(screen)
                coin_group.draw(screen)
                exit_group.draw(screen)
                blob_group.draw(screen)
                platform_group.draw(screen)
                switch_group.draw(screen)
                blob_group.update(world)
                platform_group.update()


            # 显示玩家
            game_flag = player.update(screen,world,score,game_flag)

            # 还没通关的时候死掉了
            if game_flag == 0:
                # screen.fill(BG)
                # draw_text("LOL YOU DIED", font, red, (screen_width // 2) - 200, screen_height // 2 + 50)
                if death_count == 0:
                    screen.fill(color1)
                    draw_text("LOL YOU DIED", font, red, (screen_width // 2) - 200, screen_height // 2 + 50)
                    death_count += 1
                elif death_count == 1:
                    screen.fill(color2)
                    draw_text("LOL YOU DIED", font, red, (screen_width // 2) - 200, screen_height // 2 - 100)
                    death_count += 1

                elif death_count == 2:
                    screen.fill(color3)
                    img = font.render("LOL YOU DIED", True, red)
                    img = pygame.transform.rotate(img, 90)
                    screen.blit(img, (0, 0))
                    death_count += 1

                elif death_count == 3:
                    screen.fill(color4)
                    img = font.render("LOL YOU DIED", True, red)
                    img = pygame.transform.rotate(img, 90)
                    screen.blit(img, (700, 350))
                    death_count = 0
                if sound3:
                    pygame.mixer.init()
                    pygame.mixer.music.load(lol)
                    sound3 = False
                    sound1, sound2 = True, True
                if pygame.mixer.get_busy != 1:
                    pygame.mixer.music.play()
                if restart_button.draw(screen):
                    game_over_fx.stop()
                    if sound1:
                        pygame.mixer.init()
                        pygame.mixer.music.load(vahalla)
                        sound1 = False
                        sound2, sound3 = True, True
                    if pygame.mixer.get_busy != 1:
                        pygame.mixer.music.play()

                    player.__init__(100, screen_height - 130)
                    game_flag = 1
                    score = 0
                    world_data = []
                    world = reset_level(level)

            # 通过当前关卡
            if game_flag == 2:
                if level.getLevel() < level.getMaxLevel():
                    screen.fill(BG)
                    draw_text("you pass the " + str(level.getLevel()) + " level", font, white, 80, 300)
                    draw_text("press space to continue", font, white, 80, 350)
                if level.getLevel() == level.getMaxLevel():
                    screen.fill(BG)
                    draw_text("YOU WIN!", font, white, (screen_width // 2) - 142, screen_height // 2 - 100)
                    if restart_button.draw(screen):
                        page_flag = 0
                        sound2 = True
                        if sound2:
                            pygame.mixer.init()
                            pygame.mixer.music.load(night)
                            sound2 = False
                            sound1, sound3 = True, True
                        if pygame.mixer.get_busy != 1:
                            pygame.mixer.music.play()
                        level.setLevel(1,level.getMaxLevel())
                        world_data = []
                        world = reset_level(level)
                        game_flag = 1
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    if level.getLevel() < level.getMaxLevel():
                        if (level.getLevel() + 1) % 2 == 0:
                            if sound3:
                                pygame.mixer.init()
                                pygame.mixer.music.load(hope)
                                sound3 = False
                                sound1, sound2 = True, True
                        elif (level.getLevel() + 1) % 2 == 1:
                            if sound2:
                                pygame.mixer.init()
                                pygame.mixer.music.load(night)
                                sound2 = False
                                sound1, sound3 = True, True
                            if pygame.mixer.get_busy != 1:
                                pygame.mixer.music.play()
                        if pygame.mixer.get_busy != 1:
                            pygame.mixer.music.play()
                        pre=level.getLevel()
                        level.setLevel(pre+1,level.getMaxLevel())
                        score = 0
                        world_data = []
                        world = reset_level(level)
                        game_flag = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        pygame.display.update()

