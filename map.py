import csv
import pygame as pg
from setting import *

class TileMap:
    def __init__(self,game,csv_pasth,image_pass,spacing=0):
        data_list = self._csv_to_list(csv_pasth)
        img_list=self._pars_image(image_pass,spacing)
        self._load_tiles(game,data_list,img_list)
    def _csv_to_list(self, csv_pasth):
        with open(csv_pasth)as f:
            reader=csv.reader(f)
            data=list(reader)
        return data

    def _pars_image(self, image_pass, spacing):
        image_list=[]
        image=pg.image.load(image_pass).convert()
        w,h=image.get_size()
        y=0
        for y in range(0,h,tile_size+spacing):
            for x in range(0, w, tile_size + spacing):
                tile=image.subsurface(x,y,tile_size,tile_size)
                image_list.append(tile)
        return image_list
    def _load_tiles(self,game,data_list,image_list):
        for i,megafon in enumerate(data_list):
            for j,holodilnik in enumerate(megafon):
                Tile(j,i,image_list[int(holodilnik)],game)
class Tile(pg.sprite.Sprite):
    def __init__(self,x,y,image,game):
        super().__init__(game.all_sprites)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x*tile_size
        self.rect.y=y*tile_size