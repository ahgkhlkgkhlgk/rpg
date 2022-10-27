import pygame as pg
from setting import *
from player import Player as pl
from  helper import res

pg.init()
clock=pg.time.Clock()
screen=pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption(game_title)
player=pl(res/'sprite'/'t.png',(100,100))

all_sprites=pg.sprite.Group()
all_sprites.add(player)


running=True
while running :
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE):
            running=False

    player.update()

    screen.fill(BGClr)
    all_sprites.draw(surface=screen)
    clock.tick(fps)
    pg.display.flip()
