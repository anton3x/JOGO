import pygame
import sys

def main():
    fps = pygame.time.Clock()
    largura = 1024
    altura = 600

    JogoLoop = True

    tela = pygame.display.set_mode([largura, altura])
    pygame.display.set_caption("Lucky Numbers")

    ColorBack = {"azul": [0, 132, 252], "vermelho": [137, 28, 36]}

    class Botao(pygame.sprite.Sprite):
        def __init__(self, *groups, image, image1, image2):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [190, 49])
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

    ButtonGrups = pygame.sprite.Group()

    Botao1 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png")
    Botao1.rect.center = (250, 300)

    Botao2 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png")
    Botao2.rect.center = (512, 300)

    Botao4 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png")
    Botao4.rect.center = (512, 400)

    Botao3 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png")
    Botao3.rect.center = (250, 400)

    while JogoLoop:
        fps.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JogoLoop = False

            if Botao1.touche == True:
                tela.fill(ColorBack["vermelho"])
                tela5()

            if Botao2.touche == True:
                tela.fill(ColorBack["azul"])

            if Botao3.touche == True:
                tela.fill(ColorBack["azul"])

            if Botao4.touche == True:
                tela.fill(ColorBack["azul"])

            else:
                tela.fill(ColorBack["azul"])

            ButtonGrups.update()
            ButtonGrups.draw(tela)

            pygame.display.update()
    pygame.quit()
def tela5():
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
    posy5 = 344
    posx6 = posx2
    posy6 = posy5
    posx7 = posx3
    posy7 = posy5
    posx8 = posx4
    posy8 = posy5

    posx9 = posx1
    posy9 = 429
    posx10 = posx2
    posy10 = posy9
    posx11 = posx3
    posy11 = posy9
    posx12 = posx4
    posy12 = posy9

    posx13 = posx1
    posy13 = 514
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
    Botao1 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx1, posy=posy1)
    Botao1.rect.center = (posx1, posy1)
    Botao2 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx2, posy=posy2)
    Botao2.rect.center = (posx2, posy2)
    Botao3 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx3, posy=posy3)
    Botao3.rect.center = (posx3, posy3)
    Botao4 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx4, posy=posy4)
    Botao4.rect.center = (posx4, posy4)
    Botao5 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx5, posy=posy5)
    Botao5.rect.center = (posx5, posy5)
    Botao6 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx6, posy=posy6)
    Botao6.rect.center = (posx6, posy6)
    Botao7 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx7, posy=posy7)
    Botao7.rect.center = (posx7, posy7)
    Botao8 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx8, posy=posy8)
    Botao8.rect.center = (posx8, posy8)
    Botao9 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx9, posy=posy9)
    Botao9.rect.center = (posx9, posy9)
    Botao10 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx10, posy=posy1)
    Botao10.rect.center = (posx10, posy10)
    Botao11 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx11, posy=posy11)
    Botao11.rect.center = (posx11, posy11)
    Botao12 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx12, posy=posy12)
    Botao12.rect.center = (posx12, posy12)
    Botao13 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx13, posy=posy13)
    Botao13.rect.center = (posx13, posy13)
    Botao14 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx14, posy=posy14)
    Botao14.rect.center = (posx14, posy14)
    Botao15 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx15, posy=posy15)
    Botao15.rect.center = (posx15, posy15)
    Botao16 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx16, posy=posy16)
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
            screen.blit(imagem1_fundo, (posx1 - 36, posy1 - 36))
            imagem1_verde_exibida = True
        if Botao2.touche == True and not imagem2_verde_exibida:
            print("IMAGEM2")

            # exibe a imagem 1 verde
            imagem2_fundo = pygame.transform.scale(imagem2_fundo, (73, 73))
            screen.blit(imagem2_fundo, (posx2 - 36, posy2 - 36))
            imagem2_verde_exibida = True
        if Botao3.touche == True and not imagem3_verde_exibida:
            print("IMAGEM3")

            # exibe a imagem 1 verde
            imagem3_fundo = pygame.transform.scale(imagem3_fundo, (73, 73))
            screen.blit(imagem3_fundo, (posx3 - 36, posy3 - 36))
            imagem3_verde_exibida = True
        if Botao4.touche == True and not imagem4_verde_exibida:
            print("IMAGEM4")

            # exibe a imagem 1 verde
            imagem4_fundo = pygame.transform.scale(imagem4_fundo, (73, 73))
            screen.blit(imagem4_fundo, (posx4 - 36, posy4 - 36))
            imagem4_verde_exibida = True
        if Botao5.touche == True and not imagem5_verde_exibida:
            print("IMAGEM5")

            # exibe a imagem 1 verde
            imagem5_fundo = pygame.transform.scale(imagem5_fundo, (73, 73))
            screen.blit(imagem5_fundo, (posx5 - 36, posy5 - 36))
            imagem5_verde_exibida = True
        if Botao6.touche == True and not imagem6_verde_exibida:
            print("IMAGEM6")

            # exibe a imagem 1 verde
            imagem6_fundo = pygame.transform.scale(imagem6_fundo, (73, 73))
            screen.blit(imagem6_fundo, (posx6 - 36, posy6 - 36))
            imagem6_verde_exibida = True
        if Botao7.touche == True and not imagem7_verde_exibida:
            print("IMAGEM7")

            # exibe a imagem 1 verde
            imagem7_fundo = pygame.transform.scale(imagem7_fundo, (73, 73))
            screen.blit(imagem7_fundo, (153 - 36, 259 - 36))
            imagem7_verde_exibida = True
        if Botao8.touche == True and not imagem8_verde_exibida:
            print("IMAGEM8")

            # exibe a imagem 1 verde
            imagem8_fundo = pygame.transform.scale(imagem8_fundo, (73, 73))
            screen.blit(imagem8_fundo, (posx8 - 36, posy8 - 36))
            imagem8_verde_exibida = True
        if Botao9.touche == True and not imagem9_verde_exibida:
            print("IMAGEM9")

            # exibe a imagem 1 verde
            imagem9_fundo = pygame.transform.scale(imagem9_fundo, (73, 73))
            screen.blit(imagem9_fundo, (posx9 - 36, posy9 - 36))
            imagem9_verde_exibida = True
        if Botao10.touche == True and not imagem10_verde_exibida:
            print("IMAGEM10")

            # exibe a imagem 1 verde
            imagem10_fundo = pygame.transform.scale(imagem10_fundo, (73, 73))
            screen.blit(imagem10_fundo, (posx10 - 36, posy10 - 36))
            imagem10_verde_exibida = True
        if Botao11.touche == True and not imagem11_verde_exibida:
            print("IMAGEM11")

            # exibe a imagem 1 verde
            imagem11_fundo = pygame.transform.scale(imagem11_fundo, (73, 73))
            screen.blit(imagem11_fundo, (posx11 - 36, posy11 - 36))
            imagem11_verde_exibida = True
        if Botao12.touche == True and not imagem12_verde_exibida:
            print("IMAGEM12")

            # exibe a imagem 1 verde
            imagem12_fundo = pygame.transform.scale(imagem12_fundo, (73, 73))
            screen.blit(imagem12_fundo, (posx12 - 36, posy12 - 36))
            imagem12_verde_exibida = True
        if Botao13.touche == True and not imagem13_verde_exibida:
            print("IMAGEM13")

            # exibe a imagem 1 verde
            imagem13_fundo = pygame.transform.scale(imagem13_fundo, (73, 73))
            screen.blit(imagem13_fundo, (posx13 - 36, posy13 - 36))
            imagem13_verde_exibida = True
        if Botao14.touche == True and not imagem14_verde_exibida:
            print("IMAGEM14")

            # exibe a imagem 1 verde
            imagem14_fundo = pygame.transform.scale(imagem14_fundo, (73, 73))
            screen.blit(imagem14_fundo, (posx14 - 36, posy14 - 36))
            imagem14_verde_exibida = True
        if Botao15.touche == True and not imagem15_verde_exibida:
            print("IMAGEM15")

            # exibe a imagem 1 verde
            imagem15_fundo = pygame.transform.scale(imagem15_fundo, (73, 73))
            screen.blit(imagem15_fundo, (posx15 - 36, posy15 - 36))
            imagem15_verde_exibida = True
        if Botao16.touche == True and not imagem16_verde_exibida:
            print("IMAGEM16")

            # exibe a imagem 1 verde
            imagem16_fundo = pygame.transform.scale(imagem16_fundo, (73, 73))
            screen.blit(imagem16_fundo, (posx16 - 36, posy16 - 36))
            imagem16_verde_exibida = True

        ButtonGrups.draw(screen)
        ButtonGrups.update()
        screen.fill(cor_de_fundo)
        screen.blit(imagem_fundo, (0, 0))

        if imagem1_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem1_fundo, (posx1 - 36, posy1 - 36))
        if imagem2_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem2_fundo, (posx2 - 36, posy2 - 36))
        if imagem3_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem3_fundo, (posx3 - 36, posy3 - 36))
        if imagem4_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem4_fundo, (posx4 - 36, posy4 - 36))
        if imagem5_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem5_fundo, (posx5 - 36, posy5 - 36))
        if imagem6_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem6_fundo, (posx6 - 36, posy6 - 36))
        if imagem7_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem7_fundo, (posx7 - 36, posy7 - 36))
        if imagem8_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem8_fundo, (posx8 - 36, posy8 - 36))
        if imagem9_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem9_fundo, (posx9 - 36, posy9 - 36))
        if imagem10_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem10_fundo, (posx10 - 36, posy10 - 36))
        if imagem11_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem11_fundo, (posx11 - 36, posy11 - 36))
        if imagem12_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem12_fundo, (posx12 - 36, posy12 - 36))
        if imagem13_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem13_fundo, (posx13 - 36, posy13 - 36))
        if imagem14_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem14_fundo, (posx14 - 36, posy14 - 36))
        if imagem15_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem15_fundo, (posx15 - 36, posy15 - 36))
        if imagem16_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem16_fundo, (posx16 - 36, posy16 - 36))

        pygame.display.flip()
        pygame.display.update()
main()





