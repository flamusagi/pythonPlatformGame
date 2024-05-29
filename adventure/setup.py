import pygame

from adventure.level import Level, Complete

pygame.init()
clock = pygame.time.Clock()
fps = 60

# 游戏基础配置的变量
bg_scroll = 0
game_flag = 1
main_menu = True
page_flag = 0
play=[0,0,0,0]
level=Level(1,3)
complete=Complete(0,6)
# score = 0
death_count = 0
win_count = 0
screen_width = 750
screen_height = 750
tile_size = 50
cols=15

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("kuso game")


# 定义字体
font_score = pygame.font.SysFont("Old English Text MT", 30)
font = pygame.font.SysFont("Old English Text MT", 75)

# 定义文字颜色
white = (255, 255, 255)
red = (255, 0, 0)
BG = (144, 201, 120)
blue = (100, 108, 217)
color1 = (144, 201, 120)
color2 = (96, 175, 255)
color3 = (255, 149, 43)
color4 = (184, 113, 255)

# 设置显示文字变量

# 加载图片
bg_img = pygame.image.load("img/background/sky.png")
pine1_img = pygame.image.load("img/background/pine1.png").convert_alpha()
pine2_img = pygame.image.load("img/background/pine2.png").convert_alpha()
mountain_img = pygame.image.load("img/background/mountain.png").convert_alpha()
sky_img = pygame.image.load("img/background/sky_cloud.png").convert_alpha()
restart_img = pygame.image.load("img/button/restart_btn.png")
start_img = pygame.image.load("img/button/start_btn.png")
exit_img = pygame.image.load("img/button/exit_btn.png")
subexit_img=pygame.image.load("img/exit/subexit.png")
menu_img = pygame.image.load("img/button/menu.png")
hint_img = pygame.image.load("img/button/hint.png")
dirt_img = pygame.image.load('img/tile/dirt.png')
grass_img = pygame.image.load('img/tile/grass.png')
blob_img = pygame.image.load('img/enemy/blob.png')
platform_x_img = pygame.image.load('img/platform/platform_x.png')
platform_y_img = pygame.image.load('img/platform/platform_y.png')
lava_img = pygame.image.load('img/lava/lava.png')
thorn_img = pygame.image.load('img/lava/thorn.png')
coin_img = pygame.image.load('img/coin/coin.png')
save_img = pygame.image.load('img/button/save_btn.png')
load_img = pygame.image.load('img/button/load_btn.png')
ghost_img=pygame.image.load('img/enemy/ghost.png')
switch_img=pygame.image.load('img/switch/switch.png')
door_img=pygame.image.load('img/switch/door1.png')
doo_img=pygame.image.load('img/switch/door2.png')
level1_img=pygame.image.load('level/1.png')
level2_img=pygame.image.load('level/2.png')
level3_img=pygame.image.load('level/3.png')
level4_img=pygame.image.load('level/4.png')
level5_img=pygame.image.load('level/5.png')

# 定义3个变量来表示是否在播放哪首音乐
sound1, sound2, sound3 = True, True, True
night = "music/night.mp3"
vahalla = "music/vahalla.mp3"
hope = "music/hope.mp3"
lol = "music/lol.mp3"
# 加载初始背景音乐
pygame.mixer.music.load(night)
pygame.mixer.music.play()
# 音效
coin_fx = pygame.mixer.Sound("music/coin.wav")
coin_fx.set_volume(0.8)
jump_fx = pygame.mixer.Sound("music/jump.wav")
jump_fx.set_volume(0.7)
game_over_fx = pygame.mixer.Sound("music/lol.mp3")
game_over_fx.set_volume(0.6)