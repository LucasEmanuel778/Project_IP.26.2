import sys
import pygame
from constants import (
    LARGURA, ALTURA, FPS, TITULO,
    PRETO, BRANCO,
    ESTADO_MENU, ESTADO_JOGANDO, ESTADO_PAUSADO, ESTADO_GAME_OVER
)
from src.entities.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO)
        self.clock = pygame.time.Clock()
        self.fonte_debug = pygame.font.SysFont("arial", 20)

        self.rodando = True
        self.estado = ESTADO_JOGANDO  # Trocar para ESTADO_MENU quando a tela inicial existir

        self.inicializar_objetos()

    def inicializar_objetos(self):
        """Instancia ou reseta os objetos da partida."""
        self.player = Player(LARGURA // 2, ALTURA // 2)
         # self.score_manager = ScoreManager()
         # self.coletaveis = []
        pass

    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False

            if event.type == pygame.KEYDOWN:
                # Alterna Pausa
                if event.key in (pygame.K_p, pygame.K_ESCAPE):
                    if self.estado == ESTADO_JOGANDO:
                        self.estado = ESTADO_PAUSADO
                    elif self.estado == ESTADO_PAUSADO:
                        self.estado = ESTADO_JOGANDO

                # Reinicia no Game Over
                elif event.key == pygame.K_r and self.estado == ESTADO_GAME_OVER:
                    self.inicializar_objetos()
                    self.estado = ESTADO_JOGANDO

    def atualizar(self, dt):
        if self.estado == ESTADO_JOGANDO:
            teclas = pygame.key.get_pressed()
            self.player.update(teclas, dt)
            pass

    def desenhar(self):
        self.tela.fill(PRETO)

        if self.estado == ESTADO_JOGANDO:
            self.player.draw(self.tela)
            # self.score_manager.draw(self.tela)
            pass
        elif self.estado == ESTADO_PAUSADO:
            texto = self.fonte_debug.render("JOGO PAUSADO (Pressione P para voltar)", True, BRANCO)
            self.tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2))

        pygame.display.flip()

    def run(self):
        while self.rodando:
            dt = self.clock.tick(FPS) / 1000.0
            self.processar_eventos()
            self.atualizar(dt)
            self.desenhar()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    jogo = Game()
    jogo.run()