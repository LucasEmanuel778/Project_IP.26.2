import pygame
from constants import (LARGURA, ALTURA, BRANCO)


class Player:
    def __init__(self, x, y):
        ## status de posição, vida e tamanho do player
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)
        self.velocidade = 300
        self.vida = 100
        self.vel_y = 0.0
        self.gravidade = 1200
        self.chao = False

        ## status de ataque do personagem pq quero fazer q nem o castlevania de 1986, essas floats são a duração de cada ação
        self.olhando_direita = True
        self.atacando = False
        self.duracao = 0.25
        self.tempo_atq = 0.0
        self.cooldown = 0.15
        self.cooldown_atual = 0.0
        self.alcance_chicote = 40 ## esse 40 é a distancia de 1 player (40 pixel ja que o jogador é um quadrado de 40x40)
        self.altura_chicote = 16
        self.hitbox_atq = None
        self.alvos_atingidos = set()

## isso daqui atualiza a posição do personagem e capta o movimentos das teclas sem falar que aqui ele define o limie da tela e outros sistemas como gravidade
    def update(self, teclas, dt, plataformas =()):
        self._atualizar_timers_ataque(dt)
        dx = 0
        if teclas[pygame.K_a]:
            dx -= 1
        
        if teclas[pygame.K_d]:
            dx += 1

        if teclas[pygame.K_w] and self.chao:
            self.vel_y = -550
            self.chao = False
        ## vou colocar um easter egg de dobrar a velocidade enquando o player segura a setinha direita e se move 
        self.velocidade_atual = self.velocidade * 2 if teclas[pygame.K_RIGHT] else self.velocidade
    
        ##  isso daqui evita que o player ataque em várias direções enquanto ataca
        if not self.atacando:
            if dx > 0:
                self.olhando_direita = True
            elif dx < 0:
                self.olhando_direita = False
        if (teclas[pygame.K_k] or teclas[pygame.K_SPACE]) and not self.atacando and self.cooldown_atual <= 0:
            self.iniciar_ataque()

        ## vou colocar um sistema que o personagem pare quando for atacar que nem no castlevania de 1986, mas isso se limita para os movimentos na horizontal
        if self.atacando and self.chao:
            dx = 0

## aqui o eixo dy permanece em 0, pois usamos um sistema de gravidade pro pulo e o dy movia o personagem pelo plano usando o eixo y diretamente o que fazia a boneca "voar" 
        ## sistema de colisao horizontal
        self.pos_x += dx * self.velocidade_atual * dt
        self.rect.centerx = round(self.pos_x)
        self.colisao_horizontal(dx, plataformas)

        ## sistema de colisão vertical
        self.chao = False
        self.vel_y += self.gravidade * dt
        self.pos_y += self.vel_y * dt
        self.rect.centery = round(self.pos_y)
        self.colisao_vertical(plataformas)

        self._atualizar_hitbox_ataque()

        pass

    def colisao_horizontal(self, dx, plataformas):
        for plat in plataformas:
            if self.rect.colliderect(plat):
                if dx > 0:
                    self.rect.right = plat.left
                elif dx < 0:
                    self.rect.left = plat.right
                self.pos_x = float(self.rect.centerx)
        if self.rect.left < 0:
                    self.rect.left = 0
                    self.pos_x = float(self.rect.centerx)
        
        elif self.rect.right > LARGURA:
            self.rect.right = LARGURA
            self.pos_x = float(self.rect.centerx)

    def colisao_vertical(self, plataformas):
        for plat in plataformas:
            if self.rect.colliderect(plat):
                if self.vel_y > 0:
                    self.rect.bottom = plat.top
                    self.vel_y = 0
                    self.chao = True
                elif self.vel_y < 0:
                    self.rect.top = plat.bottom
                    self.vel_y = 0
                self.pos_y = float(self.rect.centery)

        if self.rect.bottom >= ALTURA:
            self.rect.bottom = ALTURA
            self.pos_y = float(self.rect.centery)
            self.vel_y = 0
            self.chao = True
    def iniciar_ataque(self):
        self.atacando = True
        self.tempo_atq = self.duracao
        self.alvos_atingidos.clear()

    def _atualizar_timers_ataque(self, dt):
        if self.cooldown_atual > 0:
            self.cooldown_atual -= dt
        if self.atacando:
            self.tempo_atq -= dt
            if self.tempo_atq <= 0:
                self.atacando = False
                self.hitbox_atq = None
                self.cooldown_atual = self.cooldown

    def _atualizar_hitbox_ataque(self):
        if not self.atacando:
            self.hitbox_atq = None
            return
        y_chicote = self.rect.centery - (self.altura_chicote // 2)
        if self.olhando_direita:
            x_chicote = self.rect.right

        else:
            x_chicote = self.rect.left - self.alcance_chicote
        self.hitbox_atq = pygame.Rect(x_chicote, y_chicote, self.alcance_chicote, self.altura_chicote)

    def draw(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)
        if self.hitbox_atq is not None:
            pygame.draw.rect(tela, (255, 0, 0), self.hitbox_atq)
        