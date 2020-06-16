'''Importa a biblioteca math e o arquivo Settings'''
from Settings import *
import math
'''Classe da seta de lançamento '''
class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.angle=90
        '''Carrega foto da seta'''
        arrowImage = pygame.image.load('assets/arrow.png')
        arrowImage.convert_alpha()
        arrowRect= arrowImage.get_rect()
        self.orig_img = arrowImage
        self.image=arrowImage
        self.rect=arrowRect
        self.rect.centerx=STARTX
        self.rect.centery=STARTY
        self.mousex = 0
        self.mousey = 0

    '''Atualização da seta'''
    def update(self):
        dx = self.mousex - self.rect.centerx
        dy = self.mousey - self.rect.centery
        self.angle = math.degrees(math.atan2(dy, dx)) + 90
        self.image=pygame.transform.rotate(self.orig_img, -self.angle)
        self.rect = self.image.get_rect()
        self.rect.centerx=STARTX
        self.rect.centery=STARTY


