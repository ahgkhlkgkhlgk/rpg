import pygame as pg
from helper import *
from pygame.math import Vector2
from setting import *

class Player (pg.sprite.Sprite):
    # class for storing all the attributes related to the player
    speed=5
    def __init__(self,game,sprite_sheet_pasth,pos):
        # define for innitilaze required variables
        self._layer=Player_Layer
        super().__init__(game.all_sprites)
        self.sprite_sheet=SpriteSheet(sprite_sheet_pasth,1.5)
        self._load_images(self.sprite_sheet)
        self.image=self.walk_right[0]
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.last_update=0
        self.frame=0
        self.vector = Vector2(1, 0)
        self.loop_len=4
    def update(self):
        # update the player position
        self._move()
        self._animate()
    def _move(self):
        # moves the player in the directory
        keys=pg.key.get_pressed()
        step=2 if keys[pg.K_LSHIFT] else 1
        self.vector=Vector2(0,0)
        if keys[pg.K_w]:
            self.vector.y=-1*step
        elif keys[pg.K_s]:
            self.vector.y=1*step
        elif keys[pg.K_a]:
            self.vector.x=-1*step
        elif keys[pg.K_d]:
            self.vector.x=1*step
        self.vector*=Player.speed
        self.rect.center+=self.vector
        # self._restrain()
    def _load_images(self, sheet):
        self.walk_right=[]
        self.walk_left=[]
        self.walk_backward=[]
        self.walk_forward=[]
        x=0
        w,h=sheet.w//4,sheet.h//4
        for x in range(0,w*4,w):
            self.walk_forward.append(sheet.get_image(x,0,w,h))
            self.walk_left.append(sheet.get_image(x,h,w,h))
            self.walk_right.append(sheet.get_image(x,h*2,w,h))
            self.walk_backward.append(sheet.get_image(x,h*3,w,h))
    def _restrain(self):
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0
    def _animate(self,frame_len=100):
        now=pg.time.get_ticks()
        self.animation_loop=[]
        if now - self.last_update>frame_len and self.vector.length() > 0:
            self.last_update=now
            if self.vector.x > 0:
                self.animation_loop=self.walk_right
            if self.vector.x < 0:
                self.animation_loop=self.walk_left
            if self.vector.y > 0:
                self.animation_loop=self.walk_forward
            if self.vector.y < 0:
                self.animation_loop=self.walk_backward
            self.frame=(self.frame+1)%self.loop_len
            self.image=self.animation_loop[self.frame]