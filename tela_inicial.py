
import pygame
import random
from os import path

from Settings import IMG_DIR, BLACK, FPS, GAME, QUIT

def tela_inicial(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 370 and pygame.mouse.get_pos()[0] <= 470 and pygame.mouse.get_pos()[1] >= 328 and pygame.mouse.get_pos()[1] <= 480:
                    state = GAME
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        window.fill(BLACK)
        window.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
