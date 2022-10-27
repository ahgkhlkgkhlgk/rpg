import pygame as pg
import sys
from pathlib import Path

class SpriteSheet:
    def __init__(self,file_pass):
        self.sheet=pg.image.load(file_pass).convert_alpha()
    def get_img(self,x,y,width,height):
        return self.sheet.subsurface(x,y,width,height)

res=Path(sys.argv[0]).parent/'res'