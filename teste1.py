import pygame
import sys

posx = 100
posy = 100

pygame.init()

largura = 800
altura = 800

cor_de_fundo = pygame.Color(0, 132, 252)  # cor vai ser o azul usado na tela dos botoes inicial


class Botao(pygame.sprite.Sprite):
    def __init__(self, *groups, image, image1, image2):
        super().__init__(*groups)

        self.image = pygame.image.load(image).convert_alpha()

        self.rect = pygame.Rect(posx, posy, 144, 158)

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

            else:
                self.touche = False


# janela
screen = pygame.display.set_mode((largura, altura))

# dá load da imagem
imagem_fundo = pygame.image.load("imagens_jogo/background_edit.jpg").convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (500, 500))

# faz o blit + posicao da imagem
screen.blit(imagem_fundo, (10, 10))

# é uma função do Pygame que atualiza a tela.
pygame.display.flip()

# ButtonGrups é uma variável que contém um objeto do tipo Group.
ButtonGrups = pygame.sprite.Group()

# cria o botão
Botao1 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",image2="imagens_gerais/red_button02.png")
Botao1.rect.center = (100, 100)
Botao2 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",image2="imagens_gerais/red_button02.png")
Botao2.rect.center = (237, 100)
Botao3 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",image2="imagens_gerais/red_button02.png")
Botao3.rect.center = (379, 100)
Botao4 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",image2="imagens_gerais/red_button02.png")
Botao4.rect.center = (516, 100)

# dá load da imagem
imagem1_fundo = pygame.image.load("imagens_jogo/1_de_verde.png").convert()
imagem2_fundo = pygame.image.load("imagens_jogo/2_de_verde.png").convert()
imagem3_fundo = pygame.image.load("imagens_jogo/3_de_verde.png").convert()
imagem4_fundo = pygame.image.load("imagens_jogo/4_de_verde.png").convert()

imagem1_verde_exibida = False
imagem2_verde_exibida = False
imagem3_verde_exibida = False
imagem4_verde_exibida = False

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        ButtonGrups.update()

        # verifica se o botão foi pressionado
        if Botao1.touche == True and not imagem1_verde_exibida:
            print("IMAGEM1")

            # exibe a imagem 1 verde
            imagem1_fundo = pygame.transform.scale(imagem1_fundo, (50, 50))
            screen.blit(imagem1_fundo, (10, 10))
            imagem1_verde_exibida = True

        if Botao2.touche == True and not imagem2_verde_exibida:
            print("IMAGEM2")

            # exibe a imagem 1 verde
            imagem2_fundo = pygame.transform.scale(imagem2_fundo, (50, 50))
            screen.blit(imagem2_fundo, (10, 10))
            imagem2_verde_exibida = True

        if Botao3.touche == True and not imagem3_verde_exibida:
            print("IMAGEM3")

            # exibe a imagem 1 verde
            imagem3_fundo = pygame.transform.scale(imagem3_fundo, (50, 50))
            screen.blit(imagem3_fundo, (10, 10))
            imagem3_verde_exibida = True

        if Botao4.touche == True and not imagem4_verde_exibida:
            print("IMAGEM4")

            # exibe a imagem 1 verde
            imagem4_fundo = pygame.transform.scale(imagem4_fundo, (50, 50))
            screen.blit(imagem4_fundo, (10, 10))
            imagem4_verde_exibida = True

        ButtonGrups.draw(screen)

    screen.fill(cor_de_fundo)
    screen.blit(imagem_fundo, (10, 10))

    if imagem1_verde_exibida: #evitar que seja possivel clicar varias vezes
        screen.blit(imagem1_fundo, (70, 70))
        screen.blit(imagem1_fundo, (70, 180))
        screen.blit(imagem1_fundo, (70, 290))
        screen.blit(imagem1_fundo, (70, 400))
    if imagem2_verde_exibida: #evitar que seja possivel clicar varias vezes
        screen.blit(imagem2_fundo, (180, 70))
        screen.blit(imagem2_fundo, (180, 180))
        screen.blit(imagem2_fundo, (180, 290))
        screen.blit(imagem2_fundo, (180, 400))
    if imagem3_verde_exibida: #evitar que seja possivel clicar varias vezes
        screen.blit(imagem3_fundo, (290, 70))
        screen.blit(imagem3_fundo, (290, 180))
        screen.blit(imagem3_fundo, (290, 290))
        screen.blit(imagem3_fundo, (290, 400))
    if imagem4_verde_exibida: #evitar que seja possivel clicar varias vezes
        screen.blit(imagem4_fundo, (400, 70))
        screen.blit(imagem4_fundo, (400, 180))
        screen.blit(imagem4_fundo, (400, 290))
        screen.blit(imagem4_fundo, (400, 400))

    pygame.display.flip()
    pygame.display.update()