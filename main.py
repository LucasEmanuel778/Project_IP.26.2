## aqui o código importa os recursos necessários da bliblioteca pygame, por exemplo a função exit que permite fechar a janela do jogo
import pygame
from pygame.locals import *
from sys import exit
pygame.init()

## aqui as dimensões da tela são definidas por meio dessas variáveis que são colocadas dentro de uma tupla
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

## o jogo inteiro roda em um laço de repetição
while True:
    ## esse for verifica se algum evento específico aconteceu
    for event in pygame.event.get():
        ## verifica se a janela do jogo foi fechada e chama a função exit
        if event.type == QUIT:
            pygame.quit()
            exit()
    ## atualiza a tela do jogo 
    pygame.display.update()