
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
player=Bubble(STARTX,STARTY,-1,-1)
flecha=Arrow()
objetos.add(flecha)
objetos.add(player)

score=0
fonte_score=pygame.font.Font('assets/font/PressStart2P.ttf', 28)

bolinhas = []

for i in range(LINHAS):
    linha = []
    for j in range(COL):
        bolha=Bubble(BUBBLEHEIGHT*j+BUBBLEHEIGHT//2,BUBBLEWIDTH*i+BUBBLEWIDTH//2, i, j)
        objetos.add(bolha)
        grid.add(bolha)
        linha.append(bolha)
    bolinhas.append(linha)



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
        for bolha1 in hits:
            if player.cor == bolha1.cor:
                vizinhos = [bolha1]
                conta=1
                while len(vizinhos) > 0:
                    vizinho = vizinhos.pop()
                    if vizinho.alive():
                        l = vizinho.linha
                        c = vizinho.coluna
                        
                        if l > 0 and bolinhas[l-1][c] is not None and bolinhas[l-1][c].cor == player.cor:
                            vizinhos.append(bolinhas[l-1][c])
                        if l < LINHAS - 1 and bolinhas[l+1][c] is not None and bolinhas[l+1][c].cor == player.cor:
                            vizinhos.append(bolinhas[l+1][c])
                        if c > 0 and bolinhas[l][c-1] is not None and bolinhas[l][c-1].cor == player.cor:
                            vizinhos.append(bolinhas[l][c-1])
                        if c < COL and bolinhas[l][c+1] is not None and bolinhas[l][c+1].cor == player.cor:
                            vizinhos.append(bolinhas[l][c+1])
                        conta+=1
                        vizinho.kill()
                    
                player.kill()
                bolha1.kill()
                grid.remove(bolha1)
                score+=conta*100
            else:
                player.linha = bolha1.linha + 1
                player.coluna = bolha1.coluna
                if player.linha >= LINHAS:
                    linha = []
                    for j in range(COL):
                        linha.append(None)
                    bolinhas.append(linha)
                bolinhas[player.linha][player.coluna] = player
                player.rect.x = player.coluna * BUBBLEWIDTH
                player.rect.y = player.linha * BUBBLEHEIGHT
                
                grid.add(player)

    
        player = Bubble(STARTX, STARTY, -1, -1)
        objetos.add(player)

    objetos.update()
    grid.update() 

    text_surface = fonte_score.render("{:08d}".format(score), True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (60, 620)
    window.blit(text_surface, text_rect)


    window.fill(LIGHT_BLUE)
    window.blit(text_surface, text_rect)
    objetos.draw(window)
    pygame.display.update()
     



pygame.quit()
