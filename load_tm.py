import copy
import time
from config_jog1 import *
from config_jog2 import *
import pygame
import pygame_gui
import sys
import random
from tela_leadboard import leaderboard

def msg_to_screen_escolha_table_baralho(screen, nome_jogador):
    retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
    remover_message_to_screen(retangulo1, screen)
    table_baralho = message_to_screen(nome_jogador + ", escolhe um trevo da table ou usa o baralho", None, 25,
                                      [0, 0, 0])
    screen.blit(table_baralho, (500 - table_baralho.get_width() // 2, 148 - table_baralho.get_height() // 2))
def msg_to_screen_escolha_posicao(screen, nome_jogador):
    retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
    remover_message_to_screen(retangulo1, screen)
    baralho = message_to_screen(nome_jogador + ", escolhe uma posiçao para colocar o trevo", None, 25,
                                [0, 0, 0])
    screen.blit(baralho, (500 - baralho.get_width() // 2, 148 - baralho.get_height() // 2))
def atualiza_screen(screen, cond_final, table, nome_jogador1, nome_jogador2):
    screen.blit(imagem_fundo, (0, 0))
    exibir_taboleiro(cond_final, taboleiroJ1, screen, Jog2=0)
    exibir_taboleiro(cond_final, taboleiroJ2, screen, Jog2=1)
    esvazia_table(esvaziar, screen, table, ButtonGrups1, botoes)
    gerenciador.draw_ui(screen)
    player_nome(nome_jogador1, nome_jogador2, screen)
    pygame.display.flip()
    pygame.display.update()
    ButtonGrups1.update()
def escolha_posicao_trevo(ButtonGrups,B1,  vez="Jogador1"):

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            ButtonGrups.update()
        if vez=="Jogador1":
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
            B1.empty()
            return [-9, -9]
        if vez == "Jogador2":
            if Botao19.touche == True:

                print("IMAGEM19")
                Botao19.touche = False
                return [0,0]
            if Botao20.touche == True:

                print("IMAGEM20")
                Botao20.touche = False
                return [0,1]
            if Botao21.touche == True:

                print("IMAGEM21")
                Botao21.touche = False
                return [0,2]
            if Botao22.touche == True:

                print("IMAGEM22")
                Botao22.touche = False
                return [0,3]
            if Botao23.touche == True:

                print("IMAGEM23")
                Botao23.touche = False
                return [1,0]
            if Botao24.touche == True:

                print("IMAGEM24")
                Botao24.touche = False
                return [1,1]
            if Botao25.touche == True:

                print("IMAGEM25")
                Botao25.touche = False
                return [1,2]
            if Botao26.touche == True:

                print("IMAGEM26")
                Botao26.touche = False
                return [1,3]
            if Botao27.touche == True:

                print("IMAGEM27")
                Botao27.touche = False
                return [2,0]
            if Botao28.touche == True:

                print("IMAGEM28")
                Botao28.touche = False
                return [2,1]
            if Botao29.touche == True:

                print("IMAGEM29")
                Botao29.touche = False
                return [2,2]
            if Botao30.touche == True:

                print("IMAGEM30")
                Botao30.touche = False
                return [2,3]
            if Botao31.touche == True:

                print("IMAGEM31")
                Botao31.touche = False
                return [3,0]
            if Botao32.touche == True:

                print("IMAGEM32")
                Botao32.touche = False
                return [3,1]
            if Botao33.touche == True:

                print("IMAGEM33")
                Botao33.touche = False
                return [3,2]
            if Botao34.touche == True:

                print("IMAGEM34")
                Botao34.touche = False
                return [3,3]


        pygame.display.flip()
        pygame.display.update()
def jogo(proxima,winner, primeiro_jogador,ultimo_jogador, esvaziar, Cond_final, trevos, screen, table, gerenciador, tempo_delta, nome_jogador1, nome_jogador2, taboleiroJ2, retangulo, Comeco, joana, ButtonGrups, taboleiroJ1, botoes):
    while (not Cond_final[1] and not Cond_final[0]) and not (len(trevos) == 40):  # as condicoes de fim do jogo sao alguem ja ter preenchido to do o taboleiro ou os trevos esgotarem-se
        esvazia_table(esvaziar, screen, table, ButtonGrups1, botoes)
        print(botoes)
        gerenciador.draw_ui(screen)
        gerenciador.update(tempo_delta)

        player_nome(nome_jogador1, nome_jogador2, screen)
        if primeiro_jogador != nome_jogador1:
            joaninha(joana, screen, "jog2")
            if primeiro_jogador == "BOT":
                turnob(Cond_final, screen, taboleiroJ2, trevos, 40, Comeco, table, nome_jogador1, nome_jogador2)
            else:
                turnoj2(proxima,Cond_final, imagem_fundo, screen, nome_jogador2, taboleiroJ2, trevos, 40, Comeco, table, nome_jogador1, ButtonGrups, posy17=88, posx17=110)
            retangulo_joaninha_remove(retangulo, screen, "jog2")
        else:
            turnoj(proxima,Cond_final, imagem_fundo, screen, nome_jogador1, taboleiroJ1, trevos, 40, Comeco, table,nome_jogador2,ButtonGrups)
            joaninha(joana, screen, "jog1")
            retangulo_joaninha_remove(retangulo, screen)

        exibir_taboleiro(Cond_final, taboleiroJ1, screen)
        exibir_taboleiro(Cond_final, taboleiroJ2, screen, Jog2=1)

        if Cond_final[0] == True or Cond_final[1] == True:
            break

        proxima = -1
        ButtonGrups1.empty()
        botoes.clear()
        print(botoes)
        esvazia_table(esvaziar, screen, table, ButtonGrups1, botoes)
        ButtonGrups1.update()
        print(botoes)

        gerenciador.draw_ui(screen)
        player_nome(nome_jogador1, nome_jogador2, screen)


        if ultimo_jogador != nome_jogador1:
            joaninha(joana, screen, "jog2")
            if ultimo_jogador == "BOT":
                turnob(Cond_final, screen, taboleiroJ2, trevos, 40, Comeco, table, nome_jogador1, nome_jogador2)
            else:
                turnoj2(proxima,Cond_final, imagem_fundo, screen, nome_jogador2, taboleiroJ2, trevos, 40, Comeco, table,nome_jogador1, ButtonGrups, posy17=88, posx17=110)
            retangulo_joaninha_remove(retangulo, screen, "jog2")
        else:
            joaninha(joana, screen)
            exibir_taboleiro(Cond_final, taboleiroJ1, screen)
            turnoj(proxima,Cond_final, imagem_fundo, screen, nome_jogador1, taboleiroJ1, trevos, 40, Comeco, table, nome_jogador2,ButtonGrups)
            retangulo_joaninha_remove(retangulo, screen)


        exibir_taboleiro(Cond_final, taboleiroJ1, screen)
        exibir_taboleiro(Cond_final, taboleiroJ2, screen, Jog2=1)

        gerenciador.draw_ui(screen)
        ButtonGrups1.empty()
        esvazia_table(esvaziar, screen, table, ButtonGrups1, botoes)
        ButtonGrups1.update()
        print(botoes)

        pygame.display.flip()

    if Cond_final[1] == True:
        print("Taboleiro J1 preenchido")

        print("fazer uma funcao")
        winner["Jogador1"] += 2
        empty_spaces = 0
        for i in range(4):
            for j in range(4):
               if taboleiroJ2[i][j] == 0:
                   empty_spaces += 1

        winner["Jogador2"] += -1 * empty_spaces

    elif Cond_final[0] == True:
        print("Taboleiro J2 preenchido")

        print("fazer uma funcao")
        winner["Jogador2"] += 2
        empty_spaces = 0
        for i in range(4):
            for j in range(4):
                if taboleiroJ1[i][j] == 0:
                    empty_spaces += 1

        winner["Jogador1"] += -1 * empty_spaces
    else:
        print("baralho sem trevos")
        empty_spaces_j1 = 0
        for i in range(4):
            for j in range(4):
                if taboleiroJ1[i][j] == 0:
                    empty_spaces_j1 += 1

        empty_spaces_j2 = 0
        for i in range(4):
            for j in range(4):
                if taboleiroJ2[i][j] == 0:
                    empty_spaces_j2 += 1

        if empty_spaces_j1 < empty_spaces_j2:
            print("J1 ganhou")
            winner["Jogador1"] +=  2
            winner["Jogador2"] += -1 * empty_spaces_j2

        elif empty_spaces_j1 > empty_spaces_j2:
            print("J2 ganhou")
            winner["Jogador1"] += -1 * empty_spaces_j2
            winner["Jogador2"] += 2
        else:
            winner["Jogador1"] += 2
            winner["Jogador2"] += 2

    Cond_final[0] = False
    Cond_final[1] = False
    Comeco[0] = True
    Comeco[1] = True
def table_exibicao(botoes, table, ButtonGrups):
    ButtonGrups.empty()
    class Botao1(pygame.sprite.Sprite):
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
    # Desenhar cada trevo e associar um botão
    for i in range(len(table)):
        imagem_fundo = "trevos/" + str(table[i]) + ".png"
        x = 480
        y = 62
        dim = 30
        espacamento = 35
        if len(table) > 9:
            if i == 0:
                y = 68
                x = 480
                botao = Botao1(ButtonGrups, image=imagem_fundo,image1=imagem_fundo, image2=imagem_fundo, dim=dim)
                botao.rect.center = (x, y)
                botoes[botao] = table[i]
            elif i % 2 == 0 and i < 16:
                y = 68
                multiplicador = i // 2
                x += multiplicador * espacamento  # Posição x do trevo

            # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo,image1=imagem_fundo, image2=imagem_fundo, dim=dim)
                botao.rect.center = (x, y)
                botoes[botao] = table[i]
            elif i % 2 != 0 and i < 16:
                y = 68
                multiplicador = i // 2 + 1
                x -= multiplicador * espacamento  # Posição x do trevo

                # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo, image1=imagem_fundo, image2=imagem_fundo, dim=dim)

                botao.rect.center = (x, y)
                botoes[botao] = table[i]


            if i % 2 == 0 and i >= 16:
                y = 100
                multiplicador = i // 2 - 8
                x += multiplicador * espacamento  # Posição x do trevo

            # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo,image1=imagem_fundo, image2=imagem_fundo, dim=dim)
                botao.rect.center = (x, y)
                botoes[botao] = table[i]
            elif i % 2 != 0 and i >= 16:
                y = 100
                multiplicador = i // 2 - 8
                x -= multiplicador * espacamento  # Posição x do trevo

                # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo, image1=imagem_fundo, image2=imagem_fundo, dim=dim)

                botao.rect.center = (x, y)
                botoes[botao] = table[i]
        else:
            dim = 50
            espacamento = 55
            y = 82
            x = 480
            if i == 0:
                x = 480
                botao = Botao1(ButtonGrups, image=imagem_fundo, image1=imagem_fundo, image2=imagem_fundo, dim=dim)

                botao.rect.center = (x, y)
                botoes[botao] = table[i]


            elif i % 2 == 0:
                multiplicador = i // 2
                x += multiplicador * espacamento  # Posição x do trevo

            # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo,image1=imagem_fundo, image2=imagem_fundo, dim=dim)
                botao.rect.center = (x, y)
                botoes[botao] = table[i]
            elif i % 2 != 0:
                multiplicador = i // 2 + 1
                x -= multiplicador * espacamento  # Posição x do trevo

                # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo, image1=imagem_fundo, image2=imagem_fundo, dim=dim)

                botao.rect.center = (x, y)
                botoes[botao] = table[i]
def esvazia_table(esvaziar, screen,table, ButtonGrups,botoes):
    if len(table) == 10 and not esvaziar[0]:
        ButtonGrups.empty()
        esvaziar[0] = True
    table_exibicao(botoes, table, ButtonGrups)
    ButtonGrups.update()
    ButtonGrups.draw(screen)
def escolha_trevo_table(botoes, table):

    key = True
    while key:
        for botao in botoes.keys():
            if botao.touche == True:
                trevo = botoes[botao]
                key = False
    print(botoes)
    if trevo == table[0]:
        Botao18.touche = False
    print("trevo", trevo)
    return trevo
def caixa_retirada_table(nome_jogador, trevo):
    trevo_1 = 0
    if trevo > 20:
        trevo_1 = trevo - 20
    else:
        trevo_1 = trevo

    passos.insert(0, "%s - Retirou da table o trevo %d" % (nome_jogador, trevo_1))
    caixa_texto.html_text = "\n".join(passos)
    caixa_texto.rebuild()
    clock = pygame.time.Clock()
    tempo_delta = clock.tick(60) / 1000.0
    gerenciador.update(tempo_delta)
    gerenciador.draw_ui(screen)
def caixa_retirada_baralho(nome_jogador, trevo):
    trevo_1 = 0
    if trevo > 20:
        trevo_1 = trevo - 20
    else:
        trevo_1 = trevo

    passos.insert(0, "%s - Retirou do baralho o trevo %d" % (nome_jogador, trevo_1))
    caixa_texto.html_text = "\n".join(passos)
    caixa_texto.rebuild()
    clock = pygame.time.Clock()
    tempo_delta = clock.tick(60) / 1000.0
    gerenciador.update(tempo_delta)
    gerenciador.draw_ui(screen)
def caixa_subst_table(nome_jogador, trevo_taboleiro, trevo):
    trevo_1 = 0
    trevo_taboleiro_1 = 0
    if trevo > 20:
        trevo_1 = trevo - 20
    else:
        trevo_1 = trevo

    if trevo_taboleiro > 20:
        trevo_taboleiro_1 = trevo_taboleiro - 20
    else:
        trevo_taboleiro_1 = trevo_taboleiro

    passos.insert(0, "%s - O trevo %d foi colocado na table pois foi substituido pelo trevo %d" % (nome_jogador, trevo_taboleiro_1, trevo_1))
    caixa_texto.html_text = "\n".join(passos)
    caixa_texto.rebuild()
    clock = pygame.time.Clock()
    tempo_delta = clock.tick(60) / 1000.0
    gerenciador.update(tempo_delta)
    gerenciador.draw_ui(screen)
def caixa_trevo_colocacao(nome_jogador, trevo, linha, coluna):
    trevo_1 = 0
    if trevo > 20:
        trevo_1 = trevo - 20
    else:
        trevo_1 = trevo
    passos.insert(0, "%s - O trevo %d foi colocado na linha %d, coluna %d" % (nome_jogador, trevo_1, linha, coluna))
    caixa_texto.html_text = "\n".join(passos)
    caixa_texto.rebuild()
    clock = pygame.time.Clock()
    tempo_delta = clock.tick(60) / 1000.0
    gerenciador.update(tempo_delta)
    gerenciador.draw_ui(screen)
def caixa_trevo_table(nome_jogador, trevo):
    trevo_1 = 0
    if trevo > 20:
        trevo_1 = trevo - 20
    else:
        trevo_1 = trevo
    passos.insert(0, "%s - mandou o trevo %d para a table" % (nome_jogador, trevo_1))
    caixa_texto.html_text = "\n".join(passos)
    caixa_texto.rebuild()
    clock = pygame.time.Clock()
    tempo_delta = clock.tick(60) / 1000.0
    gerenciador.update(tempo_delta)
    gerenciador.draw_ui(screen)
def player_nome(nome_player1,nome_player2, screen):
    player1 = message_to_screen(nome_player1, None, 25, [0, 100, 0])
    screen.blit(player1, (1075 - player1.get_width() // 2, 116 - player1.get_height() // 2))
    screen.blit(player1, (290 - player1.get_width() // 2, 185 - player1.get_height() // 2))

    if nome_player2 == "BOT":
        player2 = message_to_screen("BOT", None, 25, [255, 0, 0])
        screen.blit(player2, (1050 - player2.get_width() // 2, 205 - player2.get_height() // 2))
    else:
        player2 = message_to_screen(nome_player2, None, 25, [255, 0, 0])
        screen.blit(player2, (1075 - player2.get_width() // 2, 205 - player2.get_height() // 2))

    screen.blit(player2, (730 - player2.get_width() // 2, 185 - player2.get_height() // 2))
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

    with open("versao_salva.txt", "w") as f:
        f.write("versao/tm"+ "\n")
        f.write("Jogador1/" + str(winner["Jogador1"]) + "\n")
        f.write("Jogador2/" + str(winner["Jogador2"]) + "\n")
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
    print(taboleiro1)
    #print("TASSDADSAD -", taboleiro1)

    lista_coluna = []
    lista_linha = []

    for i in range(4):

        if taboleiro1[i][coluna] > 20:
            print(taboleiro1[i][coluna])
            lista_coluna.append(taboleiro1[i][coluna] - 20)
        else:
            print(taboleiro1[i][coluna])
            if taboleiro1[i][coluna] != 0:
                lista_coluna.append(taboleiro1[i][coluna])

        if taboleiro1[linha][i] > 20:
            print(taboleiro1[linha][i])
            lista_linha.append(taboleiro1[linha][i] - 20)
        else:
            print(taboleiro1[linha][i])
            if taboleiro1[linha][i] != 0:
                lista_linha.append(taboleiro1[linha][i])

    print(lista_linha)
    print(lista_coluna)

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
        if len(table) == 0 and proxima != 1:  # quando nao existem trevos na table, tem que gerar um novo
            msg_to_screen_escolha_posicao(screen, nome_jogador1)

            while key:
                trevo = random.randint(1, totaltrevos)
                if trevo not in excluidos:
                    key = False
                    excluidos.append(trevo)


            taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
            caixa_retirada_baralho(nome_jogador1, taboleiroj[4][0])

            exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
            pygame.display.flip()
            pygame.display.update()

            guardar_na_mem(nome_jogador1, taboleiroj, excluidos, table,nome_jogador1, proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais
        else:  # se ja existirem trevos na table, pode usar um do baralho ou usar um da table
            if proxima != 1:

                key1 = True
                msg_to_screen_escolha_table_baralho(screen, nome_jogador1)

                pygame.display.flip()
                pygame.display.update()


                for x in botoes.keys():
                    x.touche = False

                Botao18.touche = False

                while key1:
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                        ButtonGrups.update()

                    if Botao18.touche:
                        ButtonGrups1.update()

                    for botao in botoes.keys():
                        if botao.touche == True:

                            trevo = escolha_trevo_table(botoes, table)

                            if trevo in table:
                                table.remove(trevo)
                            caixa_retirada_table(nome_jogador1, trevo)
                            taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro

                            atualiza_screen(screen, cond_final, table, nome_jogador1, nome_jogador2)

                            Botao18.touche = False #se eu clicar em um elemento da table (que nao esta contido em botoes), o botao18 que serve para colocar elementos na table vai ficar a true e vai afetar a funcao em baixo
                            botao.touche = False
                            key1 = False
                            break

                    if Botao17.touche == True:  # se ele pressionou o baralho
                        key = True
                        while key:
                            trevo = random.randint(1, totaltrevos)
                            if trevo not in excluidos:
                                key = False
                                excluidos.append(trevo)


                        taboleiroj[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                        caixa_retirada_baralho(nome_jogador1, taboleiroj[4][0])
                        exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                        pygame.display.flip()
                        pygame.display.update()

                        Botao17.touche = False
                        break

                guardar_na_mem(nome_jogador1, taboleiroj, excluidos, table,nome_jogador1, proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais

        msg_to_screen_escolha_posicao(screen, nome_jogador1) #escolhe a posicao para por o trevo

        key = True

        if proxima == 1 or proxima == -1:
            while key:

                exibir_taboleiro(cond_final, taboleiroj, screen,Jog2=0)
                pygame.display.flip()
                pygame.display.update()
                key1 = True
                while key1:
                    resultado = escolha_posicao_trevo(ButtonGrups,ButtonGrups1, "Jogador1")
                    linha = resultado[0]
                    coluna = resultado[1]
                    if linha == -9 and coluna == -9:

                        caixa_trevo_table(nome_jogador1, taboleiroj[4][0]) #"O %s mandou o trevo para a table"
                        table.append(taboleiroj[4][0])
                        key = False
                        key1 = False
                        taboleiroj[4][0] = 0
                        atualiza_screen(screen, cond_final, table, nome_jogador1, nome_jogador2)

                    elif taboleiroj[linha][coluna] == 0:
                        if verificar_taboleiro(taboleiroj, linha, coluna, taboleiroj[4][0]):
                            caixa_trevo_colocacao(nome_jogador1, taboleiroj[4][0], linha, coluna) #"\nO trevo %d foi colocado na linha %d, coluna %d\n"

                            taboleiroj[linha][coluna] = taboleiroj[4][0]
                            key = False
                            key1 = False
                            taboleiroj[4][0] = 0
                            atualiza_screen(screen, cond_final, table, nome_jogador1, nome_jogador2)

                    else:
                        if verificar_taboleiro(taboleiroj, linha, coluna, taboleiroj[4][0]):

                            caixa_trevo_colocacao(nome_jogador1, taboleiroj[4][0], linha, coluna) #"\nO trevo %d foi colocado na linha %d, coluna %d\n"
                            caixa_subst_table(nome_jogador1, taboleiroj[linha][coluna], taboleiroj[4][0]) #\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n"

                            table.append(taboleiroj[linha][coluna])
                            taboleiroj[linha][coluna] = taboleiroj[4][0]
                            key = False
                            key1 = False
                            taboleiroj[4][0] = 0
                            atualiza_screen(screen, cond_final, table, nome_jogador1, nome_jogador2)
                            break

                retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
                remover_message_to_screen(retangulo1, screen)


        passos.insert(0, "")
        caixa_texto.html_text = "\n".join(passos)
        caixa_texto.rebuild()
        guardar_na_mem(nome_jogador1, taboleiroj, excluidos, table, nome_jogador2, proxima=-1) #vai alterar na memoria os valores do taboleiro pelos atuais
def turnoj2(proxima, cond_final, imagem_fundo, screen, nome_jogador2, taboleiroj2, excluidos, totaltrevos, key_inicial, table,nome_jogador1, ButtonGrups, posy17=88,posx17=110):  # funcao destinada ao turno do jogador
    print("JOGADOR2")

    key = True

    if len(table) == 0 and proxima != 1:  # quando nao existem trevos na table, tem que gerar um novo
        msg_to_screen_escolha_posicao(screen, nome_jogador2)

        while key:
            trevo = random.randint(1, totaltrevos)
            if trevo not in excluidos:
                key = False
                excluidos.append(trevo)

        caixa_retirada_baralho(nome_jogador2, trevo)
        taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
        exibir_taboleiro(cond_final, taboleiroj2, screen, Jog2=1)

        pygame.display.flip()
        pygame.display.update()

        guardar_na_mem(nome_jogador2, taboleiroj2, excluidos, table, nome_jogador2,proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais
    else:  # se ja existirem trevos na table, pode usar um do baralho ou usar um da table
        if proxima != 1:
            key1 = True
            msg_to_screen_escolha_table_baralho(screen, nome_jogador2)

            pygame.display.flip()
            pygame.display.update()
            for x in botoes.keys():
                x.touche = False

            Botao18.touche = False

            while key1:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    ButtonGrups.update()
                if Botao18.touche == True:
                    ButtonGrups1.update()

                for botao in botoes.keys():
                    if botao.touche == True:

                        trevo = escolha_trevo_table(botoes, table)

                        if trevo in table:
                            table.remove(trevo)

                        caixa_retirada_table(nome_jogador2, trevo)
                        taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                        atualiza_screen(screen, cond_final, table, nome_jogador1, nome_jogador2)

                        botao.touche = False
                        Botao18.touche = False  # se eu clicar em um elemento da table (que nao esta contido em botoes), o botao18 que serve para colocar elementos na table vai ficar a true e vai afetar a funcao em baixo
                        key1 = False
                        break

                if Botao17.touche == True:  # se ele pressionou o baralho

                    key = True
                    while key:
                        trevo = random.randint(1, totaltrevos)
                        if trevo not in excluidos:
                            key = False
                            excluidos.append(trevo)

                    caixa_retirada_baralho(nome_jogador2, trevo)

                    taboleiroj2[4][0] = trevo  # trevo escolhido para a parte debaixo do taboleiro
                    exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
                    pygame.display.flip()
                    pygame.display.update()

                    Botao17.touche = False
                    break

            guardar_na_mem(nome_jogador2, taboleiroj2, excluidos, table, nome_jogador2,proxima=1)  # vai alterar na memoria os valores do taboleiro pelos atuais

    msg_to_screen_escolha_posicao(screen, nome_jogador2)
    key = True


    if proxima == 1 or proxima == -1:
        while key:

            exibir_taboleiro(cond_final, taboleiroj2, screen,Jog2=1)
            pygame.display.flip()
            pygame.display.update()
            key1 = True
            while key1:

                resultado = escolha_posicao_trevo(ButtonGrups,ButtonGrups1, "Jogador2")
                linha = resultado[0]
                coluna = resultado[1]
                if linha == -9 and coluna == -9:
                    print("O %s mandou o trevo para a table" % nome_jogador2)
                    table.append(taboleiroj2[4][0])
                    key = False
                    key1 = False
                    caixa_trevo_table(nome_jogador2, taboleiroj2[4][0])
                    taboleiroj2[4][0] = 0
                    atualiza_screen(screen, cond_final, table, nome_jogador1, nome_jogador2)

                elif taboleiroj2[linha][coluna] == 0:
                    if verificar_taboleiro(taboleiroj2, linha, coluna, taboleiroj2[4][0]):
                        print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (taboleiroj2[4][0], linha, coluna))
                        caixa_trevo_colocacao(nome_jogador2, taboleiroj2[4][0], linha, coluna)
                        taboleiroj2[linha][coluna] = taboleiroj2[4][0]
                        key = False
                        key1 = False
                        taboleiroj2[4][0] = 0
                        atualiza_screen(screen, cond_final, table, nome_jogador1, nome_jogador2)


                else:
                    if verificar_taboleiro(taboleiroj2, linha, coluna, taboleiroj2[4][0]):
                        print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (taboleiroj2[4][0], linha, coluna))
                        print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (taboleiroj2[linha][coluna], taboleiroj2[4][0]))

                        caixa_trevo_colocacao(nome_jogador2, taboleiroj2[4][0], linha, coluna)
                        caixa_subst_table(nome_jogador2, taboleiroj2[linha][coluna], taboleiroj2[4][0])
                        table.append(taboleiroj2[linha][coluna])
                        taboleiroj2[linha][coluna] = taboleiroj2[4][0]
                        key = False
                        key1 = False
                        taboleiroj2[4][0] = 0
                        atualiza_screen(screen, cond_final, table, nome_jogador1, nome_jogador2)

                        break
            retangulo1 = pygame.image.load("imagens_jogo/retangulo1.png").convert_alpha()
            remover_message_to_screen(retangulo1, screen)



    passos.insert(0, "")
    caixa_texto.html_text = "\n".join(passos)
    caixa_texto.rebuild()
    guardar_na_mem(nome_jogador2, taboleiroj2, excluidos, table, nome_jogador1,proxima=-1)  # vai alterar na memoria os valores do taboleiro pelos atuais
def turnob(Cond_final, screen, taboleirob, excluidos,totaltrevos, key_inicial, table, jogador1, jogador2="BOT"):#funcao destinada ao turno do bot
        msg_to_screen_escolha_posicao(screen, jogador2)
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
        caixa_retirada_baralho("BOT", trevo)

        time.sleep(1.5)
        while key1:
            linha = random.randint(0, 3)
            coluna = random.randint(0, 3)
            if taboleirob[linha][coluna] == 0:
                if verificar_taboleiro(taboleirob, linha, coluna, trevo):
                    print("O bot colocou o trevo na linha %d e coluna %d\n" % (linha, coluna))
                    caixa_trevo_colocacao("BOT", trevo, linha, coluna)
                    taboleirob[linha][coluna] = trevo
                    key1 = False
            else:
                if verificar_taboleiro(taboleirob, linha, coluna, trevo):
                    print("O bot colocou o trevo na linha %d e coluna %d\n" % (linha, coluna))

                    caixa_trevo_colocacao("BOT", trevo, linha, coluna)
                    caixa_subst_table("BOT", taboleirob[linha][coluna], trevo)

                    print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (taboleirob[linha][coluna], trevo))
                    table.append(taboleirob[linha][coluna])
                    taboleirob[linha][coluna] = trevo
                    key1 = False

        screen.blit(imagem_fundo, (0, 0))

        for i in range(4):
            print(str(taboleirob[i][0]), " | ", str(taboleirob[i][1]), " | ", str(taboleirob[i][2]), " | ",
                  str(taboleirob[i][3]))
        print("\n")

        pygame.display.flip()
        pygame.display.update()
        #time.sleep(1)
        taboleirob[4][0] = 0

        passos.insert(0, "")
        caixa_texto.html_text = "\n".join(passos)
        caixa_texto.rebuild()
        guardar_na_mem(jogador2, taboleirob, excluidos, table, jogador1, proxima=-1)

def load_tm():
    pygame.init()

    largura = 1200
    altura = 700
    global gerenciador,caixa_texto, passos, screen
    cor_de_fundo = pygame.Color(0, 132, 252)  # cor vai ser o azul usado na tela dos botoes inicial
    gerenciador = pygame_gui.UIManager((largura, altura))

    # Defina a posição e tamanho da caixa de texto
    poscaixa_x = 930
    poscaixa_y = 260
    largura_caixa = 260
    altura_caixa = 395

    # Crie a caixa de texto
    caixa_texto = pygame_gui.elements.UITextBox("",
                                                relative_rect=pygame.Rect((poscaixa_x, poscaixa_y),
                                                                          (largura_caixa, altura_caixa)),
                                                manager=gerenciador)

    # Variável para armazenar os passos do jogador
    passos = []

    class Botao(pygame.sprite.Sprite):
        def __init__(self, *groups, image, image1, image2, posx, posy, dim=73, botao18=0):
            super().__init__(*groups)
            if botao18 == 1:
                dim1 = 83
                dim = 632
            else:
                dim1 = dim
            self.image = pygame.image.load(image).convert_alpha()

            self.rect = pygame.Rect(posx, posy, dim, dim1)

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

    global imagem_fundo, ButtonGrups1
    # dá load da imagem
    imagem_fundo = pygame.image.load("imagens_jogo/template_jogo_final.png").convert_alpha()
    imagem_fundo = pygame.transform.scale(imagem_fundo, (1200, 700))


    # faz o blit + posicao da imagem
    screen.blit(imagem_fundo, (0, 0))

    # é uma função do Pygame que atualiza a tela.
    pygame.display.flip()
    # ButtonGrups é uma variável que contém um objeto do tipo Group.
    ButtonGrups = pygame.sprite.Group()
    ButtonGrups1 = pygame.sprite.Group()

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
                    image2="imagens_gerais/red_button02.png", posx=495, posy=87, dim=44, botao18=1)
    Botao18.rect.center = (471, 80)
    cores_jogadores = {"Player1":[0, 255, 127], "Player2":[255, 0, 0]}
    retangulo = pygame.image.load("imagens_jogo/retangulo.png").convert_alpha()
    global botoes, winner
    winner = {}
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


    with open("versao_salva.txt", "r") as f:
        linhas = f.readlines()

    i = 0
    for linha in linhas:
        if i == 0:
            i += 1
            continue
        else:
            jog, pontos = linha.strip().split("/")
            winner[jog] = int(pontos)
            i += 1

    nome_jogador1 = dicionario["jogador1"]
    nome_jogador2 = dicionario["jogador2"]

    global taboleiroJ1, taboleiroJ2, esvaziar
    Comeco = [False, False]
    print(dicionario)
    J2_preenhido = False  # o bot ja preencheu o taboleiro?
    J1_prenchido = False  # o jogador ja preencheu o taboleiro?
    taboleiroJ1 = dicionario[nome_jogador1]  # taboleiro do bot com base na memoria
    taboleiroJ2 = dicionario[nome_jogador2]  # taboleiro do jogador com base na memoria
    prox_jogador = dicionario["jogador"][0]  # proximo jogador a jogar com base na memoria
    trevos = dicionario["excluidos"]  # obter os trevos "excluidos" que ja foram usados
    table = dicionario["table"]  # obter os trevos que estavam na table
    joana = pygame.image.load("imagens_jogo/joaninha.png").convert_alpha()
    proxima_acao = dicionario["proxima"][0]
    print(proxima_acao)
    Cond_final = [J1_prenchido, J2_preenhido]
    exibir_taboleiro(Cond_final, taboleiroJ2, screen, Jog2=1)
    exibir_taboleiro(Cond_final, taboleiroJ1, screen,Jog2=0)
    esvaziar = [False]

    botoes = {}


    clock = pygame.time.Clock()
    tempo_delta = clock.tick(60) / 1000.0

    print(winner)
    if prox_jogador == nome_jogador2:
        print("O %s começa!" % nome_jogador2)
        gerenciador.update(tempo_delta)
        if winner["Jogador1"] == 0 and winner["Jogador2"] == 0:
            print("1 jogo")
            jogo(proxima_acao, winner, nome_jogador2, nome_jogador1, esvaziar, Cond_final, trevos, screen, table, gerenciador,
                 tempo_delta, nome_jogador1, nome_jogador2, taboleiroJ2, retangulo, Comeco, joana, ButtonGrups, taboleiroJ1, botoes)
            table = []
            trevos = []
            taboleiroJ1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0]]  # taboleiro do jogador
            taboleiroJ2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0]]  # taboleiro do bot
            esvaziar = [False]
            botoes = {}  # lista com os botoes da table

        print("2 jogo")
        jogo(proxima_acao, winner, nome_jogador2, nome_jogador1, esvaziar, Cond_final, trevos, screen, table, gerenciador,
                 tempo_delta, nome_jogador1, nome_jogador2, taboleiroJ2, retangulo, Comeco, joana, ButtonGrups, taboleiroJ1, botoes)
        apagar_ficheiro_save()
        leaderboard(winner, nome_jogador1, nome_jogador2, com_nome_jogadores=0)
        print(winner)
        if winner[nome_jogador1] > winner[nome_jogador2]:
            print("Ganhou -> ", nome_jogador1)
        elif winner[nome_jogador1] < winner[nome_jogador2]:
            print("Ganhou -> ", nome_jogador2)
        else:
            print("empate")

    else:
        print("O %s começa!" % nome_jogador1)
        gerenciador.update(tempo_delta)
        if winner["Jogador1"] == 0 and winner["Jogador2"] == 0:
            print("1 jogo")
            jogo(proxima_acao, winner, nome_jogador1, nome_jogador2, esvaziar, Cond_final, trevos, screen, table, gerenciador,
                 tempo_delta, nome_jogador1, nome_jogador2, taboleiroJ2, retangulo, Comeco, joana, ButtonGrups, taboleiroJ1, botoes)
            table = []
            trevos = []
            taboleiroJ1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0]]  # taboleiro do jogador
            taboleiroJ2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0]]  # taboleiro do bot
            esvaziar = [False]
            botoes = {}  # lista com os botoes da table

        print("2 jogo")
        jogo(proxima_acao, winner, nome_jogador1, nome_jogador2, esvaziar, Cond_final, trevos, screen, table, gerenciador,
                 tempo_delta, nome_jogador1, nome_jogador2, taboleiroJ2, retangulo, Comeco, joana, ButtonGrups, taboleiroJ1, botoes)
        apagar_ficheiro_save()
        leaderboard(winner, nome_jogador1, nome_jogador2, com_nome_jogadores=0)

        print(winner)
        if winner[nome_jogador1] > winner[nome_jogador2]:
            print("Ganhou -> ", nome_jogador1)
        elif winner[nome_jogador1] < winner[nome_jogador2]:
            print("Ganhou -> ", nome_jogador2)
        else:
            print("empate")

pygame.quit()
#load_jogo_normal()

def apagar_ficheiro_save():
    with open("versao_salva.txt", "w") as f:
        f.write("")