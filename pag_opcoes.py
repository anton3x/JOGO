import pygame
import pygame_gui
import sys
from jogo_normal_new import novo_jogo_normal
from load_normal import load_jogo_normal
from jogo_tm_new import novo_jogo_tm
from jogo_mm_new import novo_jogo_mm

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

    Botao1 = Botao(ButtonGrups,image="imagens_gerais/Novo_Jogo_01.png",image1="imagens_gerais/Novo_Jogo_01.png",image2="imagens_gerais/Novo_Jogo_02.png")
    Botao1.rect.center = (381, 350)

    Botao2 = Botao(ButtonGrups,image="imagens_gerais/carregar_jogo_01.png",image1="imagens_gerais/carregar_jogo_01.png",image2="imagens_gerais/carregar_jogo_02.png")
    Botao2.rect.center = (643, 350)

    Botao4 = Botao(ButtonGrups,image="imagens_gerais/Sair_01.png",image1="imagens_gerais/Sair_01.png",image2="imagens_gerais/sair_02.png")
    Botao4.rect.center = (643, 450)

    Botao3 = Botao(ButtonGrups,image="imagens_gerais/Regras_01.png",image1="imagens_gerais/Regras_01.png",image2="imagens_gerais/Regras_02.png")
    Botao3.rect.center = (381, 450)


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
                load_jogo_normal()

            if Botao3.touche == True:
                tela.fill(ColorBack["azul"])
                tela3()

            if Botao4.touche == True:
                pygame.quit()


        tela.fill(ColorBack["azul"])
        ButtonGrups.update()
        ButtonGrups.draw(tela)
        # Desenha a imagem no lado direito

        imagem = pygame.transform.scale(imagem, (420, 245))
        tela.blit(imagem, (291.5, 20))
        pygame.display.flip()

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


    label_jogador1 = message_to_screen("Jogador 1:", None, 25, [255, 255, 255])
    entry_jogador1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 100), (200, 50)),
                                                         manager=gerenciador)

    label_jogador2 = message_to_screen("Jogador 2:", None, 25, [255, 255, 255])
    entry_jogador2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((200, 175), (200, 50)),
                                                         manager=gerenciador)
    entry_jogador2.hide()

    label_variante = message_to_screen("Variante:", None, 25, [255, 255, 255])
    dropdown_variante = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((200, 175), (200, 100)),
        item_list=["Normal", "MICHAEL’S SETUP", "TOURNAMENT MODE"],
        manager=gerenciador)

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
    label_variante_mostrar_abaixo = False
    label_oponente_mostrar_abaixo = False


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
                            dropdown_variante.set_position((200, 240))
                            dropdown_oponente.set_position((200, 350))
                            botao_iniciar.set_position((180, 460))

                            label2_mostrar = True
                            label_oponente_mostrar_abaixo = True
                            label_variante_mostrar_abaixo = True


                            ButtonGrups.update()
                            pygame.display.flip()
                            pygame.display.update()

                        else:
                            label2_mostrar = False
                            entry_jogador2.hide()

                            dropdown_variante.set_position((200, 175))
                            dropdown_oponente.set_position((200, 300))
                            botao_iniciar.set_position((180, 440))

                            label_oponente_mostrar_abaixo = False
                            label_variante_mostrar_abaixo = False


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
                            if oponente == "Bot":
                                novo_jogo_normal(jogador1, "BOT")
                            elif oponente =="Outro jogador":
                                novo_jogo_normal(jogador1, jogador2)
                        if variante == "MICHAEL’S SETUP":
                            if oponente == "Bot":
                                novo_jogo_mm(jogador1, "BOT")
                            elif oponente == "Outro jogador":
                                novo_jogo_normal(jogador1, jogador2)
                        if variante == "TOURNAMENT MODE":
                            if oponente == "Bot":
                                novo_jogo_tm(jogador1, "BOT")
                            elif oponente =="Outro jogador":
                                novo_jogo_tm(jogador1, jogador2)


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
        gerenciador.update(tempo)
        pygame.display.flip()
        janela.fill((0, 132, 251))
        gerenciador.draw_ui(janela)

        janela.blit(label_jogador1, (150 - label_jogador1.get_width() // 2, 125 - label_jogador1.get_height() // 2))
        if label2_mostrar:
            janela.blit(label_jogador2, (150 - label_jogador2.get_width() // 2, 199 - label_jogador2.get_height() // 2))

        if label_oponente_mostrar_abaixo:
            janela.blit(label_oponente, (150 - label_oponente.get_width() // 2, 375 - label_oponente.get_height() // 2))
        else:
            janela.blit(label_oponente, (150 - label_oponente.get_width() // 2, 345 - label_oponente.get_height() // 2))

        if label_variante_mostrar_abaixo:
            janela.blit(label_variante, (150 - label_variante.get_width() // 2, 275 - label_variante.get_height() // 2))
        else:
            janela.blit(label_variante, (150 - label_variante.get_width() // 2, 220 - label_variante.get_height() // 2))


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

    pygame.quit()
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
        html_text="<body><font color='#FFA500' face='Times New Roman'><b>Ideia de Jogo:</b></font> Cada jogador tenta ser o primeiro a preencher completamente o seu jardim com trevos. Mas eles devem verificar se os números estão organizados em ordem crescente em cada linha e coluna.</body>"
                  "\n<font color='#FFA500' face='Arial'><b>Configuração do Jogo:</b></font> Usa um conjunto completo de trevos (= 1 cor numerada de 1 a 20) por jogador. Com menos de 4 jogadores, devolve as peças não utilizadas à caixa do jogo. \n Embaralha os trevos e coloca-os virados para baixo no meio da mesa. \n Cada jogador leva um jogo bordo e orienta-o para que a joaninha esteja no canto inferior direito.</body>"
                  "\n<font color='#FFA500' face='Verdana'><b>GamePlay:</b></font> O jogador mais velho começa e, em seguida, o jogo prossegue no sentido horário. Na tua vez, deves escolher uma das duas opções a seguir:"
                  "\n<font color='#FFA500' face='Comic Sans MS'><b>A) Take a face-down clover:</b></font> Pega um trevo virado para baixo do meio da mesa e coloca-o, virado para cima, no tabuleiro de jogo (vê Regras de Colocação à direita). Se não podes ou não queres colocá-lo, deixa-lo, virado para cima no meio da mesa."
                  "\n<font color='#FFA500' face='Comic Sans MS'><b>B) Take a face-up clover:</b></font> Não reveles outro trevo. Em vez disso, pega um dos trevos virados para cima e adicioná-lo ao tabuleiro de jogo em de acordo com as Regras de Colocação</b></font>."
                  "\n<font color='#FFA500' face='Comic Sans MS'><b>Regras de Colocação:</b></font> Podes adicionar um novo trevo a um espaço vazio no tabuleiro de jogo ou trocá-lo por um trevo colocado anteriormente (e devolver o trevo trocado no meio da mesa, com a face para cima)."
                  "\nO número do trevo que colocas no tabuleiro deve caber, em ordem crescente, com todos os outros números na sua linha e na sua coluna (mas os números em uma linha ou coluna não precisam seguir uns aos outros como 7,8,9...). "
                  "</body>",
        relative_rect=text_box_rect,
        manager=ui_manager)

    # Define a cor de fundo da tela
    BACKGROUND_COLOR = ([0, 132, 252])

    imagem_regras = pygame.image.load("imagens_gerais/REGRAS.png")

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

    ButtonGrups = pygame.sprite.Group()

    Botao3 = Botao11(ButtonGrups, image="imagens_gerais/x.png", image1="imagens_gerais/x.png",
                   image2="imagens_gerais/x.png", dim=60)
    Botao3.rect.center = (50, 50) #localizaçao botão voltar atrás
    i = 1
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

            pygame.display.flip()
            pygame.display.update()

            ui_manager.process_events(event)

        ui_manager.update(clock.tick(60) / 1000.0)

        screen.fill(BACKGROUND_COLOR)
        imagem_regras = pygame.transform.scale(imagem_regras, (420, 245))

        screen.blit(imagem_regras, (280, -40))

        ui_manager.draw_ui(screen)
        ButtonGrups.update()
        ButtonGrups.draw(screen)
        if i == 1:
            pygame.display.flip()
            pygame.display.update()
            i=0


main_menu()