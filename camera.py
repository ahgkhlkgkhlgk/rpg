from  setting import*

class Camera:
    def __init__(self):
        self.offset=(0,0)
    def apply(self,entity):
        return entity.rect.move(self.offset)
    def update(self,target):
        x=-target.rect.x + SCREEN_WIDTH // 2
        y=-target.rect.y + SCREEN_HEIGHT // 2
        self.offset=(x,y)