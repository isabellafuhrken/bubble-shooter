from Settings import *


class Bubble(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.radius=BUBBLERADIUS
        self.speed=0
        self.mousex=0
        self.mousey=0
        self.angle=0
        img=pygame.Surface((40,40))
        img.set_colorkey((0,0,0))
        cor_bolinha = random.choice(COLORS)
        self.cor = cor_bolinha
        pygame.draw.circle(img,cor_bolinha,(20,20),20)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y


    def tiro(self):
        self.speed=-5

    def update(self):
        dx = self.mousex - self.rect.centerx 
        dy = self.mousey - self.rect.centery
        self.angle = math.degrees(math.atan2(dy, dx))
        xmove=-math.cos(math.radians(self.angle))*self.speed
        ymove=-math.sin(math.radians(self.angle))*self.speed

        self.rect.x+=xmove
        self.rect.y+=ymove
    
    

      
        
    


      
        

