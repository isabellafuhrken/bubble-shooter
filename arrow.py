from Settings import *
import math
#Classe da seta de lançamento 
class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.angle=90
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


    def update(self):
        dx = self.mousex - self.rect.centerx
        dy = self.mousey - self.rect.centery
        self.angle = math.degrees(math.atan2(dy, dx)) + 90
        #Falta fazer o if da seta
        self.image=pygame.transform.rotate(self.orig_img, -self.angle)
        self.rect = self.image.get_rect()
        self.rect.centerx=STARTX
        self.rect.centery=STARTY


