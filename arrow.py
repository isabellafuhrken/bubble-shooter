from Settings import *

class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__unit__(self)
        self.angle=90
        arrowImage = pygame.image.load('arrow.png')
        arrowImage.convert_alpha()
        arrowRect= arrowImage.get_rect()
        self.image=arrowImage
        self.transImage =self.image
        self.rect=arrowRect
        self.rect.centerx=STARTX
        self.rect.centery=STARTY

    def draw(Self):
        display.blit(Self,transImage,self.rect)

    def update(self,angle):
        self.transImage=pygame.transform.rotate(self.image,-self.angle+angle)
        self.rect.centerx=STARTX
        self.rect.centery=STARTY

