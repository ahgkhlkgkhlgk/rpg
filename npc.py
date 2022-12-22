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
        self.talk=NPC_talk(game,(pos[0]-50,pos[1]-60),text="Hi there! Im wise mythical tree")
    def update(self):
        if self.rect.colliderect(self.game.player):
            self.talk.print()
        elif self.talk.groups():
            self.talk.reset()

class NPC_talk(pg.sprite.Sprite):
    def __init__(self,game,pos,text,font=None):
        self._layer=MassegeLayer
        super().__init__(game.all_sprites)
        self.text=text
        self.displayText=""
        self.arrow=0
        self.textPos=(10,10)
        self.font=pg.freetype.Font(font,16)
        testSurf,textRect=self.font.render(self.text)
        self.game=game
        self.image=pg.Surface((textRect.w+40,textRect.h+25),pg.SRCALPHA)
        self.rect=self.image.get_rect(center=pos)
        self.border=pg.Rect((0,0),self.rect.size)
        self.border.w=textRect.w+20
    def print(self):
        self.arrow+=0.2
        self.displayText=self.text[:int(self.arrow)]
        self.add(self.game.all_sprites)
        textSurf,textRect=self.font.render(self.displayText)
        self.image.fill((0,0,0,0))
        self.image.blit(textSurf,self.textPos)
        pg.draw.rect(self.image,(0,0,0),rect=self.border,width=5,border_radius=10)
        self.font.render_to(self.image,self.textPos,self.text)
    def reset(self):
        self.displayText=""
        self.arrow=0
        self.kill()