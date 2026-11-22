import pygame
from constants import (LARGURA, ALTURA, BRANCO)


class Player:
    def __init__(self, x, y):
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)
        self.velocidade = 300
        self.vida = 100
        self.vel_y = 0.0
        self.gravidade = 1200
        self.chao = False

## isso daqui atualiza a posição do personagem e capta o movimentos das teclas sem falar que aqui ele define o limie da tela e outros sistemas como gravidade
    def update(self, teclas, dt):
        dx = 0
        if teclas[pygame.K_a]:
            dx -= 1

        if teclas[pygame.K_d]:
            dx += 1

        if teclas[pygame.K_w] and self.chao:
            self.vel_y = -550
            self.chao = False
## aqui o eixo dy permanece em 0, pois usamos um sistema de gravidade pro pulo e o dy movia o personagem pelo plano usando o eixo y diretamente o que fazia a boneca "voar" 
        self.pos_x += dx * self.velocidade * dt
        self.vel_y += self.gravidade * dt
        self.pos_y += self.vel_y * dt
        self.rect.centerx = round(self.pos_x)
        self.rect.centery = round(self.pos_y)

        if self.rect.left < 0:
            self.rect.left = 0
            self.pos_x = float(self.rect.centerx)

        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
            self.pos_x = float(self.rect.centerx)

        if self.rect.bottom >= ALTURA:
            self.rect.bottom = ALTURA
            self.pos_y = float(self.rect.centery)
            self.vel_y = 0
            self.chao = True
            
        pass

    def draw(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)
        pass