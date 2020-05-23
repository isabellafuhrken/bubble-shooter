
import pygame
import random
from Bubble import Bubble
from arrow import Arrow
'''from Jogo import  *'''

pygame.init()

FPS=120
WIDTH=850
HEIGHT=650
TEXTHEIGHT=20
BUBBLERADIUS=20
BUBBLEWIDTH=BUBBLERADIUS*2
BUBBLEHEIGHT=40
STARTX=WIDTH/2
STARTY=HEIGHT-30
LINHAS = 5
COL= 21
LINHASCOMEÇO=5



RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
ORANGE  = (255, 128, 0)
YELLOW  = (255, 255, 0)
PURPLE  = (102, 0, 101)
NAVY    = (13, 200, 255)
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
BEIGE = (229, 255, 204)
LIGHT_BLUE = (200, 220, 255)

COLORS = [RED, GREEN, BLUE, ORANGE, YELLOW, PURPLE, NAVY]

 
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bubble Shooter')

#Começo do jogo

game = True

objetos=pygame.sprite.Group()
grid = pygame.sprite.Group()
grid_del=[]
all_bolha=pygame.sprite.Group()
player=Bubble(STARTX,STARTY)
flecha=Arrow()
objetos.add(flecha)
objetos.add(player)



for i in range(LINHAS):
    for j in range(COL):
        bolha=Bubble(BUBBLEHEIGHT*j+BUBBLEHEIGHT//2,BUBBLEWIDTH*i+BUBBLEWIDTH//2)
        objetos.add(bolha)
        grid.add(bolha)
        

while game:
    for event in pygame.event.get():
        mouse=pygame.mouse.get_pos()
        flecha.mousex = mouse[0]
        flecha.mousey = mouse[1]
        if event.type == pygame.QUIT or event.type ==pygame.KEYUP:
            game = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            player.tiro()
            player.dx=mouse[0]-player.rect.centerx
            player.dy=mouse[1]-player.rect.centery
    
    

   
    hits = pygame.sprite.spritecollide(player, grid, False,pygame.sprite.collide_circle)

    if len(hits) > 0:
        player.speed = 0
        for bolha in hits:
            if player.cor == bolha.cor:
                hits = pygame.sprite.spritecollide(player, grid, True)
                player.kill()
                

                
                
                
                
                
        grid.add(player) 
        player = Bubble(STARTX, STARTY)
        objetos.add(player)
    
    objetos.update()
    grid.update() 
    

    window.fill(LIGHT_BLUE)
    objetos.draw(window)
    pygame.display.update()
     



pygame.quit()
