import pygame as pg
from setting import*

class NPC(pg.sprite.Sprite):
    def __init__(self,game,image,pos):
        self._layer= group_layer
        groups = game.all_sprites,game.walls
        super().__init__(groups)
        self.image=image
        self.rect=self.image.get_rect(center=pos)
    def update(self):
        pass