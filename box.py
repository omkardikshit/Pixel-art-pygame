import pygame as pg

class Box(pg.sprite.Sprite):
	def __init__(self,color,x,y,solid):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((32,32))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
