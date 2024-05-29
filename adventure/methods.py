import os
import pickle
import csv


from world import World
from instance import *
from setup import *

# 显示文本信息
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

# 画背景
def draw_bg():
    screen.blit(bg_img,(0,0))

# 刷新关卡
def reset(level):
    # player.__init__(100, screen_height - 130)
    # TypeError: module() argument 1 must be str, not int
    blob_group.empty()
    lava_group.empty()
    exit_group.empty()
    platform_group.empty()
    switch_group.empty()
    coin_group.empty()
    door_group.empty()

    # 加载并且创建地图
    world_data = []
    # # 数组初始化 不能写到循环内部 否则会一直写
    # for row in range(cols):
    #     r = [0] * cols
    #     world_data.append(r)
    #
    # with open(f"level_data/level{level}.csv", newline="") as csvfile:
    #     reader = csv.reader(csvfile, delimiter=",")
    #     for y, row in enumerate(reader):
    #         for x, tile in enumerate(row):
    #             world_data[y][x] = int(tile)
    if os.path.exists(f"./level_data/level{level.getLevel()}_data"):
        pickle_in = open(f"level_data/level{level.getLevel()}_data", "rb")
        world_data = pickle.load(pickle_in)
    world = World(world_data)

    return world

#画竖线和横线达到分割的目的
def draw_grid():
    for c in range(cols+1):
        pygame.draw.line(screen, white, (c * tile_size, 0), (c * tile_size, screen_height))
        pygame.draw.line(screen, white, (0, c * tile_size), (screen_width, c * tile_size))

def draw_world(world_data):
    # for row in range(cols):
    #     r = [0] * cols
    #     world_data.append(r)
    for row in range(cols):
        r = [0] * cols
        world_data.append(r)
    for row in range(cols):
        for col in range(cols):
            if world_data[row][col] > 0:
                if world_data[row][col] == 1:
                    #dirt blocks
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 2:
                    #grass blocks
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 3:
                    #enemy blocks
                    img = pygame.transform.scale(blob_img, (tile_size, int(tile_size * 0.75)))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size * 0.25)))
                elif world_data[row][col] == 4:
                    #horizontally moving platform
                    img = pygame.transform.scale(platform_x_img, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 5:
                    #vertically moving platform
                    img = pygame.transform.scale(platform_y_img, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 6:
                    #lava
                    img = pygame.transform.scale(lava_img, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))
                elif world_data[row][col] == 7:
                    #coin
                    img = pygame.transform.scale(coin_img, (tile_size // 2, tile_size // 2))
                    screen.blit(img, (col * tile_size + (tile_size // 4), row * tile_size + (tile_size // 4)))
                elif world_data[row][col] == 8:
                    #button
                    img = pygame.transform.scale(subexit_img, (tile_size,tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 9:
                    #enemy blocks
                    img = pygame.transform.scale(ghost_img, (tile_size, int(tile_size * 0.75)))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size * 0.25)))
                elif world_data[row][col] == 10:
                    #lava
                    img=thorn_img
                    # img = pygame.transform.scale(thorn_img, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))
                elif world_data[row][col] == 11:
                    #dirt blocks
                    img = pygame.transform.scale(switch_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 12:
                    #dirt blocks
                    img = pygame.transform.scale(door_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 13:
                    #dirt blocks
                    img = pygame.transform.scale(doo_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))