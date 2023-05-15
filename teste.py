import copy
from config_jog1 import *
from config_jog2 import *
import pygame
import pygame_gui
import sys
import random
import os

def joaninha(joana, screen, jog="jog1"):
    joana = pygame.transform.scale(joana, (37, 37))
    if jog=="jog1":
        screen.blit(joana, (442, 178))
    else:
        screen.blit(joana, (880, 178))
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
def exibir_taboleiro(cond_final, taboleiro,screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1, Bot=0):
    for i in range(4):
        print(str(taboleiro[i][0]), " | ", str(taboleiro[i][1]), " | ", str(taboleiro[i][2]), " | ", str(taboleiro[i][3]))
    print("\n")

    n_botao = 0
    contador = 0

    if Bot != 1:
        for i in range(4):#linhas
            for j in range(4):#colunas
                n_botao += 1
                if taboleiro[i][j] !=0:
                    contador += 1
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

        if contador == 16:
            cond_final[1] = True
    else:
        for i in range(4):  # linhas
            for j in range(4):  # colunas
                n_botao += 1
                if taboleiro[i][j] != 0:
                    imagem_fundo = pygame.image.load("trevos/" + str(taboleiro[i][j]) + ".png").convert_alpha()
                    imagem_fundo = pygame.transform.scale(imagem_fundo, (73, 73))
                    x = eval("posx" + str(n_botao) + "_1")
                    y = eval("posy" + str(n_botao)+ "_1")
                    screen.blit(imagem_fundo, (x - 36, y - 36))

        if taboleiro[4][0] != 0:
            imagem_fundo = pygame.image.load("trevos/" + str(taboleiro[4][0]) + ".png").convert_alpha()
            imagem_fundo = pygame.transform.scale(imagem_fundo, (73, 73))
            x = 726
            y = 615
            screen.blit(imagem_fundo, (x - 36, y - 36))
        if contador == 16:
            cond_final[0] = True


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
def turnoj(cond_final, imagem_fundo, screen,nome, taboleiroj, excluidos, totaltrevos, key_inicial, table, jogador, ButtonGrups, Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17,Botao18, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,posy14, posy15, posy16, posy17=88, posx17=110):#funcao destinada ao turno do jogador

    joana = pygame.image.load("imagens_jogo/joaninha.png").convert_alpha()
    joana = pygame.transform.scale(joana, (37, 37))
    screen.blit(joana, (442, 178))

    print("JOGADOR")
    if key_inicial[1]: #se for a primeira jogada
        key_inicial[1] = primeira_rodada(taboleiroj, excluidos, totaltrevos)
        #exibir_taboleiro(taboleiroj)

    else:
        key = True
        if len(table) == 0: #quando nao existem trevos na table, tem que gerar um novo
            while key:
                trevo = random.randint(1, totaltrevos)
                if trevo not in excluidos:
                    key = False
                    excluidos.append(trevo)
            taboleiroj[4][0] = trevo #trevo escolhido para a parte debaixo do taboleiro
            exibir_taboleiro(cond_final, taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                             posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                             posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                             posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1)
            pygame.display.flip()
            pygame.display.update()

            guardar_na_mem(nome, taboleiroj, excluidos, table,jogador)  # vai alterar na memoria os valores do taboleiro pelos atuais
        else:   #se ja existirem trevos na table, pode usar um do baralho ou usar um da table
            print(table)
            key1 = True
            while key1:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    ButtonGrups.update()
                if Botao18.touche == True: #pressionou a table
                    print("TABLE TOCADA")

                    if len(table) != 1: #se existirem mais que um elementos na table, tem que escolher qual quer
                        Botao18.touche = False
                        print("Table - ", table)
                        linha = int(input("Qual trevo queres da table(0-n): "))
                        trevo = table[linha]
                        table.remove(trevo)
                        taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                        exibir_taboleiro(cond_final, taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8,
                                         posx9,
                                         posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                         posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12,
                                         posy13,
                                         posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1)
                        pygame.display.flip()
                        pygame.display.update()
                        break
                    else:   #se só existir 1, tem que ser o que está lá
                        Botao18.touche = False
                        trevo = table[0]
                        table.remove(trevo)
                        taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                        exibir_taboleiro(cond_final, taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8,
                                         posx9,
                                         posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                         posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12,
                                         posy13,
                                         posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1)
                        pygame.display.flip()
                        pygame.display.update()

                    # exibe a imagem 1 verde
                    # imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
                    # screen.blit(imagem1_fundo, (posx1 - 36, posy1 - 36))
                    break
                if Botao17.touche == True:  #se ele pressionou o baralho
                    key = True
                    while key:
                        trevo = random.randint(1, totaltrevos)
                        if trevo not in excluidos:
                            key = False
                            excluidos.append(trevo)
                    taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                    exibir_taboleiro(cond_final, taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                     posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                     posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                     posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1)
                    pygame.display.flip()
                    pygame.display.update()

                    Botao17.touche = False
                    break



        guardar_na_mem(nome, taboleiroj, excluidos, table,jogador)  # vai alterar na memoria os valores do taboleiro pelos atuais

        print("Trevo - ", trevo)
        key = True
        #imagem17_fundo = pygame.transform.scale(imagem17_fundo, (73, 73))
        #screen.blit(imagem17_fundo, (281 - 36, 615 - 36))
        #exibir_taboleiro(taboleiroj, screen)
        #pygame.display.flip()
        #exibir_taboleiro(taboleiroj)

        while key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                ButtonGrups.update()
            if Botao18.touche == True:
                print("TABLE TOCADA")
                table.append(trevo)
                key = False
                print("\nO trevo %d foi colocado na table\n" % trevo)
                taboleiroj[4][0] = 0
                screen.blit(imagem_fundo, (0, 0))
                exibir_taboleiro(cond_final, taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                 posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                 posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                 posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1)
                Botao18.touche = False
                pygame.display.flip()
                pygame.display.update()
                break
            else:
                #taboleiroj[4][0] = trevo #trevo escolhido para a parte debaixo do taboleiro
                exibir_taboleiro(cond_final, taboleiroj, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                 posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                 posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                 posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1)
                pygame.display.flip()
                pygame.display.update()

                print("Posicao: ")

                resultado = escolha_posicao_trevo(ButtonGrups, screen,
                                          Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,
                                          Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17,Botao18,
                                          posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                          posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                          posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                          posy14, posy15, posy16, posy17=88, posx17=110)
                linha = resultado[0]
                coluna = resultado[1]
                #print(linha,coluna)
                if linha == -9 and coluna == -9:
                    print("O %s mandou o trevo para a table" % nome)
                    table.append(trevo)
                    key = False
                    taboleiroj[4][0] = 0
                    screen.blit(imagem_fundo, (0, 0))
                    pygame.display.flip()
                    pygame.display.update()
                elif taboleiroj[linha][coluna] == 0:
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
            break

    guardar_na_mem(nome, taboleiroj, excluidos, table, jogador) #vai alterar na memoria os valores do taboleiro pelos atuais
def turnob(screen, taboleirob, excluidos,totaltrevos, key_inicial, table, jogador):#funcao destinada ao turno do bot
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
            else:
                tela.fill(ColorBack["azul"])
            """
            if Botao2.touche == True:
                tela.fill(ColorBack["azul"])
                tela2()


            if Botao3.touche == True:
                tela.fill(ColorBack["azul"])
                tela3()


            if Botao4.touche == True:
                tela.fill(ColorBack["azul"])
                tela4()
            """


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
    Botao19 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx1_1, posy=posy1_1)
    Botao19.rect.center = (posx1_1, posy1_1)
    Botao20 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx2_1, posy=posy2_1)
    Botao20.rect.center = (posx2_1, posy2_1)
    Botao21 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx3_1, posy=posy3_1)
    Botao21.rect.center = (posx3_1, posy3_1)
    Botao22 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx4_1, posy=posy4_1)
    Botao22.rect.center = (posx4_1, posy4_1)
    Botao23 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx5_1, posy=posy5_1)
    Botao23.rect.center = (posx5_1, posy5_1)
    Botao24 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx6_1, posy=posy6_1)
    Botao24.rect.center = (posx6_1, posy6_1)
    Botao25 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx7_1, posy=posy7_1)
    Botao25.rect.center = (posx7_1, posy7_1)
    Botao26 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx8_1, posy=posy8_1)
    Botao26.rect.center = (posx8_1, posy8_1)
    Botao27 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                   image2="imagens_gerais/red_button02.png", posx=posx9_1, posy=posy9_1)
    Botao27.rect.center = (posx9_1, posy9_1)
    Botao28 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx10_1, posy=posy1_1)
    Botao28.rect.center = (posx10_1, posy10_1)
    Botao29 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx11_1, posy=posy11_1)
    Botao29.rect.center = (posx11_1, posy11_1)
    Botao30 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx12_1, posy=posy12_1)
    Botao30.rect.center = (posx12_1, posy12_1)
    Botao31 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx13_1, posy=posy13_1)
    Botao31.rect.center = (posx13_1, posy13_1)
    Botao32 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx14_1, posy=posy14_1)
    Botao32.rect.center = (posx14_1, posy14_1)
    Botao33 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx15_1, posy=posy15_1)
    Botao33.rect.center = (posx15_1, posy15_1)
    Botao34 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=posx16_1, posy=posy16_1)
    Botao34.rect.center = (posx16_1, posy16_1)



    Botao17 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=110, posy=88, dim=44)
    Botao17.rect.center = (110, 88)
    Botao18 = Botao(ButtonGrups, image="imagens_gerais/red_button01.png", image1="imagens_gerais/red_button01.png",
                    image2="imagens_gerais/red_button02.png", posx=495, posy=87, dim=44)
    Botao18.rect.center = (495, 87)

    #joana = pygame.image.load("imagens_jogo/joaninha.png").convert_alpha()



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

    Cond_final = [J_prenchido, B_preenhido]

    if numero == 0:
        print("Bot começa!")
        while (not Cond_final[1] and not Cond_final[0]) and not (len(trevos) == 40):  # as condicoes de fim do jogo sao alguem ja ter preenchido to do o taboleiro ou os trevos esgotarem-se
            #aaa(imagem1_verde_exibida, imagem1_fundo, imagem17_fundo, imagem17_verde_exibida, Botao1, Botao17, screen, posx1, posy1, cor_de_fundo, imagem_fundo, ButtonGrups)
            #joaninha(joana,screen,"jog2")
            turnob(screen, taboleiroB, trevos, 20, Comeco, table, nome)
            exibir_taboleiro(Cond_final, taboleiroB, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                             posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                             posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                             posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1, Bot=1)
            #joaninha(joana, screen)
            turnoj(Cond_final, imagem_fundo,screen, nome, taboleiroJ, trevos, 20, Comeco, table, "BOT", ButtonGrups,
                                      Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,
                                      Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17,Botao18,posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                      posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                      posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                      posy14, posy15, posy16, posy17=88, posx17=110)
            exibir_taboleiro(Cond_final, taboleiroJ, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                      posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                      posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                      posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1)
            # print(table)
            """a = int(input("cheat: "))
            if a == 0:
                B_preenhido = True
                J_prenchido = True
                """
        # print(trevos)
    else:
        print("O %s começa!" % nome)
        while (not Cond_final[1] and not Cond_final[0]) and not (len(trevos) == 40):
            #aaa(imagem1_verde_exibida, imagem1_fundo, imagem17_fundo, imagem17_verde_exibida, Botao1, Botao17, screen, posx1, posy1, cor_de_fundo, imagem_fundo, ButtonGrups)
            #joaninha(joana, screen)
            turnoj(Cond_final, imagem_fundo,screen, nome, taboleiroJ, trevos, 40, Comeco, table, "BOT", ButtonGrups,
                                      Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,
                                      Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17,Botao18, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                      posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                      posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                      posy14, posy15, posy16, posy17=88, posx17=110)
            exibir_taboleiro(Cond_final, taboleiroJ, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                      posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                      posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                      posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1)
            #joaninha(joana, screen, "jog2")
            turnob(screen, taboleiroB, trevos, 40, Comeco, table, nome)
            exibir_taboleiro(Cond_final, taboleiroB, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                             posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                             posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                             posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1, Bot=1)

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
def escolha_posicao_trevo(ButtonGrups,screen, Botao1,Botao2,Botao3,Botao4,Botao5,Botao6,Botao7,Botao8,Botao9,Botao10,Botao11,Botao12,Botao13,Botao14,Botao15,Botao16,Botao17,Botao18, posx1, posx2, posx3, posx4, posx5, posx6, posx7,posx8,posx9,posx10,posx11,posx12,posx13,posx14,posx15,posx16,posy1, posy2, posy3, posy4, posy5, posy6, posy7,posy8,posy9,posy10,posy11,posy12,posy13,posy14,posy15,posy16, posy17, posx17):
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            ButtonGrups.update()

        if Botao1.touche == True:

            print("IMAGEM1")
            Botao1.touche = False
            return [0,0]

        if Botao2.touche == True:

            print("IMAGEM2")
            Botao2.touche = False
            return [0, 1]

        if Botao3.touche == True:

            print("IMAGEM3")
            Botao3.touche = False
            return [0, 2]

        if Botao4.touche == True:

            print("IMAGEM4")
            Botao4.touche = False
            return [0, 3]

        if Botao5.touche == True:

            print("IMAGEM5")
            Botao5.touche = False
            return [1,0]

        if Botao6.touche == True:

            print("IMAGEM6")
            Botao6.touche = False
            return [1,1]

        if Botao7.touche == True:

            print("IMAGEM7")
            Botao7.touche = False
            return [1, 2]

        if Botao8.touche == True:

            print("IMAGEM8")
            Botao8.touche = False
            return [1,3]

        if Botao9.touche == True:

            print("IMAGEM9")
            Botao9.touche = False
            return [2,0]

        if Botao10.touche == True:

            print("IMAGEM10")
            Botao10.touche = False
            return [2,1]

        if Botao11.touche == True:

            print("IMAGEM11")
            Botao11.touche = False
            return [2,2]

        if Botao12.touche == True:

            print("IMAGEM12")
            Botao12.touche = False
            return [2,3]

        if Botao13.touche == True:

            print("IMAGEM13")
            Botao13.touche = False
            return [3,0]

        if Botao14.touche == True:

            print("IMAGEM14")
            Botao14.touche = False
            return [3, 1]

        if Botao15.touche == True:

            print("IMAGEM15")
            Botao15.touche = False
            return [3,2]

        if Botao16.touche == True:

            print("IMAGEM16")
            Botao16.touche = False
            return [3,3]
        if Botao18.touche == True:

            print("TABLE")
            Botao18.touche = False
            return [-9, -9]

        pygame.display.flip()
        pygame.display.update()

main_menu()