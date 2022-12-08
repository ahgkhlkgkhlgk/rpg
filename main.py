
import pygame as pg
from setting import *
from player import Player as pl
from helper import res
from map import TileMap
from camera import *

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        self.running = True
    def New_York(self):
        self.all_sprites=pg.sprite.LayeredUpdates()
        self.walls=pg.sprite.Group()
        self.map=TileMap(self,csv_pasth=res/"map"/"map.csv",image_pass=res/"map"/"map.png",image_tile_size=16)
        self.player = pl(self,res / 'sprite' / 't.png', (100, 100),self.map.height,self.map.width)
        # self.all_sprites.add(player)
        self.camera=Camera(self.map.width,self.map.height)
    def _events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE):
                self.running = False
    def _update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
    def _draw(self):
        # self.screen.fill(BGClr)
        # self.all_sprites.draw(surface=self.screen)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite.rect))
            # self.player_hitbox()
        pg.display.flip()
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self._events()
            self._update()
            self._draw()
    def player_hitbox(self):
        pg.draw.rect(self.screen,(0,180,0),rect=self.camera.apply(self.player.rect))
        self.screen.blit(self.player.image,self.camera.apply(self.player.rect))
        pg.draw.rect(self.screen, (0, 0, 0), rect=self.camera.apply(self.player.physical_body))

if __name__ == "__main__" :
    game=Game()
    game.New_York()
    game.run()
