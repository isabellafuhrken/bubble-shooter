from Settings import *


class Bubble(pygame.sprite.Sprite):
    def __init__(self,x,y,linha,coluna):
        pygame.sprite.Sprite.__init__(self)
        self.radius=BUBBLERADIUS
        self.speed=0
        self.mousex=0
        self.mousey=0
        self.angle=0
        self.linha = linha
        self.coluna = coluna
        img=pygame.Surface((40,40))
        img.set_colorkey((0,0,0))
        cor_bolinha = random.choice(COLORS)
        self.cor = cor_bolinha
        pygame.draw.circle(img,cor_bolinha,(20,20),20)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.dx=0
        self.dy=0

    def update(self):
        self.angle = math.degrees(math.atan2(self.dy, self.dx))
        xmove=math.cos(math.radians(self.angle))*self.speed
        ymove=math.sin(math.radians(self.angle))*self.speed

        self.rect.x+=xmove
        self.rect.y+=ymove

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0

        if self.rect.left<0 or self.rect.right>WIDTH:
            self.dx = -self.dx
            if self.rect.left<0:
                self.rect.left = 0
            else:
                self.rect.right = WIDTH

    def tiro(self):
        self.speed=10
        
    
    

      
        
    


      
        

