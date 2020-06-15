import pygame
from Settings import *
from os import path
import random
from Bubble import Bubble
from arrow import Arrow
from time import sleep,time

pygame.mixer.init()

#Tela principal 

def tela_jogo(screen):
    objetos=pygame.sprite.Group()
    grid = pygame.sprite.Group()
    player=Bubble(STARTX,STARTY,-1,-1)
    flecha=Arrow()
    objetos.add(flecha)
    objetos.add(player)
    score=0
    fonte_score=pygame.font.Font('assets/font/PressStart2P.ttf', 20)
    bolha_b = pygame.mixer.Sound(path.join(SND_DIR, 'bolha.ogg'))
    fontev =pygame.font.Font('assets/font/FonteV.ttf',28)

    bolinhas = []
    #Cria grid das bolinhas
    for i in range(LINHAS):
        linha = []
        for j in range(COL):
            bolha=Bubble(BUBBLEHEIGHT*j+BUBBLEHEIGHT//2,BUBBLEWIDTH*i+BUBBLEWIDTH//2, i, j)
            objetos.add(bolha)
            grid.add(bolha)
            linha.append(bolha)
        bolinhas.append(linha)


    game = True
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
                
        #Contato entre as bolinhas e a bolinha lançada  
        hits = pygame.sprite.spritecollide(player, grid, False,pygame.sprite.collide_circle)
        if len(hits) > 0:

            player.speed = 0
            for bolha1 in hits:
                if player.cor == bolha1.cor:
                    bolha_b.play()
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
                            bolinhas[l][c] = None
                            
                    #Destroi bolinha sobrando 
                    for bolinha in grid:
                        l = bolinha.linha
                        c = bolinha.coluna
                        if l > 0:
                            cima = bolinhas[l - 1][c]
                            if l+1 < len(bolinhas):
                                baixo = bolinhas[l+1][c]
                            else:
                                baixo = None
                            if c > 0:
                                esquerda = bolinhas[l][c-1]
                            else:
                                esquerda = None
                            if c+1 < len(bolinhas[l]):
                                direita = bolinhas[l][c+1]
                            else:
                                direita = None
                            if cima is None and baixo is None and esquerda is None and direita is None:
                                bolinha.kill()
                                grid.remove(bolinha)
                                bolinhas[l][c] = None

                    player.kill()
                    bolha1.kill()
                    grid.remove(bolha1)
                    score+=conta*500
                # Cria nova linha para as bolinhas lançadas  
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
            #Termina caso tenha mais de 11 na mesma coluna
            if player.rect.y > 400:
                state = OVER
                game = False
                return state
            player = Bubble(STARTX, STARTY, -1, -1)
            objetos.add(player)

        objetos.update()
        grid.update() 

        screen.fill(LIGHT_BLUE)
        #Gerando fonte 
        text_surface = fonte_score.render("{:08d}".format(score), True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (60, 600)
        screen.fill(LIGHT_BLUE)
        
        #Finalizar a tela quando a pessoa ganha
        
        ganhou = fontev.render("Você ganhou! Seu score foi {:08d} ".format(score), True, (0, 0, 0))
        ganhou_rect =ganhou.get_rect()
        ganhou_rect.midtop=(425, 300)
        
        if score>=5000:
            screen.fill(random.choice(LIGHT))
            screen.blit(ganhou, ganhou_rect)
            pygame.display.update()
            pygame.time.delay(5000)
            state=INIT
            game=False
            return state
            
          
        pygame.draw.line(screen, RED, [0, 440], [850, 440], 3)
        pygame.draw.rect(screen, LIGHT_RED, [0, 440, 850, 250])
        objetos.draw(screen)
        screen.blit(text_surface, text_rect)
        
        
        pygame.display.update()

    

