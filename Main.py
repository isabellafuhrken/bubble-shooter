from os import path
import pygame
import random
from tela_inicial import tela_inicial
from tela_jogo import tela_jogo
from game_over import game_over
from Settings import *

# Roda as tres telas 
pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bubble Shooter')

state = INIT
while state != QUIT:
    if state == INIT:
        state = tela_inicial(window)
    elif state == GAME:
        
        pygame.mixer.music.load('assets/sound/SecondSong.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=-1)
        state = tela_jogo(window)   
        
    elif state == OVER:
        state = game_over(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

