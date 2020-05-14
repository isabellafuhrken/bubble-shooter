from Settings import *

class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.angle=90
        arrowImage = pygame.image.load('arrow.png')
        arrowImage.convert_alpha()
        arrowRect= arrowImage.get_rect()
        self.image=arrowImage
        self.rect=arrowRect
        self.rect.centerx=STARTX
        self.rect.centery=STARTY

    def draw(Self):
        window.blit(self.Image,self.rect)

    def update(self,angle,vector):
        self.Image=pygame.transform.rotate(self.image,-self.angle+angle)
        self.rect.centerx=STARTX
        self.rect.centery=STARTY

