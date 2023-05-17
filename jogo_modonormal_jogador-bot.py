import copy
import time


from config_jog1 import *
from config_jog2 import *
import pygame
import pygame_gui
import sys
import random
import os

def player_nome(nome_player1,nome_player2, screen):
    player1 = message_to_screen(nome_player1, None, 25, [0, 100, 0])
    screen.blit(player1, (1075 - player1.get_width() // 2, 116 - player1.get_height() // 2))

    if nome_player2 == "BOT":
        player2 = message_to_screen("BOT", None, 25, [255, 0, 0])
        screen.blit(player2, (1050 - player2.get_width() // 2, 205 - player2.get_height() // 2))
    else:
        player2 = message_to_screen(nome_player2, None, 25, [255, 0, 0])
        screen.blit(player2, (1075 - player2.get_width() // 2, 205 - player2.get_height() // 2))
def remover_message_to_screen(retangulo1, screen):
    retangulo = pygame.transform.scale(retangulo1, (818, 29))
    screen.blit(retangulo, (91, 136))
def message_to_screen(message, textfont, size, color):
    my_font = pygame.font.Font(textfont, size)
    my_message = my_font.render(message, True, color)
    return my_message
def retangulo_joaninha_remove(retangulo, screen, jog="jog1"):
    retangulo = pygame.transform.scale(retangulo, (35, 33))
    if jog == "jog1":
        screen.blit(retangulo, (433, 169))
    else:
        screen.blit(retangulo, (870, 169))
def joaninha(joana, screen, jog="jog1"):
    joana = pygame.transform.scale(joana, (35, 35))
    if jog=="jog1":
        screen.blit(joana, (433, 168))
    else:
        screen.blit(joana, (870, 168))
def initial_write_to_mem(name_player, player_board, excluidos, table, name_player2 = "BOT"):
    with open("save.txt", "w") as f:
        f.write(name_player +"/"+ str(player_board))
        f.write("\n")
        f.write(name_player2 + "/" + str(player_board))
        f.write("\n")
        f.write("excluidos/" + str(excluidos))
        f.write("\n")
        f.write("table/" + str(table))
    f.close()
def guardar_na_mem(name, tabuleiro_player, excluidos, table, jogador, proxima=-1):
    dicionario = {}
    with open("save.txt", "r") as f:
        linhas = f.readlines()
    i = 0
    for linha in linhas:
        nome, tabuleiro_str = linha.strip().split("/")
        if i == 0:
            dicionario["jogador1"] = nome
            i += 1
        elif i == 1:
            dicionario["jogador2"] = nome
            i += 1

        tabuleiro = eval(tabuleiro_str)
        dicionario[nome] = tabuleiro

    f.close()

    for x in dicionario.keys():
        if x == name:
            dicionario[x] = tabuleiro_player

    dicionario["excluidos"] = excluidos

    dicionario["table"] = table

    dicionario["jogador"] = [jogador]
    dicionario["proxima"] = [proxima]

    dicionario.pop("jogador1")
    dicionario.pop("jogador2")
    with open("save.txt", "w") as f:
        for y in dicionario.keys():
            f.write(y + "/" + str(dicionario[y]) + "\n")

    f.close()

    # print(dicionario)

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
    #aVnE = False  # algum valor nos excluidos
    trevo = []

    for i in range(4):  # gerar 4 valores de 1 até totaltrevos
        key1 = True  # key1 é verdade que vai ser usada para a geracao de um trevo
        while key1:  # enquanto for verdade
            t = random.randint(1, totaltrevos)  # gera-se um trevo
            if t not in excluidos:  # se ele nao estiver na lista, ou seja, se ele ainda nao foi usado desta vez e se nao foi usado no programa (lista excluidos)
                key1 = False  # o loop while vai parar
                trevo.append(t)  # adiciona-se o trevo á lista
                excluidos.append(t)  # e adiciona-se o trevo á lista dos excluidos

    trevo_final = [] #trevo usado para resultado do "tratamento de dados" dos trevos
    n_vezes = {} #dicionario com o x numero a 1 ou 0, inicialmente tudo a 1

    for i in range(len(excluidos)):
        if excluidos[i] in trevo:
            n_vezes[excluidos[i]] = 1 #inicia com todos os trevos no dicionario a 1, pois quer dizer que ainda nao foram usados
        else:
            n_vezes[excluidos[i]] = 0

    for i in range(len(trevo)):
        if trevo[i] > 20:       #se for superior a 20, trata o valor e reduz 20 a esse numero adicionando-o no trevo_final
            trevo_final.append(trevo[i] - 20)
        else:
            trevo_final.append(trevo[i])    #se for <= 20, adiciona-o a trevo_final sem tratar o numero

    trevo_final.sort() #organiza os numeros por ordem crescente

    for i in range(len(trevo_final)):   #para todos os elementos de trevo_final (so com valores <= 20)
        if (trevo_final[i] not in n_vezes) or (n_vezes[trevo_final[i]] == 0):  #se o elemento do vetor existir no dicionario e o seu valor == 0, quer dizer que ja foi percorrido um elemento antes dele com o mesmo valor, isto acontece pois existem 2 numeros de cada pois existem 2 cores
            trevo_final[i] += 20    #entao retornamos um deles ao seu valor original, nao vai afetar o taboleiro, pois o valor real vai continuar a ser (x - 20)
            taboleiro[i][i] = trevo_final[i]  # altera os valores no taboleiro consoante os que foram gerados, organizados
        else:
            n_vezes[trevo_final[i]] = 0 #se ainda estiver a 1, quer dizer que +e o primeiro que aparece, ou seja, poem a 0
            taboleiro[i][i] = trevo_final[i]  # altera os valores no taboleiro consoante os que foram gerados, organizados



    print(trevo_final)
    return False    #retorna falso para dizer que ja fez a primeira jogada
def turnoj(cond_final, imagem_fundo, screen,nome, taboleiroj, excluidos, totaltrevos, key_inicial, table, jogador, ButtonGrups, Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17,Botao18, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,posy14, posy15, posy16, posy17=88, posx17=110):#funcao destinada ao turno do jogador
    print("JOGADOR")
    if key_inicial[1]: #se for a primeira jogada
        key_inicial[1] = primeira_rodada(taboleiroj, excluidos, totaltrevos)
        #exibir_taboleiro(taboleiroj)

    else:
        key = True
        if len(table) == 0: #quando nao existem trevos na table, tem que gerar um novo
            baralho = message_to_screen(nome + ", escolhe uma posiçao para colocar o trevo", None, 25,[0, 0, 0])
            screen.blit(baralho, (500 - baralho.get_width() // 2, 150 - baralho.get_height() // 2))

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
            table_baralho = message_to_screen(nome + ", escolhe um trevo da table ou usa o baralho", None, 25, [0, 0, 0])
            screen.blit(table_baralho,(500 - table_baralho.get_width() // 2, 148 - table_baralho.get_height() // 2))
            pygame.display.flip()
            pygame.display.update()

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
                    retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
                    remover_message_to_screen(retangulo1, screen)
                    baralho = message_to_screen(nome + ", escolhe uma posiçao para colocar o trevo", None, 25,
                                                [0, 0, 0])
                    screen.blit(baralho, (500 - baralho.get_width() // 2, 148 - baralho.get_height() // 2))
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
                        pygame.display.flip() # aparece o trevo na parte de baixo do taboleiro
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
            retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
            remover_message_to_screen(retangulo1, screen)

            break

    guardar_na_mem(nome, taboleiroj, excluidos, table, jogador) #vai alterar na memoria os valores do taboleiro pelos atuais
def turnob(screen, taboleirob, excluidos,totaltrevos, key_inicial, table, jogador):#funcao destinada ao turno do bot
    if key_inicial[0]:#se for a primeira jogada
        print("BOT")
        key_inicial[0] = primeira_rodada(taboleirob, excluidos, totaltrevos)

        for i in range(4):
            print(str(taboleirob[i][0]), " | ", str(taboleirob[i][1]), " | ", str(taboleirob[i][2]), " | ", str(taboleirob[i][3]))
        print("\n")
        pygame.display.flip()
        pygame.display.update()


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

        pygame.display.flip()
        pygame.display.update()
        #time.sleep(1)

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
                #novo_jogo_normal()
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
def novo_jogo_normal(nome):
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

    cores_jogadores = {"Player1":[0, 255, 127], "Player2":[255, 0, 0]}
    retangulo = pygame.image.load("imagens_jogo/retangulo.png").convert_alpha()

    #jogo abaixo
    B_preenhido = False  # o bot ja preencheu o taboleiro?
    J_prenchido = False  # o jogador ja preencheu o taboleiro?
    trevos = []  # todos os trevos vao parar aqui para que nao haja repeticao na geracao de trevos
    taboleiroJ = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0]]  # taboleiro do jogador
    taboleiroB = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0]]  # taboleiro do bot
    table = []
    joana = pygame.image.load("imagens_jogo/joaninha.png").convert_alpha()
    initial_write_to_mem(nome, taboleiroJ, trevos,table)  # guarda os taboleiros na mem com os nomes do bot e do jogador

    numero = 0#random.randint(0, 1)  # quem comeca
    Comeco = [True, True]

    Cond_final = [J_prenchido, B_preenhido]

    if numero == 0:
        print("Bot começa!")

        while (not Cond_final[1] and not Cond_final[0]) and not (len(trevos) == 40):  # as condicoes de fim do jogo sao alguem ja ter preenchido to do o taboleiro ou os trevos esgotarem-se
            #aaa(imagem1_verde_exibida, imagem1_fundo, imagem17_fundo, imagem17_verde_exibida, Botao1, Botao17, screen, posx1, posy1, cor_de_fundo, imagem_fundo, ButtonGrups)
            player_nome(nome,"Antonio",screen)
            joaninha(joana,screen,"jog2")
            turnob(screen, taboleiroB, trevos, 40, Comeco, table, nome)
            exibir_taboleiro(Cond_final, taboleiroB, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                             posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                             posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                             posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1, Bot=1)
            retangulo_joaninha_remove(retangulo, screen, "jog2")
            joaninha(joana, screen)
            player_nome(nome,"Antonio",screen)
            turnoj(Cond_final, imagem_fundo,screen, nome, taboleiroJ, trevos, 40, Comeco, table, "BOT", ButtonGrups,
                                      Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,
                                      Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17,Botao18,posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                      posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                      posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                      posy14, posy15, posy16, posy17=88, posx17=110)

            exibir_taboleiro(Cond_final, taboleiroJ, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                      posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                      posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                                      posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1)
            retangulo_joaninha_remove(retangulo, screen)
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
            joaninha(joana, screen)
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
            retangulo_joaninha_remove(retangulo, screen)
            #time.sleep(5)
            joaninha(joana, screen, "jog2")
            turnob(screen, taboleiroB, trevos, 40, Comeco, table, nome)
            exibir_taboleiro(Cond_final, taboleiroB, screen, posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                             posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                             posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12, posy13,
                             posy14, posy15, posy16, posx1_1, posx2_1, posx3_1, posx4_1, posx5_1, posx6_1, posx7_1, posx8_1, posx9_1,posx10_1, posx11_1, posx12_1, posx13_1, posx14_1, posx15_1, posx16_1, posy1_1, posy2_1,posy3_1, posy4_1, posy5_1, posy6_1, posy7_1, posy8_1, posy9_1, posy10_1, posy11_1, posy12_1, posy13_1,posy14_1, posy15_1, posy16_1, Bot=1)
            retangulo_joaninha_remove(retangulo, screen, "jog2")
            time.sleep(2)
            # print(table)
            """a = int(input("cheat: "))
            if a == 0:
                B_preenhido = True
                J_prenchido = True"""
        # print(trevos)
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


novo_jogo_normal("Filipe Pinto")