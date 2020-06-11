import pygame , random , math , time 
import pygame.gfxdraw
import sys
from os import path


INIT = 0
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
GAME = 1
QUIT = 2

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
BGCOLOR = BEIGE

def load_assets():
    assets={}
    
    pygame.mixer.music.load('assets/StartSong.wav')
    pygame.mixer.music.set_volume(0.4)
    #Colocar uma segunda musica na hora que clica no start

    
    return assets
    