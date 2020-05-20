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
        pygame.draw.circle(img,cor_bolinha,(20,20),20)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y

        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500


    def update(self):
        xmove=math.cos(math.radians(self.angle))*self.speed
        ymove=-math.sin(math.radians(self.angle))*self.speed
        
        self.rect.x+=xmove
        self.rect.y+=ymove
        

        '''if self.rect.left<0 or self.rect.right>WIDTH:
            self.angle=180-self.angle
            

        if self.rect.top<0 or self.rect.bottom>HEIGHT:
            self.angle=180-self.angle
            self.speed *= -1'''



    def tiro(self):
        now=pygame.time.get_ticks()
        tempo_passado=now-self.last_shot
        if tempo_passado>self.last_shot:
            self.last_shot=now
            self.speed=10
            dx = self.mousex - self.rect.centerx
            dy = self.mousey - self.rect.centery
            self.angle = math.degrees(math.atan2(dy, dx)) + 90
            self.rect+=self.speed
        

            

        