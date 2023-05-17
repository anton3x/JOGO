import pygame
import pygame_gui
import sys
from jogo_tm import jogo_tm

def message_to_screen(message, textfont, size, color):
    my_font = pygame.font.Font(textfont, size)
    my_message = my_font.render(message, True, color)
    return my_message

def main_menu():
    #pygame.init()
    fps = pygame.time.Clock()
    largura = 1024
    altura = 600

    JogoLoop = True

    tela = pygame.display.set_mode([largura, altura])
    pygame.display.set_caption("Lucky Numbers")

    imagem = pygame.image.load("imagens_jogo\Lucky-logo.png")
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
                tela1()
                #tela5()

            if Botao2.touche == True:
                tela.fill(ColorBack["azul"])
                tela2()

            if Botao3.touche == True:
                tela.fill(ColorBack["azul"])
                tela3()


            if Botao4.touche == True:
                pygame.quit()

            else:
                tela.fill(ColorBack["azul"])

            ButtonGrups.update()
            ButtonGrups.draw(tela)
            pygame.display.update()
        # Desenha a imagem no lado direito
    pygame.quit()
def tela1():
    pygame.init()

    # Configurações da janela
    tamanho_janela = (1024, 600)
    janela = pygame.display.set_mode(tamanho_janela)
    pygame.display.set_caption("Lucky Numbers")

    # Inicializa o gerenciador da interface do usuário
    gerenciador = pygame_gui.UIManager(tamanho_janela)

    # Carrega a imagem
    imagem = pygame.image.load("imagens_jogo/Lucky-logo.png")
    #imagem_jogador1 = pygame.image.load("imagens_gerais/jogador_1.png")

    # Cria os elementos da interface do usuário com font_size maior

    #label_jogador1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 100), (100, 50)), text="Jogador 1:",
                                                 #manager=gerenciador)
    label_jogador1 = message_to_screen("Jogador 1:", None, 25, [255, 255, 255])
    entry_jogador1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 100), (200, 50)),
                                                         manager=gerenciador)

    #label_jogador2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 200), (100, 50)), text="Jogador 2:",
                                                # manager=gerenciador)
    label_jogador2 = message_to_screen("Jogador 2:", None, 25, [255, 255, 255])
    entry_jogador2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 200), (200, 50)),
                                                         manager=gerenciador)
    entry_jogador2.hide()
    #label_jogador2.hide()

    #label_variante = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 175), (100, 50)),text="Variante:",manager=gerenciador)
    label_variante = message_to_screen("Variante:", None, 25, [255, 255, 255])
    dropdown_variante = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((200, 175), (200, 100)),
        item_list=["Normal", "MICHAEL’S SETUP", "TOURNAMENT MODE"],
        manager=gerenciador)

    #label_oponente = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 300), (100, 50)),text="Oponente:",manager=gerenciador)
    label_oponente = message_to_screen("Oponente:", None, 25, [255, 255, 255])
    dropdown_oponente = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((200, 300), (200, 100)),
        item_list=["Bot", "Outro jogador"], manager=gerenciador)

    botao_iniciar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((180, 440), (240, 100)),
                                                 text="Começar Jogo",
                                                 manager=gerenciador)

    class Botao11(pygame.sprite.Sprite):
        def __init__(self, *groups, image, image1, image2):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [70, 70])  # dimensoes botao voltar atras
            self.rect = pygame.Rect(65, 53, 58, 66)
            self.rect = self.image.get_rect()

            # no botao de voltar para tras ainda nao existe a imagem de profundidade
            # self.image1 = pygame.image.load(image1).convert_alpha()
            # self.image2 = pygame.image.load(image2).convert_alpha() #profundidade

            self.touche = False

        def update(self):
            self.mouse = pygame.mouse.get_pressed()
            self.MousePos = pygame.mouse.get_pos()

            if self.rect.collidepoint(self.MousePos):

                if self.mouse[0]:
                    self.touche = True
                    pygame.mouse.get_rel()
                    # self.image = self.image2 #no botao de voltar para tras ainda nao existe a imagem de profundidade

                else:
                    self.touche = False
                    # self.image = self.image1 #no botao de voltar para tras ainda nao existe a imagem de profundidade

            pass

    ButtonGrups = pygame.sprite.Group()

    Botao1 = Botao11(ButtonGrups, image="imagens_gerais/x.png", image1="imagens_gerais/x.png",
                     image2="imagens_gerais/x.png")
    Botao1.rect.center = (65, 53)  # localizaçao botão voltar atrás
    tempo = pygame.time.Clock().tick(60)
    # Loop principal
    label2_mostrar = False
    rodando = True
    while rodando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()

            if evento.type == pygame.USEREVENT:
                if evento.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                    if evento.ui_element == dropdown_oponente:
                        if evento.text == "Outro jogador":
                            entry_jogador2.show()
                            #label_jogador2.show()
                            #label_variante.set_position((100, 300))
                            #label_oponente.set_position((100, 400))
                            dropdown_variante.set_position((200, 300))
                            dropdown_oponente.set_position((200, 400))
                            botao_iniciar.set_position((160, 540))
                            label2_mostrar = True

                            ButtonGrups.update()
                            pygame.display.flip()
                            pygame.display.update()

                        else:
                            label2_mostrar = False
                            entry_jogador2.hide()
                            #label_jogador2.hide()
                            #label_variante.set_position((100, 175))
                            #label_oponente.set_position((100, 300))
                            dropdown_variante.set_position((200, 175))
                            dropdown_oponente.set_position((200, 300))
                            botao_iniciar.set_position((160, 440))
                            ButtonGrups.update()
                            ButtonGrups.draw(janela)

                            pygame.display.flip()
                            gerenciador.process_events(evento)

                if evento.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if evento.ui_element == botao_iniciar:
                        jogador1 = entry_jogador1.get_text()
                        jogador2 = entry_jogador2.get_text()
                        variante = dropdown_variante.get_single_selection()
                        oponente = dropdown_oponente.get_single_selection()

                        if variante == "Normal":
                            jogo_normal(jogador1, jogador2, oponente)
                        elif variante == "MICHAEL’S SETUP":
                            jogo_ms(jogador1, jogador2, oponente)
                        else:
                            jogo_tm(jogador1, jogador2, oponente)

                        print("Jogador 1:", jogador1)
                        print("Jogador 2:", jogador2)
                        print("Variante escolhida:", variante)
                        print("Oponente:", oponente)

            if Botao1.touche == True:
                rodando = False
                pygame.quit()
                main_menu()

            ButtonGrups.update()
            ButtonGrups.draw(janela)

            pygame.display.flip()
            gerenciador.process_events(evento)

        ButtonGrups.update()
        ButtonGrups.draw(janela)
        pygame.display.flip()
        gerenciador.update(tempo)
        janela.fill((0, 132, 251))
        gerenciador.draw_ui(janela)

        janela.blit(label_jogador1, (150 - label_jogador1.get_width() // 2, 125 - label_jogador1.get_height() // 2))
        if label2_mostrar:
            janela.blit(label_jogador2, (150 - label_jogador2.get_width() // 2, 220 - label_jogador2.get_height() // 2))

        imagem = pygame.transform.scale(imagem, (420, 245))
        #imagem_jogador1 = pygame.transform.scale(imagem_jogador1,(80,20))
        # Desenha a imagem no lado direito
        janela.blit(imagem, (495, 180))
        #janela.blit(imagem_jogador1, (110,115))
pygame.quit()
def tela2():
    pygame.init()
    #fps = pygame.time.Clock()
    largura = 1024
    altura = 600

    JogoLoop = True

    tela = pygame.display.set_mode([largura, altura])
    tela.fill([0, 132, 251])
   # ColorBack = {"azul": [0, 132, 252], "vermelho": [137, 28, 36], "laranja": [255, 117, 24]}
    pygame.display.set_caption("Lucky Numbers")
    gerenciador = pygame_gui.UIManager((largura, altura))
    # Criar o botão "Carregar Jogo"
    botao_carregar_jogo = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((275, 200), (200, 40)), text='Carregar Jogo', manager=gerenciador)

    class Botao11(pygame.sprite.Sprite):
        def __init__(self, *groups, image, image1, image2):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [70, 70])#dimensoes botao voltar atras
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
                    #self.image = self.image2

                else:
                    self.touche = False
                    #self.image = self.image1

            pass

    ButtonGrups = pygame.sprite.Group()

    Botao2 = Botao11(ButtonGrups, image="imagens_gerais/x.png", image1="imagens_gerais/x.png",
                   image2="imagens_gerais/x.png")
    Botao2.rect.center = (50, 50) #localizaçao botão voltar atrás


    while JogoLoop:
        #fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JogoLoop = False
            if Botao2.touche == True:
                pygame.quit()
                main_menu()
            gerenciador.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == botao_carregar_jogo:
                        # Carregar o jogo aqui
                        print("Jogo carregado com sucesso!")

            ButtonGrups.update()
            ButtonGrups.draw(tela)

            gerenciador.update(pygame.time.Clock().tick(60))
            gerenciador.draw_ui(tela)

            pygame.display.update()


    pygame.quit()
def tela3():
    pygame.init()
    #fps = pygame.time.Clock()
    largura = 1024
    altura = 600

    JogoLoop = True

    tela = pygame.display.set_mode([largura, altura])
    tela.fill([0, 132, 251])
   # ColorBack = {"azul": [0, 132, 252], "vermelho": [137, 28, 36], "laranja": [255, 117, 24]}
    pygame.display.set_caption("Lucky Numbers")

    regras_jogo()

    while JogoLoop:
        #fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JogoLoop = False


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
                        #tela6()
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
def jogo_normal(jogador1,jogador2,oponente):
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
        def __init__(self, *groups, image, image1, image2, posx, posy, dim=73):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()

            self.rect = pygame.Rect(posx, posy, dim, dim)

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
    Botao17 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=110, posy=88, dim=44)
    Botao17.rect.center = (110, 88)

    # dá load da imagem
    imagem1_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem2_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem3_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem4_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem5_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem6_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem7_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem8_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem9_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem10_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem11_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem12_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem13_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem14_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem15_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem16_fundo = pygame.image.load("verdes/1.png").convert_alpha()
    imagem17_fundo = pygame.image.load("verdes/1.png").convert_alpha()

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
    imagem17_verde_exibida = False

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

        if Botao17.touche == True:
            print("IMAGEM17")

            # exibe a imagem 1 verde
            imagem17_fundo = pygame.transform.scale(imagem17_fundo, (73, 73))
            screen.blit(imagem17_fundo, (281 - 36, 615 - 36))
            imagem17_verde_exibida = True

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
        if imagem17_verde_exibida:  # evitar que seja possivel clicar varias vezes
            screen.blit(imagem17_fundo, (281 - 36, 615 - 36))

        pygame.display.flip()
        pygame.display.update()
def regras_jogo():
    pygame.init()

    # Define as dimensões da tela e cria a superfície
    largura = 1024
    altura = 600
    screen = pygame.display.set_mode((largura, altura))

    # Cria um gerenciador de interface de usuário e define o tema
    ui_manager = pygame_gui.UIManager((largura, altura), 'data/themes/theme_1.json')

    # Define as dimensões e a posição da caixa de texto
    largura_textbox = 800
    altura_textbox = 400
    posição_x_textbox = 100
    posição_y_textbox = 150
    text_box_rect = pygame.Rect(posição_x_textbox, posição_y_textbox, largura_textbox, altura_textbox)

    # Cria a caixa de texto
    text_box = pygame_gui.elements.UITextBox(
        html_text="<body><font color>O jogo é composto por dois tabuleiros de 4x4 espaços (casas) para cada jogador. Para jogar usam-se os trevos numerados de 1 a 20; um conjunto por cada jogador. Os trevos de ambos os jogadores são misturados num só saco. À vez, cada jogador retira um trevo do saco colocando-o no seu tabuleiro. Deve primeiro preencher os 4 espaços da diagonal principal e de seguida os restantes espaços. Como regra de base, quer na vertical quer na horizontal os números devem ser colocados em ordem estritamente crescente. As restantes regras podem ser lidas no ficheiro em "
                  "f k.</font></body>",
        relative_rect=text_box_rect,
        manager=ui_manager)

    # Define a cor de fundo da tela
    BACKGROUND_COLOR = ([0, 132, 252])

    imagem_regras = pygame.image.load("imagens_gerais/REGRAS.png")

    class Botao11(pygame.sprite.Sprite):
        def __init__(self, *groups, image, image1, image2):
            super().__init__(*groups)

            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, [70, 70])#dimensoes botao voltar atras
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
                    #self.image = self.image2

                else:
                    self.touche = False
                    #self.image = self.image1

            pass

    ButtonGrups = pygame.sprite.Group()

    Botao3 = Botao11(ButtonGrups, image="imagens_gerais/x.png", image1="imagens_gerais/x.png",
                   image2="imagens_gerais/x.png")
    Botao3.rect.center = (50, 50) #localizaçao botão voltar atrás

    # Loop principal do jogo
    clock = pygame.time.Clock()
    while True:
        # Processa os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if Botao3.touche == True:
                pygame.quit()
                main_menu()
            ui_manager.process_events(event)

        ui_manager.update(clock.tick(60) / 1000.0)

        screen.fill(BACKGROUND_COLOR)
        imagem_regras = pygame.transform.scale(imagem_regras, (420, 245))

        screen.blit(imagem_regras, (280, -40))

        ui_manager.draw_ui(screen)
        pygame.display.flip()

































        ButtonGrups.update()
        ButtonGrups.draw(screen)

        pygame.display.flip()
        pygame.display.update()
def jogo_ms(jogador1,jogador2,oponente):
    print("Variante MICHAEL’S SETUP")
main_menu()
