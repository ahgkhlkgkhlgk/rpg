from  setting import*

class Camera:
    # класс камеры (и так понятно)
    def __init__(self,map_width,map_height):
        self.offset=(0,0)
        self.m_width=map_width
        self.m_height=map_height
    def apply(self,entity):
        # возвращает позицию игрока
        return entity.rect.move(self.offset)
    def update(self,target):
        # обновляет позицию карты(передвижение камеры)
        # target = спрайт за которой следит камера
        x=-target.rect.x + SCREEN_WIDTH // 2
        y=-target.rect.y + SCREEN_HEIGHT // 2
        x=min(x,0)
        y=min(y,0)
        x=max(x,SCREEN_WIDTH - self.m_width)
        y=max(y,SCREEN_HEIGHT - self.m_height)
        self.offset=(x,y)