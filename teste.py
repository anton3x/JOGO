import copy

import pygame
import pygame_gui
import sys
import random
import os

from Tela2 import tela2
from Tela3 import tela3
from Tela4 import tela4

def mem():
    # define o caminho para a pasta com as imagens
    path = "trevos"

    # lista o conteúdo da pasta
    files = os.listdir(path)

    # filtra apenas os arquivos com a extensão .png
    images = [file for file in files if file.endswith(".png")]

    # gera um número aleatório de 1 a 40
    random_number = random.randint(1, len(images))

    # concatena o número aleatório com a extensão ".png" para obter o nome da imagem
    random_image = str(random_number) + ".png"

    # exibe o nome da imagem aleatória escolhida
    print("A imagem aleatória escolhida é: " + random_image)
def initial_write_to_mem(name_player, player_board, excluidos, table):
    with open("save.txt", "w") as f:
        f.write(name_player +"/"+ str(player_board))
        f.write("\n")
        f.write("BOT/" + str(player_board))
        f.write("\n")
        f.write("excluidos/" + str(excluidos))
        f.write("\n")
        f.write("table/" + str(table))
    f.close()
def guardar_na_mem(name, tabuleiro_player, excluidos, table, jogador):
    dicionario = {}

    with open("save.txt", "r") as f:
        linhas = f.readlines()

    for linha in linhas:
        nome, tabuleiro_str = linha.strip().split("/")
        tabuleiro = eval(tabuleiro_str)
        dicionario[nome] = tabuleiro

    f.close()

    for x in dicionario.keys():
        if x == name:
            dicionario[x] = tabuleiro_player

    dicionario["excluidos"] = excluidos

    dicionario["table"] = table

    dicionario["jogador"] = [jogador]

    with open("save.txt", "w") as f:
        for y in dicionario.keys():
            f.write(y + "/" + str(dicionario[y]) + "\n")

    f.close()

    #print(dicionario)
def exibir_taboleiro(taboleiro,screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,posy14, posy15, posy16):
    for i in range(4):
        print(str(taboleiro[i][0]), " | ", str(taboleiro[i][1]), " | ", str(taboleiro[i][2]), " | ", str(taboleiro[i][3]))
    print("\n")


    n_botao = 0
    for i in range(4):#linhas
        for j in range(4):#colunas
            n_botao += 1
            if taboleiro[i][j] !=0:
                imagem_fundo = pygame.image.load("trevos/" + str(taboleiro[i][j]) + ".png").convert_alpha()
                imagem_fundo = pygame.transform.scale(imagem_fundo, (73, 73))
                x = eval("posx" + str(n_botao))
                y = eval("posy" + str(n_botao))
                screen.blit(imagem_fundo, (x - 36, y - 36))

    if taboleiro[4][0] != 0:
        imagem_fundo = pygame.image.load("trevos/" + str(taboleiro[4][0]) + ".png").convert_alpha()
        imagem_fundo = pygame.transform.scale(imagem_fundo, (73, 73))
        x = 281
        y = 615
        screen.blit(imagem_fundo, (x - 36, y - 36))


    pygame.display.flip()
    pygame.display.update()
def verificar_taboleiro(taboleiro, linha, coluna, trevo):
    taboleiro1 = copy.deepcopy(taboleiro)
    taboleiro1[linha][coluna] = trevo

    #print("TASSDADSAD -", taboleiro1)

    lista_coluna = []
    lista_linha = []
    """
    if trevo > 60:
        trevo_real = trevo - 60
    elif trevo > 40:
        trevo_real = trevo - 40
    elif trevo > 20:
        trevo_real = trevo - 20
    else:
        trevo_real = trevo
    """

    for i in range(4):
        if  taboleiro1[i][coluna] > 60:
            lista_coluna.append(taboleiro1[i][coluna] - 60)
        elif  taboleiro1[i][coluna] > 40:
            lista_coluna.append(taboleiro1[i][coluna] - 40)
        elif  taboleiro1[i][coluna] > 20:
            lista_coluna.append(taboleiro1[i][coluna] - 20)
        else:
            if taboleiro1[i][coluna] == 0:
                continue
            else:


                lista_coluna.append(taboleiro1[i][coluna])

        if taboleiro1[linha][i] > 60:
            lista_linha.append(taboleiro1[linha][i] - 60)
        elif taboleiro1[linha][i] > 40:
            lista_linha.append(taboleiro1[linha][i] - 40)
        elif taboleiro1[linha][i] > 20:
            lista_linha.append(taboleiro1[linha][i] - 20)
        else:
            if taboleiro1[linha][i] == 0:
                continue
            else:

                lista_linha.append(taboleiro1[linha][i])

    for i in range(len(lista_coluna)):
        if not (i == (len(lista_coluna) - 1)):
            if lista_coluna[i] > lista_coluna[i + 1]:
                return False
        else:
            continue
    for i in range(len(lista_linha)):
        if not (i == (len(lista_linha) - 1)):
            if lista_linha[i] > lista_linha[i + 1]:
                return False
        else:
            continue

    return True
def primeira_rodada(taboleiro, excluidos, totaltrevos): #funcao destinada a gerar os trevos e colocar no taboleiro na primeira ronda do jogo
    key = True
    #aVnE = False  # algum valor nos excluidos

    while key: #enquanto a key for verdade
        trevo = [] #cria-se uma lista de trevos vazia
        for i in range(4):  # gerar 4 valores de 1 até totaltrevos
            if len(trevo) == 0: # se a lista estiver vazia, qualquer trevo que sair poderá ser usado pois ainda nao existe nenhum
                b = random.randint(1, totaltrevos)  #gera-se um trevo
                trevo.append(b) #adiciona-se á lista dos trevos
                excluidos.append(b) # e adiciona-se á lista dos trevos ja usados
            else:   #se existirem trevos na lista de trevos
                key1 = True #key1 é verdade que vai ser usada para a geracao de um trevo
                while key1: #enquanto for verdade
                    t = random.randint(1, totaltrevos) #gera-se um trevo
                    if (t not in trevo) and (t not in excluidos):  #se ele nao estiver na lista, ou seja, se ele ainda nao foi usado desta vez e se nao foi usado no programa (lista excluidos)
                        key1 = False    #o loop while vai parar
                        trevo.append(t) #adiciona-se o trevo á lista
                        excluidos.append(t) #e adiciona-se o trevo á lista dos excluidos

        if len(trevo) == 4: #para parar o loop principal, se ja existirem os 4 elementos na lista dos trevos, a key vai ser falsa
            key = False

        """
        for i in range(4):
            if i == 3:  # se estiver no 4 elemento
                if trevo[i] not in excluidos and not aVnE:  # e o quarto elemento nao estiver na lista dos excluidos e a key ainda for True
                    key = False  # acaba o loop
                    for j in range(4):  # adiciona todos á lista dos excluidos, pois vao ser usados agora
                        excluidos.append(trevo[j])
                if trevo[i] in excluidos:
                    aVnE = True
        """

    elementos_vetor = [0, 0, 0, 0]  # usado para verificar se o elemento foi convertido no for em baixo, pois se lhe tirar 20 é dificil verificar se foi feita a operacao
    posicoes_originais = {}  # dicionário para armazenar as posições originais de cada elemento

    # remove 20 de todos os elementos > 20 e armazena as posições originais
    for i in range(4):
        if trevo[i] > 20:
            elementos_vetor[i] = 1
            trevo[i] -= 20
        posicoes_originais[trevo[i]] = i

    # ordena a lista
    lista_ordenada = sorted(trevo)

    # adiciona 20 aos elementos correspondentes
    for i in range(4):
        if elementos_vetor[posicoes_originais[lista_ordenada[i]]] == 1:
            lista_ordenada[i] += 20

        taboleiro[i][i] = lista_ordenada[i]

    return False
def turnoj(imagem_fundo, screen,nome, taboleiroj, excluidos, totaltrevos, key_inicial, table, jogador, imagem17_fundo, ButtonGrups, imagem2_fundo, imagem3_fundo, imagem4_fundo, imagem5_fundo, imagem6_fundo,imagem7_fundo, imagem8_fundo, imagem9_fundo, imagem10_fundo, imagem11_fundo,imagem12_fundo, imagem13_fundo, imagem14_fundo, imagem15_fundo, imagem16_fundo, Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17,imagem1_fundo, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,posy14, posy15, posy16, posy17=88, posx17=110):#funcao destinada ao turno do jogador
    print("JOGADOR")
    if key_inicial[1]: #se for a primeira jogada
        key_inicial[1] = primeira_rodada(taboleiroj, excluidos, totaltrevos)
        #exibir_taboleiro(taboleiroj)

    else:
        key = True
        if len(table) == 0:
            while key:
                trevo = random.randint(1, totaltrevos)
                if trevo not in excluidos:
                    key = False
                    excluidos.append(trevo)
            taboleiroj[4][0] = trevo #trevo escolhido para a parte debaixo do taboleiro
            exibir_taboleiro(taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                             posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                             posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                             posy14, posy15, posy16)
            pygame.display.flip()
            pygame.display.update()

            guardar_na_mem(nome, taboleiroj, excluidos, table,jogador)  # vai alterar na memoria os valores do taboleiro pelos atuais
        else:
            resposta = input("Queres usar algum trevo na table? (S/N): ")
            if resposta == "S" or resposta == "s":
                if len(table) != 1:
                    print("Table - ", table)
                    linha = int(input("Qual trevo queres da table(0-n): "))
                    trevo = table[linha]
                    table.remove(trevo)
                    taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                    exibir_taboleiro(taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                     posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                     posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                     posy14, posy15, posy16)
                    pygame.display.flip()
                    pygame.display.update()
                else:
                    trevo = table[0]
                    table.remove(trevo)
                    taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                    exibir_taboleiro(taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                     posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                     posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                     posy14, posy15, posy16)
                    pygame.display.flip()
                    pygame.display.update()
            else:
                key = True
                while key:
                    trevo = random.randint(1, totaltrevos)
                    if trevo not in excluidos:
                        key = False
                        excluidos.append(trevo)
                taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                exibir_taboleiro(taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                 posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                 posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                 posy14, posy15, posy16)
                pygame.display.flip()
                pygame.display.update()
        guardar_na_mem(nome, taboleiroj, excluidos, table,
                       jogador)  # vai alterar na memoria os valores do taboleiro pelos atuais

        print("Trevo - ", trevo)
        key = True
        #imagem17_fundo = pygame.transform.scale(imagem17_fundo, (73, 73))
        #screen.blit(imagem17_fundo, (281 - 36, 615 - 36))
        #exibir_taboleiro(taboleiroj, screen)
        #pygame.display.flip()
        #exibir_taboleiro(taboleiroj)

        while key:
            tabela = input("Queres colocar o trevo na table (S/N): ")
            if tabela == "S" or tabela == "s":
                table.append(trevo)
                key = False
                print("\nO trevo %d foi colocado na table\n" % trevo)
                taboleiroj[4][0] = 0
                screen.blit(imagem_fundo, (0,0))
                exibir_taboleiro(taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                 posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                 posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                 posy14, posy15, posy16)
                pygame.display.flip()
                pygame.display.update()
            else:
                #taboleiroj[4][0] = trevo #trevo escolhido para a parte debaixo do taboleiro
                exibir_taboleiro(taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                 posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                 posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                 posy14, posy15, posy16)
                pygame.display.flip()
                pygame.display.update()

                print("Posicao: ")

                resultado = escolha_posicao_trevo(ButtonGrups, screen, imagem2_fundo, imagem3_fundo, imagem4_fundo, imagem5_fundo, imagem6_fundo,
                                          imagem7_fundo, imagem8_fundo, imagem9_fundo, imagem10_fundo, imagem11_fundo,
                                          imagem12_fundo, imagem13_fundo, imagem14_fundo, imagem15_fundo, imagem16_fundo,
                                          imagem17_fundo, Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,
                                          Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17,
                                          imagem1_fundo, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                          posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                          posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                          posy14, posy15, posy16, posy17=88, posx17=110)
                linha = resultado[0]
                coluna = resultado[1]
                #print(linha,coluna)

                if taboleiroj[linha][coluna] == 0:
                    #print("verificar")
                    if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                        #print("feito")
                        print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (trevo, linha, coluna))
                        taboleiroj[linha][coluna] = trevo
                        key = False
                        taboleiroj[4][0] = 0
                        screen.blit(imagem_fundo, (0, 0))
                        pygame.display.flip()
                        pygame.display.update()

                else:
                    #print("verificar")
                    if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                        #print("feito")
                        print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (trevo, linha, coluna))
                        print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (taboleiroj[linha][coluna], trevo))
                        table.append(taboleiroj[linha][coluna])
                        taboleiroj[linha][coluna] = trevo
                        key = False
                        taboleiroj[4][0] = 0
                        screen.blit(imagem_fundo, (0, 0))
                        pygame.display.flip()
                        pygame.display.update()

    guardar_na_mem(nome, taboleiroj, excluidos, table, jogador) #vai alterar na memoria os valores do taboleiro pelos atuais
def turnob(taboleirob, excluidos,totaltrevos, key_inicial, table, jogador):#funcao destinada ao turno do bot
    if key_inicial[0]:#se for a primeira jogada
        print("BOT")
        key_inicial[0] = primeira_rodada(taboleirob, excluidos, totaltrevos)
        for i in range(4):
            print(str(taboleirob[i][0]), " | ", str(taboleirob[i][1]), " | ", str(taboleirob[i][2]), " | ", str(taboleirob[i][3]))
        print("\n")

    else:
        print("BOT")
        key = True

        while key:
            trevo = random.randint(1, totaltrevos)
            if trevo not in excluidos:
                key = False
                excluidos.append(trevo)

        key = True
        print("Bot retirou do baralho o trevo n: %d " % (trevo))

        while key:
            linha = random.randint(0, 3)
            coluna = random.randint(0, 3)
            if taboleirob[linha][coluna] == 0:
                if verificar_taboleiro(taboleirob, linha, coluna, trevo):
                    print("O bot colocou o trevo na linha %d e coluna %d\n" % (linha, coluna))
                    taboleirob[linha][coluna] = trevo
                    key = False
            else:
                if verificar_taboleiro(taboleirob, linha, coluna, trevo):
                    print("O bot colocou o trevo na linha %d e coluna %d\n" % (linha, coluna))
                    print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (taboleirob[linha][coluna], trevo))
                    table.append(taboleirob[linha][coluna])
                    taboleirob[linha][coluna] = trevo
                    key = False
        for i in range(4):
            print(str(taboleirob[i][0]), " | ", str(taboleirob[i][1]), " | ", str(taboleirob[i][2]), " | ",
                  str(taboleirob[i][3]))
        print("\n")
    #exibir_taboleiro(taboleirob)
    guardar_na_mem("BOT", taboleirob, excluidos, table, jogador)
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
    texto_botao = "Iniciar"

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
                        tela6(nome)
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
def tela6(nome):
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

    #jogo abaixo
    B_preenhido = False  # o bot ja preencheu o taboleiro?
    J_prenchido = False  # o jogador ja preencheu o taboleiro?
    trevos = []  # todos os trevos vao parar aqui para que nao haja repeticao na geracao de trevos
    taboleiroJ = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0]]  # taboleiro do jogador
    taboleiroB = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0]]  # taboleiro do bot
    table = []

    initial_write_to_mem(nome, taboleiroJ, trevos,table)  # guarda os taboleiros na mem com os nomes do bot e do jogador

    numero = 1#random.randint(0, 1)  # quem comeca

    Comeco = [True, True]
    if numero == 0:
        print("Bot começa!")
        while (not B_preenhido and not J_prenchido) and not (len(trevos) == 40):  # as condicoes de fim do jogo sao alguem ja ter preenchido to do o taboleiro ou os trevos esgotarem-se
            #aaa(imagem1_verde_exibida, imagem1_fundo, imagem17_fundo, imagem17_verde_exibida, Botao1, Botao17, screen, posx1, posy1, cor_de_fundo, imagem_fundo, ButtonGrups)
            turnob(taboleiroB, trevos, 20, Comeco, table, nome)
            turnoj(imagem_fundo,screen, nome, taboleiroJ, trevos, 20, Comeco, table, "BOT", imagem17_fundo,ButtonGrups, imagem2_fundo, imagem3_fundo, imagem4_fundo, imagem5_fundo, imagem6_fundo,
                                      imagem7_fundo, imagem8_fundo, imagem9_fundo, imagem10_fundo, imagem11_fundo,
                                      imagem12_fundo, imagem13_fundo, imagem14_fundo, imagem15_fundo, imagem16_fundo,
                                      Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,
                                      Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17,
                                      imagem1_fundo, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                      posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                      posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                      posy14, posy15, posy16, posy17=88, posx17=110)
            exibir_taboleiro(taboleiroJ, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                      posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                      posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                      posy14, posy15, posy16)
            # print(table)
            """a = int(input("cheat: "))
            if a == 0:
                B_preenhido = True
                J_prenchido = True
                """
        # print(trevos)
    else:
        print("O %s começa!" % nome)
        while (not B_preenhido or not J_prenchido) and not (len(trevos) == 40):
            #aaa(imagem1_verde_exibida, imagem1_fundo, imagem17_fundo, imagem17_verde_exibida, Botao1, Botao17, screen, posx1, posy1, cor_de_fundo, imagem_fundo, ButtonGrups)
            turnoj(imagem_fundo,screen, nome, taboleiroJ, trevos, 20, Comeco, table, "BOT", imagem17_fundo, ButtonGrups, imagem2_fundo, imagem3_fundo, imagem4_fundo, imagem5_fundo, imagem6_fundo,
                                      imagem7_fundo, imagem8_fundo, imagem9_fundo, imagem10_fundo, imagem11_fundo,
                                      imagem12_fundo, imagem13_fundo, imagem14_fundo, imagem15_fundo, imagem16_fundo,
                                      Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,
                                      Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17,
                                      imagem1_fundo, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                      posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                      posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                      posy14, posy15, posy16, posy17=88, posx17=110)
            exibir_taboleiro(taboleiroJ, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                      posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                      posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                      posy14, posy15, posy16)
            turnob(taboleiroB, trevos, 20, Comeco, table, nome)

            # print(table)
            """a = int(input("cheat: "))
            if a == 0:
                B_preenhido = True
                J_prenchido = True"""
        # print(trevos)


def aaa(imagem1_verde_exibida, imagem1_fundo, imagem17_fundo, imagem17_verde_exibida, Botao1, Botao17, screen, posx1, posy1, cor_de_fundo, imagem_fundo, ButtonGrups):
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

    if Botao17.touche == True:
        print("IMAGEM17")

            # exibe a imagem 1 verde
        imagem17_fundo = pygame.transform.scale(imagem17_fundo, (73, 73))
        screen.blit(imagem17_fundo, (281 - 36, 615 - 36))
        imagem17_verde_exibida = True
        keu = False

    ButtonGrups.draw(screen)
    ButtonGrups.update()
    screen.fill(cor_de_fundo)
    screen.blit(imagem_fundo, (0, 0))

    if imagem1_verde_exibida:  # evitar que seja possivel clicar varias vezes
        screen.blit(imagem1_fundo, (posx1 - 36, posy1 - 36))
    if imagem17_verde_exibida:  # evitar que seja possivel clicar varias vezes
        screen.blit(imagem17_fundo, (281 - 36, 615 - 36))

    pygame.display.flip()
    pygame.display.update()
def escolha_posicao_trevo(ButtonGrups,screen, imagem2_fundo,imagem3_fundo,imagem4_fundo,imagem5_fundo,imagem6_fundo,imagem7_fundo,imagem8_fundo,imagem9_fundo,imagem10_fundo,imagem11_fundo,imagem12_fundo,imagem13_fundo,imagem14_fundo,imagem15_fundo,imagem16_fundo,imagem17_fundo,Botao1,Botao2,Botao3,Botao4,Botao5,Botao6,Botao7,Botao8,Botao9,Botao10,Botao11,Botao12,Botao13,Botao14,Botao15,Botao16,Botao17,imagem1_fundo, posx1, posx2, posx3, posx4, posx5, posx6, posx7,posx8,posx9,posx10,posx11,posx12,posx13,posx14,posx15,posx16,posy1, posy2, posy3, posy4, posy5, posy6, posy7,posy8,posy9,posy10,posy11,posy12,posy13,posy14,posy15,posy16, posy17, posx17):
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            ButtonGrups.update()
        if Botao1.touche == True:
            print("IMAGEM1")

            # exibe a imagem 1 verde
            #imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
            #screen.blit(imagem1_fundo, (posx1 - 36, posy1 - 36))
            Botao1.touche = False
            return [0,0]
            imagem1_verde_exibida = True
        if Botao2.touche == True:
            print("IMAGEM2")

            # exibe a imagem 1 verde
            #imagem2_fundo = pygame.transform.scale(imagem2_fundo, (73, 73))
            #screen.blit(imagem2_fundo, (posx2 - 36, posy2 - 36))
            Botao2.touche = False
            return [0, 1]
            imagem2_verde_exibida = True
        if Botao3.touche == True:
            print("IMAGEM3")

            # exibe a imagem 1 verde
            #imagem3_fundo = pygame.transform.scale(imagem3_fundo, (73, 73))
            #screen.blit(imagem3_fundo, (posx3 - 36, posy3 - 36))
            Botao3.touche = False
            return [0, 2]
            imagem3_verde_exibida = True
        if Botao4.touche == True:
            print("IMAGEM4")

            # exibe a imagem 1 verde
            #imagem4_fundo = pygame.transform.scale(imagem4_fundo, (73, 73))
            #screen.blit(imagem4_fundo, (posx4 - 36, posy4 - 36))
            Botao4.touche = False
            return [0, 3]
            imagem4_verde_exibida = True
        if Botao5.touche == True:
            print("IMAGEM5")

            # exibe a imagem 1 verde
            #imagem5_fundo = pygame.transform.scale(imagem5_fundo, (73, 73))
            #screen.blit(imagem5_fundo, (posx5 - 36, posy5 - 36))
            Botao5.touche = False
            return [1,0]
            imagem5_verde_exibida = True
        if Botao6.touche == True:
            print("IMAGEM6")

            # exibe a imagem 1 verde
            #imagem6_fundo = pygame.transform.scale(imagem6_fundo, (73, 73))
            # screen.blit(imagem6_fundo, (posx6 - 36, posy6 - 36))
            Botao6.touche = False
            return [1,1]
            imagem6_verde_exibida = True
        if Botao7.touche == True:
            print("IMAGEM7")

            # exibe a imagem 1 verde
            #imagem7_fundo = pygame.transform.scale(imagem7_fundo, (73, 73))
            # screen.blit(imagem7_fundo, (posx7 - 36, posy7 - 36))
            Botao7.touche = False
            return [1, 2]
            imagem7_verde_exibida = True
        if Botao8.touche == True:
            print("IMAGEM8")

            # exibe a imagem 1 verde
            #imagem8_fundo = pygame.transform.scale(imagem8_fundo, (73, 73))
            #screen.blit(imagem8_fundo, (posx8 - 36, posy8 - 36))
            Botao8.touche = False
            return [1,3]
            imagem8_verde_exibida = True
        if Botao9.touche == True:
            print("IMAGEM9")

            # exibe a imagem 1 verde
            #imagem9_fundo = pygame.transform.scale(imagem9_fundo, (73, 73))
            #screen.blit(imagem9_fundo, (posx9 - 36, posy9 - 36))
            Botao9.touche = False
            return [2,0]
            imagem9_verde_exibida = True
        if Botao10.touche == True:
            print("IMAGEM10")

            # exibe a imagem 1 verde
            #imagem10_fundo = pygame.transform.scale(imagem10_fundo, (73, 73))
            #screen.blit(imagem10_fundo, (posx10 - 36, posy10 - 36))
            Botao10.touche = False
            return [2,1]
            imagem10_verde_exibida = True
        if Botao11.touche == True:
            print("IMAGEM11")

            # exibe a imagem 1 verde
            #imagem11_fundo = pygame.transform.scale(imagem11_fundo, (73, 73))
            #screen.blit(imagem11_fundo, (posx11 - 36, posy11 - 36))
            Botao11.touche = False
            return [2,2]
            imagem11_verde_exibida = True
        if Botao12.touche == True:
            print("IMAGEM12")

            # exibe a imagem 1 verde
            #imagem12_fundo = pygame.transform.scale(imagem12_fundo, (73, 73))
            #screen.blit(imagem12_fundo, (posx12 - 36, posy12 - 36))
            Botao12.touche = False
            return [2,3]
            imagem12_verde_exibida = True
        if Botao13.touche == True:
            print("IMAGEM13")

            # exibe a imagem 1 verde
            #imagem13_fundo = pygame.transform.scale(imagem13_fundo, (73, 73))
            #screen.blit(imagem13_fundo, (posx13 - 36, posy13 - 36))
            Botao13.touche = False
            return [3,0]
            imagem13_verde_exibida = True
        if Botao14.touche == True:
            print("IMAGEM14")

            # exibe a imagem 1 verde
            #imagem14_fundo = pygame.transform.scale(imagem14_fundo, (73, 73))
            #screen.blit(imagem14_fundo, (posx14 - 36, posy14 - 36))
            Botao14.touche = False
            return [3, 1]
            imagem14_verde_exibida = True
        if Botao15.touche == True:
            print("IMAGEM15")

            # exibe a imagem 1 verde
            #imagem15_fundo = pygame.transform.scale(imagem15_fundo, (73, 73))
            #screen.blit(imagem15_fundo, (posx15 - 36, posy15 - 36))
            Botao15.touche = False
            return [3,2]
            imagem15_verde_exibida = True
        if Botao16.touche == True:
            print("IMAGEM16")

            # exibe a imagem 1 verde
            #imagem16_fundo = pygame.transform.scale(imagem16_fundo, (73, 73))
            #screen.blit(imagem16_fundo, (posx16 - 36, posy16 - 36))
            Botao16.touche = False
            return [3,3]
            imagem16_verde_exibida = True

        """if Botao17.touche == True:
            print("IMAGEM17")

            # exibe a imagem 1 verde
            imagem17_fundo = pygame.transform.scale(imagem17_fundo, (73, 73))
            screen.blit(imagem17_fundo, (281 - 36, 615 - 36))
            return [0,0]
            imagem17_verde_exibida = True
        """

        pygame.display.flip()
        pygame.display.update()

main_menu()