from os import path
import pygame
import random
from tela_inicial import tela_inicial
from tela_jogo import tela_jogo
from Settings import *
'''from Jogo import  *'''

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bubble Shooter')

state = INIT
while state != QUIT:
    if state == INIT:
        state = tela_inicial(window)
    elif state == GAME:
        state = tela_jogo(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

