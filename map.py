import csv
import pygame as pg
from setting import *

class TileMap:
    def __init__(self,csv_pasth,image_pass,spacing=0):
        data_list = self._csv_to_list(csv_pasth)
        img_list=self._pars_image(image_pass,spacing)
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