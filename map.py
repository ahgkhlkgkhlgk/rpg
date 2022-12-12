import csv
import pygame as pg
from setting import *

class TileMap:
    WALL_ID=[7,8,9,10,11,12,13,14,15,16,
             24,25,26,27,28,29,30,31,32,33,
             41,42,43,44,45,46,47,48,49,50,
             61,64,65,66,67,
             80,
             92,93,94,95,96,97,98,99,100,
             107,108,109,110,111,112,113,114,115,116,117,
             126,127,128,129,130,131,132,133,134,135]
    NPC_ID=[119,120,121,122,123,124,125]
    def __init__(self,game,csv_pasth,image_tile_size,image_pass,spacing=0):
        data_list = self._csv_to_list(csv_pasth)
        self.img_list=self._pars_image(image_pass,spacing,image_tile_size)
        self._load_tiles(game,data_list,self.img_list)
        self.width=len(data_list[0])*TILE_SIZE
        self.height=len(data_list)*TILE_SIZE
    def _csv_to_list(self, csv_pasth):
        with open(csv_pasth)as f:
            reader=csv.reader(f)
            data=list(reader)
        return data
    def _pars_image(self, image_pass, spacing,image_tile_size):
        image_list=[]
        image=pg.image.load(image_pass).convert()
        if image_tile_size != TILE_SIZE :
            scale=TILE_SIZE//image_tile_size
            spacing*=scale
            currrent_size=image.get_size()
            target_size=tuple(i*scale for i in currrent_size)
            image=pg.transform.scale(image, target_size)
        w,h=image.get_size()
        y=0
        for y in range(0, h, TILE_SIZE + spacing):
            for x in range(0, w, TILE_SIZE + spacing):
                tile=image.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                image_list.append(tile)
        return image_list
    def _load_tiles(self,game,data_list,image_list):
        for i,megafon in enumerate(data_list):
            for j,holodilnik in enumerate(megafon):
                if int(holodilnik) in TileMap.WALL_ID:
                    collide=True
                else:
                    collide = False
                Tile(j,i,image_list[int(holodilnik)],game,collide)
class Tile(pg.sprite.Sprite):
    def __init__(self,x,y,image,game,wall_collide=False):
        self._layer = group_layer
        if wall_collide :
            groups=game.all_sprites,game.walls
        else:
            groups=game.all_sprites
        super().__init__(groups)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x= x * TILE_SIZE
        self.rect.y= y * TILE_SIZE
