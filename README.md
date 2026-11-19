
# Sabrina Doesn't Know How To Integrate

## Descrição do Projeto:
A 2D game inspired by Sabrina Carpenter, featuring character movement and 3 unique collectibles. Developed as a college project. This project will be based on "classicvania"-style games—for instance, the original 1986 *Castlevania*. The game will feature a combat system centered on defeating iconic enemies, such as integrals, limits, and derivatives. Standing against these fearsome creatures, which seek to invade the earthly realm, will be our heroine: Sabrina Carpenter.

## Participantes do Projeto:
- Lucas Emanuel Araújo Arruda <leaa2>
- Brian Miguel da Silva Santos <bmss>
- Mateus Soares Mendes <msm4>
- Lucas Kauã Gomes <lkgs>
- Vitor Gabriel Jose de Oliveira Belo <vgjob>
- João Pedro Cabral Bezerra Cavalcanti <jpcbc>

## Organização e Desenvolvimento de Jogo:


## Capturas de tela:
### Tela inicial do jogo
    print
### Jogabilidade
    print
### Tela final do jogo
    print

## Estrutura do Projeto:
- main.py: 

## Ferramentas utilizadas:
### Bibliotecas


### Ferramentas


## Controles:
Pressione a tecla <- para que o goleiro se desloque para esquerda
Pressione a tecla -> para que o goleiro se desloque para direita

## Regras do Jogo:
- O jogador inicia a partida com uma quantidade definida de vidas;
- A partida se estende até que todas as vidas sejam esgotadas;


## Divisão de tarefas:
A definição dos principais elementos do jogo, como tema, lógica, regras, personagens e visual da interface, foi feita de maneira colaborativa. Todos os integrantes apresentaram sugestões durante as reuniões do grupo, e as decisões foram tomadas em consenso ao longo do desenvolvimento.

Detalhes técnicos:

- Lucas Emanuel Araújo Arruda:
    Classe Player (movimentação 2D, limites da tela, animações de direção/estado);
    Sistema de colisão (pygame.Rect ou máscaras) e controle de inputs (teclado/mouse).

- Brian Miguel da Silva Santos:
    Telas de Menu Inicial, Instruções, Pausa e Fim de Jogo (botões interativos);
    Renderização do mapa/cenário 2D, plano de fundo e eventuais obstáculos do ambiente.

- Mateus Soares Mendes:
    Estrutura inicial do repositório GitHub (main, branches e .gitignore);
    Loop principal do jogo (Game), máquina de estados (Menu, Jogando, Game Over) e controle de FPS;
    Revisão de Pull Requests (PRs) e integração das classes;
    Gestão do GitHub e organização das pastas;
    Construção do ReadMe.

- Lucas Kauã Gomes:
    Classe ScoreManager / Inventario para registrar a quantidade coletada de cada um dos 3+ tipos de objetos;
    Exibição em tempo real na tela (HUD com contadores individuais e ícones);
    Salvamento de recordes (High Score em arquivo .txt ou .json).

- Vitor Gabriel Jose de Oliveira Belo:
    Classe AudioManager (música de fundo e efeitos sonoros ao coletar cada tipo de item);
    Feedback visual de coleta (partículas, textos flutuantes de +1, transições);
    Testes de bugs (colisões falhando, travamentos, edge cases).

- João Pedro Cabral Bezerra Cavalcanti:
    Classe base abstrata/pai Coletavel (herança e polimorfismo);
    Implementação de pelo menos 3 subclasses distintas de objetos coletáveis (com comportamentos, pontuações ou efeitos diferentes);
        Lógica de spawn (geração aleatória ou programada na tela).


## Conceitos aprendidos durante a disciplina utilizados no jogo:


## Desafios e erros enfrentados:


## Lições aprendidas: