import pygame
from instance import *
# 创建地图类
class World(object):
    def __init__(self, data):
        self.tile_list = []
        tile_size = 50
        #加载图片

        dirt_img = pygame.image.load("img/tile/dirt.png")
        grass_img = pygame.image.load("img/tile/grass.png")
        # for group in data.objectgroups:
        #     if group.name=="dirt":
        #      for obj in group:
        #         img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
        #         img_rect = img.get_rect()
        #         img_rect.x = obj.x
        #         img_rect.y = obj.y
        #         tile = (img, img_rect)
        #         self.tile_list.append(tile)
        #     if group.name=="grass":
        #      for obj in group:
        #         img = pygame.transform.scale(grass_img, (tile_size, tile_size))
        #         img_rect = img.get_rect()
        #         img_rect.x = obj.x
        #         img_rect.y = obj.y
        #         tile = (img, img_rect)
        #         self.tile_list.append(tile)
        #     if group.name == "enemy":
        #       for obj in group:
        #             from adventure.enemy import Enemy
        #             blob = Enemy(obj.x, obj.y)
        #             blob_group.add(blob)
        #     if group.name == "platformx":
        #         for obj in group:
        #             from adventure.platform import Platform
        #             platform = Platform(obj.x, obj.y, 1, 0)
        #             platform_group.add(platform)
        #     if group.name == "platformy":
        #         for obj in group:
        #             from adventure.platform import Platform
        #             platform = Platform(obj.x, obj.y, 0, 1)
        #             platform_group.add(platform)
        #     if group.name == "lava":
        #         for obj in group:
        #             from adventure.lava import Lava
        #             lava = Lava(obj.x, obj.y)
        #             lava_group.add(lava)
        #     if group.name == "coin":
        #         for obj in group:
        #             from adventure.coin import Coin
        #             coin = Coin(obj.x, obj.y)
        #             coin_group.add(coin)
        #     if group.name == "exit":
        #         for obj in group:
        #             from adventure.exit import Exit
        #             exit = Exit(obj.x, obj.y)
        #             exit_group.add(exit)
        #     if group.name == "ghost":
        #         for obj in group:
        #             from adventure.enemy import Ghost
        #             ghost = Ghost(obj.x, obj.y)
        #             blob_group.add(ghost)
        #     if group.name == "thorn":
        #         for obj in group:
        #             from adventure.enemy import Thorn
        #             thorn =Thorn(obj.x, obj.y)
        #             blob_group.add(thorn)
        #     if group.name == "switch":
        #         for obj in group:
        #             from adventure.switch import Switch
        #             switch=Switch(obj.x, obj.y)
        #             switch_group.add(switch)
        #     if group.name == "door":
        #         for obj in group:
        #             from adventure.switch import Door
        #             door=Door(obj.x, obj.y)
        #             door_group.add(door)
        #     if group.name == "doo":
        #         for obj in group:
        #             from adventure.switch import Doo
        #             doo=Doo(obj.x, obj.y)
        #             door_group.add(doo)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile > 0:
                    if tile == 1:
                        img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = x * tile_size
                        img_rect.y = y * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    elif tile == 2:
                        img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = x * tile_size
                        img_rect.y = y * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    elif tile == 3:
                        from adventure.enemy import Enemy
                        blob = Enemy(x * tile_size, y * tile_size+15)
                        blob_group.add(blob)
                    elif tile == 4:
                        from adventure.platform import Platform
                        platform = Platform(x * tile_size, y * tile_size, 1, 0)
                        platform_group.add(platform)
                    elif tile == 5:
                        from adventure.platform import Platform
                        platform = Platform(x * tile_size, y * tile_size, 0, 1)
                        platform_group.add(platform)
                    elif tile == 6:
                        from adventure.lava import Lava
                        lava = Lava(x * tile_size, y * tile_size + (tile_size // 2))
                        lava_group.add(lava)
                    elif tile == 7:
                        from adventure.coin import Coin
                        coin = Coin(x * tile_size + (tile_size // 2), y * tile_size + (tile_size // 2))
                        coin_group.add(coin)
                    elif tile == 8:
                        from adventure.exit import Exit
                        exit = Exit(x * tile_size, y * tile_size)
                        exit_group.add(exit)
                    elif tile == 9:
                        from adventure.enemy import Ghost
                        ghost = Ghost(x * tile_size, y * tile_size + 15)
                        blob_group.add(ghost)
                    elif tile == 10:
                        from adventure.enemy import Thorn
                        thorn =Thorn(x * tile_size, y * tile_size + (tile_size // 2))
                        blob_group.add(thorn)
                    elif tile==11:
                        from adventure.switch import Switch
                        switch=Switch(x * tile_size, y * tile_size)
                        switch_group.add(switch)
                    elif tile==12:
                        from adventure.switch import Door
                        door=Door(x * tile_size, y * tile_size)
                        door_group.add(door)
                    elif tile==13:
                        from adventure.switch import Doo
                        doo=Doo(x * tile_size, y * tile_size)
                        door_group.add(doo)


    def draw(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


