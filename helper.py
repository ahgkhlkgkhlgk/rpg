import pygame as pg
import sys
from pathlib import Path

class SpriteSheet:
    def __init__(self,file_pass,scale=1):
        sheet=pg.image.load(file_pass).convert_alpha()
        w,h=sheet.get_size()
        target_size=(int(w*scale),int(h*scale))
        self.sheet=pg.transform.scale(sheet,target_size)
        self.w,self.h=self.sheet.get_size()
    def get_image(self,x,y,width,height):
        return self.sheet.subsurface(x,y,width,height)

res=Path(sys.argv[0]).parent/'res'