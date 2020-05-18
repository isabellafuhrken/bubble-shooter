from Settings import *

class Bubble(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.radius=BUBBLERADIUS
        self.speed=0
        self.angle=0
        img=pygame.Surface((40,40))
        img.set_colorkey((0,0,0))
        cor_bolinha = random.choice(COLORS)
        pygame.draw.circle(img,cor_bolinha,(20,20),20)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y

    def update(self):
        xmove=math.cos(math.radians(self.angle))*self.speed
        ymove=-math.sin(math.radians(self.angle))*self.speed
        self.rect.centerx+=xmove
        self.rect.centery+=ymove   

        if self.rect.left<0 or self.rect.right>WIDTH:
            self.angle=180-self.angle
            self.speed*= -1

        if self.rect.top<0 or self.rect.bottom>HEIGHT:
            self.angle=180-self.angle
            self.speed *= -1

    def desenho(self):
        pygame.gfxdraw.filled_circle(window, self.rect.centerx,self.rect.centery,self.radius,BLACK)
        pygame.gfxdraw.aacircle(window,self.rect.centerx,self.rect.centery,self.radius,BLACK)

    def tiro(self,algle):
        self.angle=angle
        self.speed=10