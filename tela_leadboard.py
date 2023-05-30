import pygame
import sys


def leaderboard(winner, nome_jogador1, nome_jogador2, com_nome_jogadores = 1):
    pygame.init()
    class Botao(pygame.sprite.Sprite):
        def __init__(self, *groups,image, image1, image2):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [244, 68])
            self.rect = pygame.Rect(190, 49, 190, 49)
            self.rect = self.image.get_rect()

            self.image1 = pygame.image.load(image1).convert_alpha()
            self.image2 = pygame.image.load(image2).convert_alpha()

            self.touche = False

        def update(self):
            self.mouse = pygame.mouse.get_pressed()
            self.MousePos = pygame.mouse.get_pos()

            if self.rect.collidepoint(self.MousePos):

                if self.mouse[0]:
                    self.touche = True
                    pygame.mouse.get_rel()
                    self.image = self.image2

                else:
                    self.touche = False
                    self.image = self.image1

            pass

    class Botao11(pygame.sprite.Sprite):
        def __init__(self, *groups, image, image1, image2, dim):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [dim, dim])  # dimensoes botao voltar atras
            self.rect = pygame.Rect(190, 49, 190, 49)
            self.rect = self.image.get_rect()

            self.image1 = pygame.image.load(image1).convert_alpha()
            self.image2 = pygame.image.load(image2).convert_alpha()

            self.touche = False

        def update(self):
            self.mouse = pygame.mouse.get_pressed()
            self.MousePos = pygame.mouse.get_pos()

            if self.rect.collidepoint(self.MousePos):

                if self.mouse[0]:
                    self.touche = True
                    pygame.mouse.get_rel()
                    # self.image = self.image2

                else:
                    self.touche = False
                    # self.image = self.image1

            pass


    # Configurações da tela
    largura_tela = 757
    altura_tela = 567
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Leaderboard")

    # Cores
    cor_fundo = (255, 255, 255)  # Branco
    cor_letra_branca = (255, 255, 255)  # Branco
    cor_letra_preta = (0, 0, 0)  # Preto

    # Fonte
    pygame.font.init()
    fonte_titulo = pygame.font.SysFont(None, 48)
    fonte_leaderboard = pygame.font.SysFont(None, 36)

    ButtonGrups = pygame.sprite.Group()


    Botao3 = Botao11(ButtonGrups, image="imagens_gerais/x.png", image1="imagens_gerais/x.png",
                     image2="imagens_gerais/x.png", dim=60)
    Botao3.rect.center = (680, 50)  # localizaçao botão voltar atrás


    if com_nome_jogadores == 1:
        # Leaderboard (exemplo)
        leaderboard = [
            (nome_jogador1, winner[nome_jogador1]),
            (nome_jogador2, winner[nome_jogador2]),
        ]
    else:
        leaderboard = [
            (nome_jogador1, winner["Jogador1"]),
            (nome_jogador2, winner["Jogador2"]),
        ]

    if leaderboard[0][1] < leaderboard[1][1]:
        leaderboard.append(leaderboard[0])
        leaderboard.remove(leaderboard[0])
    # Carrega a imagem do placar
    imagem_placar = pygame.image.load("imagens_jogo/leadboard.png")

    # Loop principal do jogo
    while True:
        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or Botao3.touche == True:
                pygame.quit()
                sys.exit()

        # Preenche a tela com a cor de fundo
        tela.fill(cor_fundo)

        # Renderiza a imagem do placar
        tela.blit(imagem_placar, (0, 0))

        # Renderiza os nomes e pontuações dos jogadores
        for i, jogador in enumerate(leaderboard):
            nome = jogador[0].upper()  # Converte para letras maiúsculas
            pontuacao = jogador[1]
            posicao_texto = (278, 210 + i * 80)  # Posição do texto ajustada

            # Define a cor do texto com base no índice
            cor_texto = cor_letra_branca if i == 0 else cor_letra_preta

            texto_jogador = fonte_leaderboard.render(nome + "         " + str(pontuacao), True, cor_texto)
            tela.blit(texto_jogador, posicao_texto)

        # Atualiza a tela
        ButtonGrups.update()
        ButtonGrups.draw(tela)
        pygame.display.flip()

pygame.quit()



