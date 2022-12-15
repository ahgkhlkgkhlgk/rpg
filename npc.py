import pygame as pg
from setting import*
import pygame.freetype

class NPC(pg.sprite.Sprite):
    def __init__(self,game,image,pos):
        self._layer= group_layer
        self.game=game
        groups = game.all_sprites,game.walls
        super().__init__(groups)
        self.image=image
        self.rect=self.image.get_rect(center=pos)
        self.talk=NPC_talk(game,(pos[0]-50,pos[1]-60),text="Hi there!\nIm wise mythical tree")
    def update(self):
        if self.rect.colliderect(self.game.player):
            if not self.talk.groups():
                self.talk.add(self.game.all_sprites)
                self.talk.print()
        elif self.talk.groups():
            self.talk.kill()

class NPC_talk(pg.sprite.Sprite):
    def __init__(self,game,pos,text,font=None):
        self._layer=MassegeLayer
        super().__init__(game.all_sprites)
        self.image=pg.Surface((200,128),pg.SRCALPHA)
        self.rect=self.image.get_rect(topleft=pos)
        self.border=pg.Rect((0,0),self.rect.size)
        self.text=text
        self.displayText=""
        self.arrow=0
        self.textPos=(10,10)
        self.font=pg.freetype.Font(font,16)
        testSurf,textRect=self.font.render(self.text)
    def print(self):
        pg.draw.rect(self.image,(255,255,255),rect=self.border,width=5,border_radius=10)
        self.font.render_to(self.image,self.textPos,self.text)
