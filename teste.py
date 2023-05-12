import pygame
import sys

posx = 115
posy = 217

pygame.init()

largura = 1200
altura = 700

cor_de_fundo = pygame.Color(0, 132, 252)  # cor vai ser o azul usado na tela dos botoes inicial


class Botao(pygame.sprite.Sprite):
    def __init__(self, *groups, image, image1, image2):
        super().__init__(*groups)

        self.image = pygame.image.load(image).convert_alpha()

        self.rect = pygame.Rect(posx, posy, 93, 93)

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


# ButtonGrups é uma variável que contém um objeto do tipo Group.
ButtonGrups = pygame.sprite.Group()

# cria o botão
Botao1 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png")
Botao1.rect.center = (posx, posy)

# dá load da imagem
imagem1_fundo = pygame.image.load("imagens_jogo/1_verde_trevo.png").convert_alpha()

imagem1_verde_exibida = False

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        ButtonGrups.update()

    # verifica se o botão foi pressionado
    if Botao1.touche == True:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (80, 80))
        screen.blit(imagem1_fundo, (posx, posy))
        imagem1_verde_exibida = True

    ButtonGrups.draw(screen)
    ButtonGrups.update()
    screen.fill(cor_de_fundo)

    pygame.display.flip()
    pygame.display.update()