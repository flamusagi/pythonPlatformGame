import csv

import pygame
import pickle
from os import path
from setup import *
from methods import *
from button import Button

pygame.init()

clock = pygame.time.Clock()
fps = 60

tile_size = 50
cols = 15
margin = 100
bg_scroll=0
screen_width = tile_size * cols
screen_height = (tile_size * cols) + margin

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Editor')


clicked = False
level = 1

font = pygame.font.SysFont('Futura', 24)
world_data = []


save_button = Button(screen_width // 2 - 150, screen_height - 80, save_img)
load_button = Button(screen_width // 2 + 50, screen_height - 80, load_img)


run = True
while run:

	clock.tick(fps)
	screen.fill(BG)
	draw_bg()
	#save and load
	if save_button.draw(screen):
		if path.exists(f'level_data/level{level}_data'):
			pickle_out = open(f'level_data/level{level}_data', 'wb')
			pickle.dump(world_data, pickle_out)
			pickle_out.close()
	if load_button.draw(screen):
		if path.exists(f'level_data/level{level}_data'):
			pickle_in = open(f'level_data/level{level}_data', 'rb')
			world_data = pickle.load(pickle_in)

	draw_grid()
	draw_world(world_data)


	draw_text(f'Level: {level}', font, white, tile_size, screen_height - 60)
	draw_text('up or down to change level', font, white, tile_size, screen_height - 40)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		# 如果按键 处理事件
		elif event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
			pos = pygame.mouse.get_pos()
			x = (int)(pos[0] / tile_size)
			y = (int)(pos[1] / tile_size)
			if x < cols and y < cols:
				if pygame.mouse.get_pressed()[0] == 1:
					world_data[y][x] += 1
					if world_data[y][x] > 13:
						world_data[y][x] = 0
		# 如果现在按键 恢复事件
		elif event.type == pygame.MOUSEBUTTONUP:
			clicked = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				level += 1
			elif event.key == pygame.K_DOWN and level > 1:
				level -= 1
	pygame.display.update()


pygame.quit()