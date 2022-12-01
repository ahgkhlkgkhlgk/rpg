import pygame as pg
from setting import *
from helper import res
import pygame.freetype

pg.init()
الشاشة=pg.display.set_mode((544,256))
pg.display.set_caption("الشاشة")
image=pg.image.load(res/"map"/"map.png")
image=pg.transform.scale(image,(544,256))
font=pg.freetype.Font(None,12)

index=0
for y in range(0,256,TILE_SIZE):
    for x in range(0,544,TILE_SIZE):
        font.render_to(image,(x+10,y+10),str(index))
        index+=1

v1=True
while v1 :
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            v1=False
    الشاشة.blit(image,(0,0))
    pg.display.flip()
