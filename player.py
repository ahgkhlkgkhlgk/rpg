import pygame as pg
from helper import *
from pygame.math import Vector2

class Player (pg.sprite.Sprite):
    # class for storing all the attributes related to the player
    speed=5
    def __init__(self,sprite_sheet_pasth,pos):
        # define for innitilaze required variables
        super().__init__()
        self.sprite_sheet=SpriteSheet(sprite_sheet_pasth)
        self.image=self.sprite_sheet.get_img(0,0,32,32)
        self.rect=self.image.get_rect()
        self.rect.center=pos
    def update(self):
        # update the player position
        self.move()
    def move(self):
        # moves the player in the directory
        keys=pg.key.get_pressed()
        self.vector=Vector2(0,0)
        if keys[pg.K_w]:
            self.vector.y=-1
        elif keys[pg.K_s]:
            self.vector.y=1
        elif keys[pg.K_a]:
            self.vector.x=-1
        elif keys[pg.K_d]:
            self.vector.x=1
        self.vector*=Player.speed
        self.rect.center+=self.vector