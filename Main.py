import pygame
import random
from Bubble import Bubble

 
pygame.init()

FPS=120
WIDTH=600
HEIGHT=480
TEXTHEIGHT=20
BUBBLERADIUS=20
BUBBLEWIDTH=BUBBLERADIUS*2
BUBBLEHEIGHT=10
STARTX=WIDTH/2
STARTY=HEIGHT-30
LINHAS=14
COL=16
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

COLORS = [RED, GREEN, BLUE, ORANGE, YELLOW, PURPLE, NAVY]
BGCOLOR = BEIGE
 
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bubble Shooter')

game = True

aa=pygame.sprite.Group()
player=Bubble(STARTX,STARTY)
aa.add(player)
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type ==pygame.KEYUP:
            game = False
    


    window.fill(BEIGE)
    aa.draw(window)
    pygame.display.update()
 
 
pygame.quit()