import pygame as pg
from setting import *
from player import Player as pl
from helper import res
from map import TileMap

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((screen_width, screen_height))
        pg.display.set_caption(game_title)
        self.running = True
    def New_York(self):
        player = pl(res / 'sprite' / 't.png', (100, 100))
        self.all_sprites=pg.sprite.Group()
        self.all_sprites.add(player)
        self.map=TileMap(csv_pasth=res/"map"/"map.csv",image_pass=res/"map"/"map.png")
    def _events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE):
                self.running = False
    def _update(self):
        self.all_sprites.update()
    def _draw(self):
        self.screen.fill(BGClr)
        self.all_sprites.draw(surface=self.screen)
        pg.display.flip()
    def run(self):
        while self.running:
            self.clock.tick(fps)
            self._events()
            self._update()
            self._draw()

if __name__ == "__main__" :
    game=Game()
    game.New_York()
    game.run()