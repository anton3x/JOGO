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
    player1 = message_to_screen(nome_player1, None, 25, [0, 255, 127])
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

    #print(dicionario)
def exibir_taboleiro(cond_final, taboleiro,screen, Jog2=0):
    for i in range(4):
        print(str(taboleiro[i][0]), " | ", str(taboleiro[i][1]), " | ", str(taboleiro[i][2]), " | ", str(taboleiro[i][3]))
    print("\n")

    n_botao = 0
    contador = 0

    if Jog2 != 1:
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
            if lista_coluna[i] >= lista_coluna[i + 1]:
                return False
        else:
            continue
    for i in range(len(lista_linha)):
        if not (i == (len(lista_linha) - 1)):
            if lista_linha[i] >= lista_linha[i + 1]:
                return False
        else:
            continue

    return True
def turnoj(proxima, cond_final, imagem_fundo, screen,nome_jogador1, taboleiroj, excluidos, totaltrevos, key_inicial, table, nome_jogador2, ButtonGrups, posy17=88, posx17=110):#funcao destinada ao turno do jogador
        print("JOGADOR")

        key = True
        if proxima == -1:
            if len(table) == 0: #quando nao existem trevos na table, tem que gerar um novo
                baralho = message_to_screen(nome_jogador1 + ", escolhe uma posiçao para colocar o trevo", None, 25,[0, 0, 0])
                screen.blit(baralho, (500 - baralho.get_width() // 2, 150 - baralho.get_height() // 2))

                while key:
                    trevo = random.randint(1, totaltrevos)
                    if trevo not in excluidos:
                        key = False
                        excluidos.append(trevo)
                taboleiroj[4][0] = trevo #trevo escolhido para a parte debaixo do taboleiro
                exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                pygame.display.flip()
                pygame.display.update()

                guardar_na_mem(nome_jogador1, taboleiroj, excluidos, table,nome_jogador1, proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais
            else:   #se ja existirem trevos na table, pode usar um do baralho ou usar um da table
                print(table)
                key1 = True
                table_baralho = message_to_screen(nome_jogador1 + ", escolhe um trevo da table ou usa o baralho", None, 25, [0, 0, 0])
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
                            exibir_taboleiro(cond_final, taboleiroj, screen, Jog2=0)
                            pygame.display.flip()
                            pygame.display.update()
                            break
                        else:   #se só existir 1, tem que ser o que está lá
                            Botao18.touche = False
                            trevo = table[0]
                            table.remove(trevo)
                            taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                            exibir_taboleiro(cond_final, taboleiroj, screen, Jog2=0)
                            pygame.display.flip()
                            pygame.display.update()

                        # exibe a imagem 1 verde
                        # imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
                        # screen.blit(imagem1_fundo, (posx1 - 36, posy1 - 36))
                        break
                    if Botao17.touche == True:  #se ele pressionou o baralho
                        retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
                        remover_message_to_screen(retangulo1, screen)
                        baralho = message_to_screen(nome_jogador1 + ", escolhe uma posiçao para colocar o trevo", None, 25,
                                                    [0, 0, 0])
                        screen.blit(baralho, (500 - baralho.get_width() // 2, 148 - baralho.get_height() // 2))
                        key = True
                        while key:
                            trevo = random.randint(1, totaltrevos)
                            if trevo not in excluidos:
                                key = False
                                excluidos.append(trevo)
                        taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                        exibir_taboleiro(cond_final, taboleiroj, screen, Jog2=0)
                        pygame.display.flip()
                        pygame.display.update()

                        Botao17.touche = False
                        break


                guardar_na_mem(nome_jogador1, taboleiroj, excluidos, table,nome_jogador1, proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais

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
                        exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                        Botao18.touche = False
                        pygame.display.flip()
                        pygame.display.update()
                        break
                    else:
                        #taboleiroj[4][0] = trevo #trevo escolhido para a parte debaixo do taboleiro
                        exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                        pygame.display.flip()
                        pygame.display.update()
                        key1 = True
                        while key1:
                            print("Posicao: ")

                            resultado = escolha_posicao_trevo(ButtonGrups, "Jogador1")
                            linha = resultado[0]
                            coluna = resultado[1]
                            #print(linha,coluna)
                            if linha == -9 and coluna == -9:
                                print("O %s mandou o trevo para a table" % nome_jogador2)
                                table.append(trevo)
                                key = False
                                key1 = False
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
                                    key1 = False
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
                                    key1 = False
                                    taboleiroj[4][0] = 0
                                    screen.blit(imagem_fundo, (0, 0))
                                    pygame.display.flip()
                                    pygame.display.update()
                        retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
                        remover_message_to_screen(retangulo1, screen)

                        break
        else:
            if len(table) == 0 and proxima != 1:  # quando nao existem trevos na table, tem que gerar um novo
                baralho = message_to_screen(nome_jogador1 + ", escolhe uma posiçao para colocar o trevo", None, 25, [0, 0, 0])
                screen.blit(baralho, (500 - baralho.get_width() // 2, 150 - baralho.get_height() // 2))

                while key:
                    trevo = random.randint(1, totaltrevos)
                    if trevo not in excluidos:
                        key = False
                        excluidos.append(trevo)
                taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                pygame.display.flip()
                pygame.display.update()

                guardar_na_mem(nome_jogador1, taboleiroj, excluidos, table,nome_jogador1, proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais
            else:  # se ja existirem trevos na table, pode usar um do baralho ou usar um da table
                if proxima != 1:
                    print(table)
                    key1 = True
                    table_baralho = message_to_screen(nome_jogador1 + ", escolhe um trevo da table ou usa o baralho", None, 25,
                                                      [0, 0, 0])
                    screen.blit(table_baralho,
                                (500 - table_baralho.get_width() // 2, 148 - table_baralho.get_height() // 2))
                    pygame.display.flip()
                    pygame.display.update()

                    while key1:
                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            ButtonGrups.update()
                        if Botao18.touche == True:  # pressionou a table
                            print("TABLE TOCADA")

                            if len(table) != 1:  # se existirem mais que um elementos na table, tem que escolher qual quer
                                Botao18.touche = False
                                print("Table - ", table)
                                linha = int(input("Qual trevo queres da table(0-n): "))
                                trevo = table[linha]
                                table.remove(trevo)
                                taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                                exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                                pygame.display.flip()
                                pygame.display.update()
                                break
                            else:  # se só existir 1, tem que ser o que está lá
                                Botao18.touche = False
                                trevo = table[0]
                                table.remove(trevo)
                                taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                                exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                                pygame.display.flip()
                                pygame.display.update()

                            # exibe a imagem 1 verde
                            # imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
                            # screen.blit(imagem1_fundo, (posx1 - 36, posy1 - 36))
                            break
                        if Botao17.touche == True:  # se ele pressionou o baralho
                            retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
                            remover_message_to_screen(retangulo1, screen)
                            baralho = message_to_screen(nome_jogador1 + ", escolhe uma posiçao para colocar o trevo", None, 25,
                                                        [0, 0, 0])
                            screen.blit(baralho, (500 - baralho.get_width() // 2, 148 - baralho.get_height() // 2))
                            key = True
                            while key:
                                trevo = random.randint(1, totaltrevos)
                                if trevo not in excluidos:
                                    key = False
                                    excluidos.append(trevo)
                            taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                            exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                            pygame.display.flip()
                            pygame.display.update()

                            Botao17.touche = False
                            break

                    guardar_na_mem(nome_jogador1, taboleiroj, excluidos, table,nome_jogador1, proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais

            print("Trevo - ", taboleiroj[4][0])
            key = True
                    # imagem17_fundo = pygame.transform.scale(imagem17_fundo, (73, 73))
                    # screen.blit(imagem17_fundo, (281 - 36, 615 - 36))
                    # exibir_taboleiro(taboleiroj, screen)
                    # pygame.display.flip()
                    # exibir_taboleiro(taboleiroj)

            if proxima == 1:
                    while key:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            ButtonGrups.update()
                        if Botao18.touche == True and proxima == 3:
                            print("TABLE TOCADA")
                            table.append(trevo)
                            key = False
                            print("\nO trevo %d foi colocado na table\n" % trevo)
                            taboleiroj[4][0] = 0
                            screen.blit(imagem_fundo, (0, 0))
                            exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                            Botao18.touche = False
                            pygame.display.flip()
                            pygame.display.update()
                            break
                        else:
                            # taboleiroj[4][0] = trevo #trevo escolhido para a parte debaixo do taboleiro
                            exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                            pygame.display.flip()
                            pygame.display.update()
                            key1 = True
                            while key1:

                                print("Posicao: ")

                                resultado = escolha_posicao_trevo(ButtonGrups, "Jogador1")
                                linha = resultado[0]
                                coluna = resultado[1]
                                # print(linha,coluna)
                                if linha == -9 and coluna == -9:
                                    print("O %s mandou o trevo para a table" % nome_jogador1)
                                    table.append(taboleiroj[4][0])
                                    key = False
                                    key1 = False
                                    taboleiroj[4][0] = 0
                                    screen.blit(imagem_fundo, (0, 0))
                                    pygame.display.flip()
                                    pygame.display.update()
                                elif taboleiroj[linha][coluna] == 0:
                                    # print("verificar")
                                    if verificar_taboleiro(taboleiroj, linha, coluna, taboleiroj[4][0]):
                                        # print("feito")
                                        print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (taboleiroj[4][0], linha, coluna))
                                        taboleiroj[linha][coluna] = taboleiroj[4][0]
                                        key = False
                                        key1 = False
                                        taboleiroj[4][0] = 0
                                        screen.blit(imagem_fundo, (0, 0))
                                        pygame.display.flip()  # aparece o trevo na parte de baixo do taboleiro
                                        pygame.display.update()

                                else:
                                    # print("verificar")
                                    if verificar_taboleiro(taboleiroj, linha, coluna, taboleiroj[4][0]):
                                        # print("feito")
                                        print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (taboleiroj[4][0], linha, coluna))
                                        print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (taboleiroj[linha][coluna], taboleiroj[4][0]))
                                        table.append(taboleiroj[linha][coluna])
                                        taboleiroj[linha][coluna] = taboleiroj[4][0]
                                        key = False
                                        key1 = False
                                        taboleiroj[4][0] = 0
                                        screen.blit(imagem_fundo, (0, 0))
                                        pygame.display.flip()
                                        pygame.display.update()
                            retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
                            remover_message_to_screen(retangulo1, screen)

                            break

        guardar_na_mem(nome_jogador1, taboleiroj, excluidos, table, nome_jogador2, proxima=-1) #vai alterar na memoria os valores do taboleiro pelos atuais
def turnoj2(proxima, cond_final, imagem_fundo, screen, nome_jogador2, taboleiroj2, excluidos, totaltrevos, key_inicial, table,nome_jogador1, ButtonGrups, posy17=88,posx17=110):  # funcao destinada ao turno do jogador
    print("JOGADOR2")

    key = True
    if proxima == -1:
        if len(table) == 0:  # quando nao existem trevos na table, tem que gerar um novo
            baralho = message_to_screen(nome_jogador2 + ", escolhe uma posiçao para colocar o trevo", None, 25, [0, 0, 0])
            screen.blit(baralho, (500 - baralho.get_width() // 2, 150 - baralho.get_height() // 2))

            while key:
                trevo = random.randint(1, totaltrevos)
                if trevo not in excluidos:
                    key = False
                    excluidos.append(trevo)
            taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
            exibir_taboleiro(cond_final, taboleiroj2, screen, Jog2=1)

            pygame.display.flip()
            pygame.display.update()

            guardar_na_mem(nome_jogador2, taboleiroj2, excluidos, table, nome_jogador2,proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais
        else:  # se ja existirem trevos na table, pode usar um do baralho ou usar um da table
            print(table)
            key1 = True
            table_baralho = message_to_screen(nome_jogador2 + ", escolhe um trevo da table ou usa o baralho", None, 25,
                                              [0, 0, 0])
            screen.blit(table_baralho, (500 - table_baralho.get_width() // 2, 148 - table_baralho.get_height() // 2))
            pygame.display.flip()
            pygame.display.update()

            while key1:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    ButtonGrups.update()
                if Botao18.touche == True:  # pressionou a table
                    print("TABLE TOCADA")

                    if len(table) != 1:  # se existirem mais que um elementos na table, tem que escolher qual quer
                        Botao18.touche = False
                        print("Table - ", table)
                        linha = int(input("Qual trevo queres da table(0-n): "))
                        trevo = table[linha]
                        table.remove(trevo)
                        taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                        exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                        pygame.display.flip()
                        pygame.display.update()
                        break
                    else:  # se só existir 1, tem que ser o que está lá
                        Botao18.touche = False
                        trevo = table[0]
                        table.remove(trevo)
                        taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                        exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                        pygame.display.flip()
                        pygame.display.update()

                    # exibe a imagem 1 verde
                    # imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
                    # screen.blit(imagem1_fundo, (posx1 - 36, posy1 - 36))
                    break
                if Botao17.touche == True:  # se ele pressionou o baralho
                    retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
                    remover_message_to_screen(retangulo1, screen)
                    baralho = message_to_screen(nome_jogador2 + ", escolhe uma posiçao para colocar o trevo", None, 25,
                                                [0, 0, 0])
                    screen.blit(baralho, (500 - baralho.get_width() // 2, 148 - baralho.get_height() // 2))
                    key = True
                    while key:
                        trevo = random.randint(1, totaltrevos)
                        if trevo not in excluidos:
                            key = False
                            excluidos.append(trevo)
                    taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                    exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                    pygame.display.flip()
                    pygame.display.update()

                    Botao17.touche = False
                    break

            guardar_na_mem(nome_jogador2, taboleiroj2, excluidos, table, nome_jogador2,
                           proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais

        print("Trevo - ", trevo)
        key = True
        # imagem17_fundo = pygame.transform.scale(imagem17_fundo, (73, 73))
        # screen.blit(imagem17_fundo, (281 - 36, 615 - 36))
        # exibir_taboleiro(taboleiroj, screen)
        # pygame.display.flip()
        # exibir_taboleiro(taboleiroj)

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
                taboleiroj2[4][0] = 0
                screen.blit(imagem_fundo, (0, 0))
                exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                Botao18.touche = False
                pygame.display.flip()
                pygame.display.update()
                break
            else:
                # taboleiroj[4][0] = trevo #trevo escolhido para a parte debaixo do taboleiro
                exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                pygame.display.flip()
                pygame.display.update()
                key1 = True
                while key1:
                    print("Posicao: ")

                    resultado = escolha_posicao_trevo(ButtonGrups,"Jogador2")
                    linha = resultado[0]
                    coluna = resultado[1]
                    # print(linha,coluna)
                    if linha == -9 and coluna == -9:
                        print("O %s mandou o trevo para a table" % nome_jogador2)
                        table.append(trevo)
                        key = False
                        key1 = False
                        taboleiroj2[4][0] = 0
                        screen.blit(imagem_fundo, (0, 0))
                        pygame.display.flip()
                        pygame.display.update()
                    elif taboleiroj2[linha][coluna] == 0:
                        # print("verificar")
                        if verificar_taboleiro(taboleiroj2, linha, coluna, trevo):
                            # print("feito")
                            print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (trevo, linha, coluna))
                            taboleiroj2[linha][coluna] = trevo
                            key = False
                            key1 = False
                            taboleiroj2[4][0] = 0
                            screen.blit(imagem_fundo, (0, 0))
                            pygame.display.flip()  # aparece o trevo na parte de baixo do taboleiro
                            pygame.display.update()

                    else:
                        # print("verificar")
                        if verificar_taboleiro(taboleiroj2, linha, coluna, trevo):
                            # print("feito")
                            print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (trevo, linha, coluna))
                            print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (
                            taboleiroj2[linha][coluna], trevo))
                            table.append(taboleiroj2[linha][coluna])
                            taboleiroj2[linha][coluna] = trevo
                            key = False
                            key1 = False
                            taboleiroj2[4][0] = 0
                            screen.blit(imagem_fundo, (0, 0))
                            pygame.display.flip()
                            pygame.display.update()
                retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
                remover_message_to_screen(retangulo1, screen)

                break
    else:
        if len(table) == 0 and proxima != 1:  # quando nao existem trevos na table, tem que gerar um novo
            baralho = message_to_screen(nome_jogador2 + ", escolhe uma posiçao para colocar o trevo", None, 25, [0, 0, 0])
            screen.blit(baralho, (500 - baralho.get_width() // 2, 150 - baralho.get_height() // 2))

            while key:
                trevo = random.randint(1, totaltrevos)
                if trevo not in excluidos:
                    key = False
                    excluidos.append(trevo)
            taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
            exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)

            pygame.display.flip()
            pygame.display.update()

            guardar_na_mem(nome_jogador2, taboleiroj2, excluidos, table, nome_jogador2,
                           proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais
        else:  # se ja existirem trevos na table, pode usar um do baralho ou usar um da table
            if proxima != 1:
                print(table)
                key1 = True
                table_baralho = message_to_screen(nome_jogador2 + ", escolhe um trevo da table ou usa o baralho", None, 25,
                                                  [0, 0, 0])
                screen.blit(table_baralho,
                            (500 - table_baralho.get_width() // 2, 148 - table_baralho.get_height() // 2))
                pygame.display.flip()
                pygame.display.update()

                while key1:
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                        ButtonGrups.update()
                    if Botao18.touche == True:  # pressionou a table
                        print("TABLE TOCADA")

                        if len(table) != 1:  # se existirem mais que um elementos na table, tem que escolher qual quer
                            Botao18.touche = False
                            print("Table - ", table)
                            linha = int(input("Qual trevo queres da table(0-n): "))
                            trevo = table[linha]
                            table.remove(trevo)
                            taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                            exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                            pygame.display.flip()
                            pygame.display.update()
                            break
                        else:  # se só existir 1, tem que ser o que está lá
                            Botao18.touche = False
                            trevo = table[0]
                            table.remove(trevo)
                            taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                            exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                            pygame.display.flip()
                            pygame.display.update()

                        # exibe a imagem 1 verde
                        # imagem1_fundo = pygame.transform.scale(imagem1_fundo, (73, 73))
                        # screen.blit(imagem1_fundo, (posx1 - 36, posy1 - 36))
                        break
                    if Botao17.touche == True:  # se ele pressionou o baralho
                        retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
                        remover_message_to_screen(retangulo1, screen)
                        baralho = message_to_screen(nome_jogador2 + ", escolhe uma posiçao para colocar o trevo", None, 25,
                                                    [0, 0, 0])
                        screen.blit(baralho, (500 - baralho.get_width() // 2, 148 - baralho.get_height() // 2))
                        key = True
                        while key:
                            trevo = random.randint(1, totaltrevos)
                            if trevo not in excluidos:
                                key = False
                                excluidos.append(trevo)
                        taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                        exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                        pygame.display.flip()
                        pygame.display.update()

                        Botao17.touche = False
                        break

                guardar_na_mem(nome_jogador2, taboleiroj2, excluidos, table, nome_jogador2,
                               proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais

        print("Trevo - ", taboleiroj2[4][0])
        key = True
        # imagem17_fundo = pygame.transform.scale(imagem17_fundo, (73, 73))
        # screen.blit(imagem17_fundo, (281 - 36, 615 - 36))
        # exibir_taboleiro(taboleiroj, screen)
        # pygame.display.flip()
        # exibir_taboleiro(taboleiroj)

        if proxima == 1:
            while key:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    ButtonGrups.update()
                if Botao18.touche == True and proxima == 3:
                    print("TABLE TOCADA")
                    table.append(trevo)
                    key = False
                    print("\nO trevo %d foi colocado na table\n" % trevo)
                    taboleiroj2[4][0] = 0
                    screen.blit(imagem_fundo, (0, 0))
                    exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                    Botao18.touche = False
                    pygame.display.flip()
                    pygame.display.update()
                    break
                else:
                    # taboleiroj[4][0] = trevo #trevo escolhido para a parte debaixo do taboleiro
                    exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                    pygame.display.flip()
                    pygame.display.update()
                    key1 = True
                    while key1:

                        print("Posicao: ")

                        resultado = escolha_posicao_trevo(ButtonGrups, "Jogador2")
                        linha = resultado[0]
                        coluna = resultado[1]
                        # print(linha,coluna)
                        if linha == -9 and coluna == -9:
                            print("O %s mandou o trevo para a table" % nome_jogador2)
                            table.append(taboleiroj2[4][0])
                            key = False
                            key1 = False
                            taboleiroj2[4][0] = 0
                            screen.blit(imagem_fundo, (0, 0))
                            pygame.display.flip()
                            pygame.display.update()
                        elif taboleiroj2[linha][coluna] == 0:
                            # print("verificar")
                            if verificar_taboleiro(taboleiroj2, linha, coluna, taboleiroj2[4][0]):
                                # print("feito")
                                print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (
                                taboleiroj2[4][0], linha, coluna))
                                taboleiroj2[linha][coluna] = taboleiroj2[4][0]
                                key = False
                                key1 = False
                                taboleiroj2[4][0] = 0
                                screen.blit(imagem_fundo, (0, 0))
                                pygame.display.flip()  # aparece o trevo na parte de baixo do taboleiro
                                pygame.display.update()

                        else:
                            # print("verificar")
                            if verificar_taboleiro(taboleiroj2, linha, coluna, taboleiroj2[4][0]):
                                # print("feito")
                                print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (
                                taboleiroj2[4][0], linha, coluna))
                                print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (
                                taboleiroj2[linha][coluna], taboleiroj2[4][0]))
                                table.append(taboleiroj2[linha][coluna])
                                taboleiroj2[linha][coluna] = taboleiroj2[4][0]
                                key = False
                                key1 = False
                                taboleiroj2[4][0] = 0
                                screen.blit(imagem_fundo, (0, 0))
                                pygame.display.flip()
                                pygame.display.update()
                    retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
                    remover_message_to_screen(retangulo1, screen)

                    break

    guardar_na_mem(nome_jogador2, taboleiroj2, excluidos, table, nome_jogador1,proxima=-1)  # vai alterar na memoria os valores do taboleiro pelos atuais
def turnob(Cond_final, screen, taboleirob, excluidos,totaltrevos, key_inicial, table, jogador1, jogador2="BOT"):#funcao destinada ao turno do bot
        print(jogador2, ", é a tua vez.")
        key = True

        while key:
            trevo = random.randint(1, totaltrevos)
            if trevo not in excluidos:
                key = False
                excluidos.append(trevo)
        taboleirob[4][0] = trevo
        key1 = True
        exibir_taboleiro(Cond_final, taboleirob, screen,Jog2=1)
        print("Bot retirou do baralho o trevo n: %d " % (trevo))
        time.sleep(1.5)
        while key1:
            linha = random.randint(0, 3)
            coluna = random.randint(0, 3)
            if taboleirob[linha][coluna] == 0:
                if verificar_taboleiro(taboleirob, linha, coluna, trevo):
                    print("O bot colocou o trevo na linha %d e coluna %d\n" % (linha, coluna))
                    taboleirob[linha][coluna] = trevo
                    key1 = False
            else:
                if verificar_taboleiro(taboleirob, linha, coluna, trevo):
                    print("O bot colocou o trevo na linha %d e coluna %d\n" % (linha, coluna))
                    print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (taboleirob[linha][coluna], trevo))
                    table.append(taboleirob[linha][coluna])
                    taboleirob[linha][coluna] = trevo
                    key1 = False

        for i in range(4):
            print(str(taboleirob[i][0]), " | ", str(taboleirob[i][1]), " | ", str(taboleirob[i][2]), " | ",
                  str(taboleirob[i][3]))
        print("\n")

        pygame.display.flip()
        pygame.display.update()
        #time.sleep(1)
        taboleirob[4][0] = 0
        guardar_na_mem(jogador2, taboleirob, excluidos, table, jogador1)
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
def load_jogo_normal():
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

    global Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8, Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16, Botao17, Botao18, Botao19, Botao20, Botao21, Botao22, Botao23, Botao24, Botao25, Botao26, Botao27, Botao28, Botao29, Botao30, Botao31, Botao32, Botao33, Botao34
    global posx1, posy1, posx1_1, posy1_1, posx2, posy2, posx2_1, posy2_1, posx3, posy3, posx3_1, posy3_1, posx4, posy4, posx4_1, posy4_1, posx5, posy5, posx5_1, posy5_1, posx6, posy6, posx6_1, posy6_1, posx7, posy7, posx7_1, posy7_1, posx8, posy8, posx8_1, posy8_1, posx9, posy9, posx9_1, posy9_1, posx10, posy10, posx10_1, posy10_1, posx11, posy11, posx11_1, posy11_1, posx12, posy12, posx12_1, posy12_1, posx13, posy13, posx13_1, posy13_1, posx14, posy14, posx14_1, posy14_1, posx15, posy15, posx15_1, posy15_1, posx16, posy16, posx16_1, posy16_1

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


    nome_jogador1 = dicionario["jogador1"]
    #print(nome_jogador1)
    nome_jogador2 = dicionario["jogador2"]
    #print(nome_jogador2)
    Comeco = [False, False]
    print(dicionario)
    #jogo abaixo
    J2_preenhido = False  # o bot ja preencheu o taboleiro?
    J1_prenchido = False  # o jogador ja preencheu o taboleiro?
    taboleiroJ1 = dicionario[nome_jogador1]  # taboleiro do bot com base na memoria
    taboleiroJ2 = dicionario[nome_jogador2]  # taboleiro do jogador com base na memoria
    prox_jogador = dicionario["jogador"][0]  # proximo jogador a jogar com base na memoria
    trevos = dicionario["excluidos"]  # obter os trevos "excluidos" que ja foram usados
    table = dicionario["table"]  # obter os trevos que estavam na table
    joana = pygame.image.load("imagens_jogo/joaninha.png").convert_alpha()
    proxima_acao = dicionario["proxima"][0]

    Cond_final = [J1_prenchido, J2_preenhido]
    exibir_taboleiro(Cond_final, taboleiroJ2, screen, Jog2=1)
    exibir_taboleiro(Cond_final, taboleiroJ1, screen,Jog2=0)

    if nome_jogador2 == "BOT":
        if prox_jogador == "BOT":
            print("Bot começa!")

            while (not Cond_final[1] and not Cond_final[0]) and not (len(trevos) == 40):  # as condicoes de fim do jogo sao alguem ja ter preenchido to do o taboleiro ou os trevos esgotarem-se
                player_nome(nome_jogador1,nome_jogador2,screen)
                joaninha(joana,screen,"jog2")
                turnob(screen, taboleiroJ2, trevos, 40, Comeco, table, nome_jogador1, nome_jogador2)
                exibir_taboleiro(Cond_final, taboleiroJ2, screen,Jog2=1)
                retangulo_joaninha_remove(retangulo, screen, "jog2")
                joaninha(joana, screen)
                player_nome(nome_jogador1,nome_jogador2,screen)
                turnoj(proxima_acao, Cond_final, imagem_fundo,screen, nome_jogador1, taboleiroJ1, trevos, 40, Comeco, table, nome_jogador2, ButtonGrups)

                exibir_taboleiro(Cond_final, taboleiroJ1, screen)
                retangulo_joaninha_remove(retangulo, screen)
        else:
            print("Player começa!")
            while (not Cond_final[1] and not Cond_final[0]) and not (len(trevos) == 40):  # as condicoes de fim do jogo sao alguem ja ter preenchido to do o taboleiro ou os trevos esgotarem-se
                joaninha(joana, screen)
                player_nome(nome_jogador1, nome_jogador2, screen)
                turnoj(proxima_acao, Cond_final, imagem_fundo, screen, nome_jogador1, taboleiroJ1, trevos, 40, Comeco,table,nome_jogador2, ButtonGrups, posy17=88, posx17=110)
                exibir_taboleiro(Cond_final, taboleiroJ1, screen)
                retangulo_joaninha_remove(retangulo, screen)
                player_nome(nome_jogador1, nome_jogador2, screen)
                proxima_acao = -1
                joaninha(joana, screen, "jog2")
                turnob(Cond_final, screen, taboleiroJ2, trevos, 40, Comeco, table, nome_jogador1, nome_jogador2)
                exibir_taboleiro(Cond_final, taboleiroJ2, screen, Jog2=1)
                retangulo_joaninha_remove(retangulo, screen, "jog2")

    else:

        if prox_jogador == nome_jogador1:
            print("O %s começa!" % nome_jogador1)
            while (not Cond_final[1] and not Cond_final[0]) and not (len(trevos) == 40):
                joaninha(joana, screen, "jog1")
                exibir_taboleiro(Cond_final, taboleiroJ1, screen, Jog2=0)
                turnoj(proxima_acao, Cond_final, imagem_fundo,screen, nome_jogador1, taboleiroJ1, trevos, 40, Comeco, table,nome_jogador2, ButtonGrups, posy17=88, posx17=110)
                exibir_taboleiro(Cond_final, taboleiroJ1, screen, Jog2=0)
                retangulo_joaninha_remove(retangulo, screen)

                joaninha(joana, screen, "jog2")
                exibir_taboleiro(Cond_final, taboleiroJ2, screen, Jog2=1)
                turnoj2(proxima_acao, Cond_final, imagem_fundo, screen, nome_jogador2, taboleiroJ2, trevos, 40, Comeco, table, nome_jogador1, ButtonGrups, posy17=88, posx17=110)
                exibir_taboleiro(Cond_final, taboleiroJ2, screen, Jog2=1)
                retangulo_joaninha_remove(retangulo, screen, "jog2")

        else:
            print("O %s começa!" % nome_jogador2)
            while (not Cond_final[1] and not Cond_final[0]) and not (len(trevos) == 40):
                exibir_taboleiro(Cond_final, taboleiroJ2, screen, Jog2=1)
                joaninha(joana, screen, "jog2")
                turnoj2(proxima_acao, Cond_final, imagem_fundo, screen, nome_jogador2, taboleiroJ2, trevos, 40, Comeco,
                       table, nome_jogador1, ButtonGrups, posy17=88, posx17=110)
                exibir_taboleiro(Cond_final, taboleiroJ2, screen, Jog2=1)
                retangulo_joaninha_remove(retangulo, screen, "jog2")

                joaninha(joana, screen, "jog1")
                exibir_taboleiro(Cond_final, taboleiroJ1, screen, Jog2=0)
                turnoj(proxima_acao, Cond_final, imagem_fundo, screen, nome_jogador1, taboleiroJ1, trevos, 40, Comeco,
                       table, nome_jogador2, ButtonGrups, posy17=88, posx17=110)
                exibir_taboleiro(Cond_final, taboleiroJ1, screen, Jog2=0)
                retangulo_joaninha_remove(retangulo, screen)


def escolha_posicao_trevo(ButtonGrups, vez="Jogador1"):
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            ButtonGrups.update()

        if Botao1.touche == True and vez == "Jogador1":
                print("IMAGEM1")
                Botao1.touche = False
                return [0, 0]

        if Botao2.touche == True and vez == "Jogador1":
                print("IMAGEM2")
                Botao2.touche = False
                return [0, 1]

        if Botao3.touche == True and vez == "Jogador1":
                print("IMAGEM3")
                Botao3.touche = False
                return [0, 2]

        if Botao4.touche == True and vez == "Jogador1":
                print("IMAGEM4")
                Botao4.touche = False
                return [0, 3]

        if Botao5.touche == True and vez == "Jogador1":
                print("IMAGEM5")
                Botao5.touche = False
                return [1, 0]

        if Botao6.touche == True and vez == "Jogador1":
                print("IMAGEM6")
                Botao6.touche = False
                return [1, 1]

        if Botao7.touche == True and vez == "Jogador1":
                print("IMAGEM7")
                Botao7.touche = False
                return [1, 2]

        if Botao8.touche == True and vez == "Jogador1":
                print("IMAGEM8")
                Botao8.touche = False
                return [1, 3]

        if Botao9.touche == True and vez == "Jogador1":
                print("IMAGEM9")
                Botao9.touche = False
                return [2, 0]

        if Botao10.touche == True and vez == "Jogador1":
                print("IMAGEM10")
                Botao10.touche = False
                return [2, 1]

        if Botao11.touche == True and vez == "Jogador1":
                print("IMAGEM11")
                Botao11.touche = False
                return [2, 2]

        if Botao12.touche == True and vez == "Jogador1":
                print("IMAGEM12")
                Botao12.touche = False
                return [2, 3]

        if Botao13.touche == True and vez == "Jogador1":
                print("IMAGEM13")
                Botao13.touche = False
                return [3, 0]

        if Botao14.touche == True and vez == "Jogador1":
                print("IMAGEM14")
                Botao14.touche = False
                return [3, 1]

        if Botao15.touche == True and vez == "Jogador1":
                print("IMAGEM15")
                Botao15.touche = False
                return [3, 2]

        if Botao16.touche == True and vez == "Jogador1":
                print("IMAGEM16")
                Botao16.touche = False
                return [3, 3]
        if Botao18.touche == True:
            print("TABLE")
            Botao18.touche = False
            return [-9, -9]

        if Botao19.touche == True and vez == "Jogador2":
                print("IMAGEM19")
                Botao19.touche = False
                return [0, 0]
        if Botao20.touche == True and vez == "Jogador2":
                print("IMAGEM20")
                Botao20.touche = False
                return [0, 1]
        if Botao21.touche == True and vez == "Jogador2":
                print("IMAGEM21")
                Botao21.touche = False
                return [0, 2]
        if Botao22.touche == True and vez == "Jogador2":
                print("IMAGEM22")
                Botao22.touche = False
                return [0, 3]
        if Botao23.touche == True and vez == "Jogador2":
                print("IMAGEM23")
                Botao23.touche = False
                return [1, 0]
        if Botao24.touche == True and vez == "Jogador2":
                print("IMAGEM24")
                Botao24.touche = False
                return [1, 1]
        if Botao25.touche == True and vez == "Jogador2":
                print("IMAGEM25")
                Botao25.touche = False
                return [1, 2]
        if Botao26.touche == True and vez == "Jogador2":
                print("IMAGEM26")
                Botao26.touche = False
                return [1, 3]
        if Botao27.touche == True and vez == "Jogador2":
                print("IMAGEM27")
                Botao27.touche = False
                return [2, 0]
        if Botao28.touche == True and vez == "Jogador2":
                print("IMAGEM28")
                Botao28.touche = False
                return [2, 1]
        if Botao29.touche == True and vez == "Jogador2":
                print("IMAGEM29")
                Botao29.touche = False
                return [2, 2]
        if Botao30.touche == True and vez == "Jogador2":
                print("IMAGEM30")
                Botao30.touche = False
                return [2, 3]
        if Botao31.touche == True and vez == "Jogador2":
                print("IMAGEM31")
                Botao31.touche = False
                return [3, 0]
        if Botao32.touche == True and vez == "Jogador2":
                print("IMAGEM32")
                Botao32.touche = False
                return [3, 1]
        if Botao33.touche == True and vez == "Jogador2":
                print("IMAGEM33")
                Botao33.touche = False
                return [3, 2]
        if Botao34.touche == True and vez == "Jogador2":
                print("IMAGEM34")
                Botao34.touche = False
                return [3, 3]

        pygame.display.flip()
        pygame.display.update()

load_jogo_normal()