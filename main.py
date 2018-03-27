import pygame as pg
from settings import *
from box import *
import math

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((width,height))

clock = pg.time.Clock()

screen.fill(bg)



while running:
	all_sprites = pg.sprite.Group()
	x,y = pg.mouse.get_pos()
	posx = (math.floor(x/32)*32)
	posy = (math.floor(y/32)*32)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		elif event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				mouse = 1
			elif event.button == 3:
				mouse = 3
			elif event.button == 2:
				mouse = 2
		elif event.type == pg.MOUSEBUTTONUP:
			mouse = 0
				
	if mouse == 1:
		box = Box(blue,posx,posy,True)
		all_sprites.add(box)
	elif mouse == 3:
		blank = Box(bg,posx,posy,False)
		all_sprites.add(blank)
	elif mouse == 2:
		pass
	all_sprites.draw(screen)
	all_sprites.update()
	pg.display.update()
	clock.tick(60)

pg.quit()
quit()

