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

    def update(self, teclas, dt):
        dx, dy = 0, 0
        if teclas[pygame.K_LEFT]:
            dx -= 1

        if teclas[pygame.K_RIGHT]:
            dx += 1
        self.pos_x += dx * self.velocidade * dt
        self.pos_y += dy * self.velocidade * dt

        self.rect.centerx = round(self.pos_x)
        self.rect.centery = round(self.pos_y)
        pass

    def draw(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)
        pass