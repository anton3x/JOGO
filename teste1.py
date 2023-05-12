import pygame
import sys

pygame.init()

largura = 1200
altura = 700

posx1 = 153
posy1 = 259
posx2 = 239
posy2 = posy1
posx3 = 325
posy3 = posy1
posx4 = 411
posy4 = posy1

posx5 = posx1
posy5 = 345
posx6 = posx2
posy6 = posy5
posx7 = posx3
posy7 = posy5
posx8 = posx4
posy8 = posy5

posx9 = posx1
posy9 = 431
posx10 = posx2
posy10 = posy9
posx11 = posx3
posy11 = posy9
posx12 = posx4
posy12 = posy9

posx13 = posx1
posy13 = 517
posx14 = posx2
posy14 = posy13
posx15 = posx3
posy15 = posy13
posx16 = posx4
posy16 = posy13

cor_de_fundo = pygame.Color(0, 132, 252)  # cor vai ser o azul usado na tela dos botoes inicial


class Botao(pygame.sprite.Sprite):
    def __init__(self, *groups, image, image1, image2, posx, posy):
        super().__init__(*groups)

        self.image = pygame.image.load(image).convert_alpha()

        self.rect = pygame.Rect(posx, posy, 73, 73)

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
imagem_fundo = pygame.image.load("imagens_jogo/template_jogo_final.png").convert_alpha()
imagem_fundo = pygame.transform.scale(imagem_fundo, (1200, 700))

# faz o blit + posicao da imagem
screen.blit(imagem_fundo, (0, 0))

# é uma função do Pygame que atualiza a tela.
pygame.display.flip()

# ButtonGrups é uma variável que contém um objeto do tipo Group.
ButtonGrups = pygame.sprite.Group()

# cria o botão
Botao1 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx1, posy=posy1)
Botao1.rect.center = (posx1, posy1)
Botao2 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx2, posy=posy2)
Botao2.rect.center = (posx2, posy2)
Botao3 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx3, posy=posy3)
Botao3.rect.center = (posx3, posy3)
Botao4 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx4, posy=posy4)
Botao4.rect.center = (posx4, posy4)
Botao5 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx5, posy=posy5)
Botao5.rect.center = (posx5, posy5)
Botao6 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx6, posy=posy6)
Botao6.rect.center = (posx6, posy6)
Botao7 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx7, posy=posy7)
Botao7.rect.center = (posx7, posy7)
Botao8 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx8, posy=posy8)
Botao8.rect.center = (posx8, posy8)
Botao9 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx9, posy=posy9)
Botao9.rect.center = (posx9, posy9)
Botao10 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx10, posy=posy1)
Botao10.rect.center = (posx10, posy10)
Botao11 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx11, posy=posy11)
Botao11.rect.center = (posx11, posy11)
Botao12 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx12, posy=posy12)
Botao12.rect.center = (posx12, posy12)
Botao13 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx13, posy=posy13)
Botao13.rect.center = (posx13, posy13)
Botao14 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx14, posy=posy14)
Botao14.rect.center = (posx14, posy14)
Botao15 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx15, posy=posy15)
Botao15.rect.center = (posx15, posy15)
Botao16 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png", image2="imagens_gerais/red_button02.png", posx=posx16, posy=posy16)
Botao16.rect.center = (posx16, posy16)

# dá load da imagem
imagem1_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem2_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem3_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem4_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem5_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem6_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem7_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem8_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem9_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem10_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem11_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem12_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem13_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem14_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem15_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()
imagem16_fundo = pygame.image.load("imagens_jogo/num1_73.png").convert_alpha()

imagem1_verde_exibida = False
imagem2_verde_exibida = False
imagem3_verde_exibida = False
imagem4_verde_exibida = False
imagem5_verde_exibida = False
imagem6_verde_exibida = False
imagem7_verde_exibida = False
imagem8_verde_exibida = False
imagem9_verde_exibida = False
imagem10_verde_exibida = False
imagem11_verde_exibida = False
imagem12_verde_exibida = False
imagem13_verde_exibida = False
imagem14_verde_exibida = False
imagem15_verde_exibida = False
imagem16_verde_exibida = False

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
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (posx1-36, posy1-36))
        imagem1_verde_exibida = True

    if Botao2.touche == True and not imagem2_verde_exibida:
        print("IMAGEM2")

        # exibe a imagem 1 verde
        imagem2_fundo = pygame.transform.scale(imagem2_fundo, (73, 73))
        screen.blit(imagem2_fundo, (posx2-36, posy2-36))
        imagem2_verde_exibida = True


    if Botao3.touche == True and not imagem3_verde_exibida:
        print("IMAGEM3")

        # exibe a imagem 1 verde
        imagem3_fundo = pygame.transform.scale(imagem3_fundo, (73, 73))
        screen.blit(imagem3_fundo, (posx3-36, posy3-36))
        imagem3_verde_exibida = True

    if Botao4.touche == True and not imagem4_verde_exibida:
        print("IMAGEM4")

        # exibe a imagem 1 verde
        imagem4_fundo = pygame.transform.scale(imagem4_fundo, (73, 73))
        screen.blit(imagem4_fundo, (posx4-36, posy4-36))
        imagem4_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True
    if Botao1.touche == True and not imagem1_verde_exibida:
        print("IMAGEM1")

        # exibe a imagem 1 verde
        imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
        screen.blit(imagem1_fundo, (153-36, 259-36))
        imagem1_verde_exibida = True


    ButtonGrups.draw(screen)
    ButtonGrups.update()
    screen.fill(cor_de_fundo)
    screen.blit(imagem_fundo, (0, 0))

    if imagem1_verde_exibida:  # evitar que seja possivel clicar varias vezes
        screen.blit(imagem1_fundo, (posx1-36, posy1-36))
    if imagem2_verde_exibida:  # evitar que seja possivel clicar varias vezes
        screen.blit(imagem2_fundo, (posx2-36, posy2-36))
    if imagem3_verde_exibida:  # evitar que seja possivel clicar varias vezes
        screen.blit(imagem3_fundo, (posx3-36, posy3-36))
    if imagem4_verde_exibida:  # evitar que seja possivel clicar varias vezes
        screen.blit(imagem4_fundo, (posx4-36, posy4-36))

    pygame.display.flip()
    pygame.display.update()