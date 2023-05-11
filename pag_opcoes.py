import pygame
import pygame_gui
#from Botao1 import botao1
from Tela2 import tela2
from Tela3 import tela3
from Tela4 import tela4

def main_menu():
    #pygame.init()
    fps = pygame.time.Clock()
    largura = 1024
    altura = 600

    JogoLoop = True

    tela = pygame.display.set_mode([largura, altura])
    pygame.display.set_caption("Lucky Numbers")

    ColorBack = {"azul": [0, 132, 252], "vermelho": [137, 28, 36]}

    class Botao(pygame.sprite.Sprite):
        def __init__(self, *groups,image, image1, image2):
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

    Botao1 = Botao(ButtonGrups,image="imagens_gerais/red_button01_A.png",image1="imagens_gerais/red_button01_A.png",image2="imagens_gerais/red_button02_A.png")
    Botao1.rect.center = (250, 300)

    Botao2 = Botao(ButtonGrups,image="imagens_gerais/red_button01_B.png",image1="imagens_gerais/red_button01_B.png",image2="imagens_gerais/red_button02_B.png")
    Botao2.rect.center = (512, 300)

    Botao4 = Botao(ButtonGrups,image="imagens_gerais/red_button01_D.png",image1="imagens_gerais/red_button01_D.png",image2="imagens_gerais/red_button02_D.png")
    Botao4.rect.center = (512, 400)

    Botao3 = Botao(ButtonGrups,image="imagens_gerais/red_button01_C.png",image1="imagens_gerais/red_button01_C.png",image2="imagens_gerais/red_button02_C.png")
    Botao3.rect.center = (250, 400)


    while JogoLoop:
        fps.tick(144)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JogoLoop = False

            if Botao1.touche == True:
                tela.fill(ColorBack["vermelho"])
                #tela1()
                tela5()

            if Botao2.touche == True:
                tela.fill(ColorBack["azul"])
                tela2()


            if Botao3.touche == True:
                tela.fill(ColorBack["azul"])
                tela3()


            if Botao4.touche == True:
                tela.fill(ColorBack["azul"])
                tela4()

            else:
                tela.fill(ColorBack["azul"])

            ButtonGrups.update()
            ButtonGrups.draw(tela)

            pygame.display.update()
    pygame.quit()


def tela1():
    pygame.init()
    #fps = pygame.time.Clock()
    largura = 1024
    altura = 600

    JogoLoop = True

    tela = pygame.display.set_mode([largura, altura])
    tela.fill([255, 117, 24])
   # ColorBack = {"azul": [0, 132, 252], "vermelho": [137, 28, 36], "laranja": [255, 117, 24]}
    pygame.display.set_caption("Lucky Numbers")

    class Botao11(pygame.sprite.Sprite):
        def __init__(self, *groups, image, image1, image2):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [50, 50])#dimensoes botao voltar atras
            self.rect = pygame.Rect(190, 49, 190, 49)
            self.rect = self.image.get_rect()

            #no botao de voltar para tras ainda nao existe a imagem de profundidade
            #self.image1 = pygame.image.load(image1).convert_alpha()
            #self.image2 = pygame.image.load(image2).convert_alpha() #profundidade

            self.touche = False

        def update(self):
            self.mouse = pygame.mouse.get_pressed()
            self.MousePos = pygame.mouse.get_pos()

            if self.rect.collidepoint(self.MousePos):

                if self.mouse[0]:
                    self.touche = True
                    pygame.mouse.get_rel()
                    #self.image = self.image2 #no botao de voltar para tras ainda nao existe a imagem de profundidade

                else:
                    self.touche = False
                    #self.image = self.image1 #no botao de voltar para tras ainda nao existe a imagem de profundidade

            pass

    ButtonGrups = pygame.sprite.Group()

    Botao1 = Botao11(ButtonGrups, image="imagens_gerais/voltaratras.png", image1="imagens_gerais/voltaratras.png",
                   image2="imagens_gerais/voltaratras.png")
    Botao1.rect.center = (50, 50)#localizaçao botão voltar atrás

    while JogoLoop:
        #fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JogoLoop = False
            if Botao1.touche == True:
                pygame.quit()
                main_menu()

            ButtonGrups.update()
            ButtonGrups.draw(tela)

            pygame.display.update()
        #pygame.display.update()

    pygame.quit()

def tela2():
    pygame.init()
    #fps = pygame.time.Clock()
    largura = 1024
    altura = 600

    JogoLoop = True

    tela = pygame.display.set_mode([largura, altura])
    tela.fill([255, 117, 24])
   # ColorBack = {"azul": [0, 132, 252], "vermelho": [137, 28, 36], "laranja": [255, 117, 24]}
    pygame.display.set_caption("Lucky Numbers")

    class Botao11(pygame.sprite.Sprite):
        def __init__(self, *groups, image, image1, image2):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [50, 50])#dimensoes botao voltar atras
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
                    #self.image = self.image1

            pass

    ButtonGrups = pygame.sprite.Group()

    Botao2 = Botao11(ButtonGrups, image="imagens_gerais/voltaratras.png", image1="imagens_gerais/voltaratras.png",
                   image2="imagens_gerais/voltaratras.png")
    Botao2.rect.center = (50, 50) #localizaçao botão voltar atrás

    while JogoLoop:
        #fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JogoLoop = False
            if Botao2.touche == True:
                pygame.quit()
                main_menu()

            ButtonGrups.update()
            ButtonGrups.draw(tela)

            pygame.display.update()
        #pygame.display.update()
    pygame.quit()

def tela3():
    pygame.init()
    #fps = pygame.time.Clock()
    largura = 1024
    altura = 600

    JogoLoop = True

    tela = pygame.display.set_mode([largura, altura])
    tela.fill([255, 117, 24])
   # ColorBack = {"azul": [0, 132, 252], "vermelho": [137, 28, 36], "laranja": [255, 117, 24]}
    pygame.display.set_caption("Lucky Numbers")

    class Botao11(pygame.sprite.Sprite):
        def __init__(self, *groups, image, image1, image2):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [50, 50])#dimensoes botao voltar atras
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
                    #self.image = self.image1

            pass

    ButtonGrups = pygame.sprite.Group()

    Botao3 = Botao11(ButtonGrups, image="imagens_gerais/voltaratras.png", image1="imagens_gerais/voltaratras.png",
                   image2="imagens_gerais/voltaratras.png")
    Botao3.rect.center = (50, 50) #localizaçao botão voltar atrás

    while JogoLoop:
        #fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JogoLoop = False
            if Botao3.touche == True:
                pygame.quit()
                main_menu()

            ButtonGrups.update()
            ButtonGrups.draw(tela)

            pygame.display.update()
        #pygame.display.update()
    pygame.quit()

def tela4():
    pygame.init()
    #fps = pygame.time.Clock()
    largura = 1024
    altura = 600

    JogoLoop = True

    tela = pygame.display.set_mode([largura, altura])
    tela.fill([255, 117, 24])
   # ColorBack = {"azul": [0, 132, 252], "vermelho": [137, 28, 36], "laranja": [255, 117, 24]}
    pygame.display.set_caption("Lucky Numbers")

    class Botao11(pygame.sprite.Sprite):
        def __init__(self, *groups, image, image1, image2):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [50, 50])#dimensoes botao voltar atras
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
                    #self.image = self.image1

            pass

    ButtonGrups = pygame.sprite.Group()

    Botao4 = Botao11(ButtonGrups, image="imagens_gerais/voltaratras.png", image1="imagens_gerais/voltaratras.png",
                   image2="imagens_gerais/voltaratras.png")
    Botao4.rect.center = (50, 50) #localizaçao botão voltar atrás

    while JogoLoop:
        #fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JogoLoop = False
            if Botao4.touche == True:
                pygame.quit()
                main_menu()

            ButtonGrups.update()
            ButtonGrups.draw(tela)

            pygame.display.update()
        #pygame.display.update()
    pygame.quit()
def tela5():
    pygame.init()

    # Definir o tamanho da janela
    window_surface = pygame.display.set_mode((800, 600))

    # Criar um gerenciador de eventos para lidar com eventos do Pygame GUI
    manager = pygame_gui.UIManager((800, 600))

    # Definir a fonte para a caixa de texto
    fonte = pygame.font.Font(None, 36)

    # Criar uma caixa de texto usando o Pygame GUI
    caixa_texto = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((300, 250), (200, 50)),
        manager=manager,
        # font=fonte
    )

    # Define o texto para o botão
    texto_botao = "Nome:"

    # Cria um botão usando o Pygame GUI
    botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((325, 325), (150, 50)),
                                         text=texto_botao,
                                         manager=manager
                                         )

    # Loop principal
    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            # Atualiza o gerenciador de eventos com os eventos do Pygame
            manager.process_events(event)

            # Verifica se o botão foi pressionado
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == botao:
                        # Recupera o texto da caixa de texto e imprime na tela
                        nome = caixa_texto.get_text()
                        print("Nome inserido:", nome)

            # Atualiza o gerenciador de eventos com o tempo
            manager.update(pygame.time.get_ticks() / 1000.0)

        # Desenha o fundo e os elementos do Pygame GUI na tela
        window_surface.fill((255, 255, 255))
        manager.draw_ui(window_surface)

        # Atualiza a janela do Pygame
        pygame.display.update()

    # Encerra o Pygame
    pygame.quit()

main_menu()

