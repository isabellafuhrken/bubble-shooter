#Importa bibliotecas
import pygame , random , math , time 
import pygame.gfxdraw
import sys
from os import path

#Define os parâmetros e variáveis
INIT = 0
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'sound')
GAME = 1
QUIT = 2
OVER = 3

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


#Define as cores que serão utilizadas no jogo
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
LIGHT_RED = (255, 222, 222)
LIGHT_GREEN = (209, 255, 205)
LIGHT_PINK = (255, 205, 247)
LIGHT = [LIGHT_PINK, LIGHT_GREEN,LIGHT_BLUE]

COLORS = [RED, GREEN, BLUE, ORANGE, YELLOW, PURPLE, NAVY]
BGCOLOR = BEIGE

BOLHA_SND = 'bolha_snd'

#Função que carrega a música utilizada na tela de início
def load_assets():
    assets={}
    pygame.mixer.music.load(path.join(SND_DIR, 'StartSong.wav'))
    pygame.mixer.music.set_volume(0.7)

    return assets

