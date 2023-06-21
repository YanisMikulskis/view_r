import pygame as pg
class EGOR(pg.sprite.Sprite):

    def __init__(self, x, y, filename, *args):
        pg.sprite.Sprite.__init__(self)
        image_base = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(image_base, [image_base.get_width()//10, image_base.get_height()//10])
        self.rect = self.image.get_rect(center= [x, y])
        self.speed_arg = 20
        self.speed_inc = 0.5
        self.jump_cof = None #коэффициент, чтобы Егор отскакивал только тогда
        #когда ПАДАЕТ ВНИЗ на платформу при пересечении с ее верхней частью,
        # а не когда он ее просто пересекает снизу
        self.scale = 0
    def update(self):
        def drive():
            self.rect.centery -= self.speed_arg
            self.speed_arg -= self.speed_inc

            if self.speed_arg > 0: self.jump_cof = True#верхняя сторона платформы игнорируется
            if self.speed_arg < 0: self.jump_cof = False#происходит отскок(подробности в главном цикле)
        drive()
        if self.rect.top <= 400:
            self.rect.top = 400
            self.scale += 1
        print(self.scale)

