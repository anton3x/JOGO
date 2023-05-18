import random
def primeira_rodada(controlo, taboleiro, excluidos, totaltrevos): #funcao destinada a gerar os trevos e colocar no taboleiro na primeira ronda do jogo
    #aVnE = False  # algum valor nos excluidos
    trevo = []


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

    #trevo_final.sort() #organiza os numeros por ordem crescente


    if (trevo_final[0] not in n_vezes) or (n_vezes[trevo_final[0]] == 0):  #se o elemento do vetor existir no dicionario e o seu valor == 0, quer dizer que ja foi percorrido um elemento antes dele com o mesmo valor, isto acontece pois existem 2 numeros de cada pois existem 2 cores
        trevo_final[0] += 20    #entao retornamos um deles ao seu valor original, nao vai afetar o taboleiro, pois o valor real vai continuar a ser (x - 20)
        while key1:
            print("Posicao: ")

            resultado = escolha_posicao_trevo(ButtonGrups, screen,
                                              Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,
                                              Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16,
                                              Botao17, Botao18,
                                              posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                              posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                              posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12,
                                              posy13,
                                              posy14, posy15, posy16, posy17=88, posx17=110)
            linha = resultado[0]
            coluna = resultado[1]
            # print(linha,coluna)
            if linha == -9 and coluna == -9:
                print("O %s mandou o trevo para a table" % nome)
                table.append(trevo)
                key = False
                key1 = False
                taboleiroj[4][0] = 0
                screen.blit(imagem_fundo, (0, 0))
                pygame.display.flip()
                pygame.display.update()
            elif taboleiroj[linha][coluna] == 0:
                # print("verificar")
                if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                    # print("feito")
                    print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (trevo, linha, coluna))
                    taboleiroj[linha][coluna] = trevo
                    key = False
                    key1 = False
                    taboleiroj[4][0] = 0
                    screen.blit(imagem_fundo, (0, 0))
                    pygame.display.flip()  # aparece o trevo na parte de baixo do taboleiro
                    pygame.display.update()

            else:
                # print("verificar")
                if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                    # print("feito")
                    print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (trevo, linha, coluna))
                    print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (
                    taboleiroj[linha][coluna], trevo))
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
        n_vezes[trevo_final[0]] = 0 #se ainda estiver a 1, quer dizer que +e o primeiro que aparece, ou seja, poem a 0
        while key1:
            print("Posicao: ")

            resultado = escolha_posicao_trevo(ButtonGrups, screen,
                                              Botao1, Botao2, Botao3, Botao4, Botao5, Botao6, Botao7, Botao8,
                                              Botao9, Botao10, Botao11, Botao12, Botao13, Botao14, Botao15, Botao16,
                                              Botao17, Botao18,
                                              posx1, posx2, posx3, posx4, posx5, posx6, posx7, posx8, posx9,
                                              posx10, posx11, posx12, posx13, posx14, posx15, posx16, posy1, posy2,
                                              posy3, posy4, posy5, posy6, posy7, posy8, posy9, posy10, posy11, posy12,
                                              posy13,
                                              posy14, posy15, posy16, posy17=88, posx17=110)
            linha = resultado[0]
            coluna = resultado[1]
            # print(linha,coluna)
            if linha == -9 and coluna == -9:
                print("O %s mandou o trevo para a table" % nome)
                table.append(trevo)
                key = False
                key1 = False
                taboleiroj[4][0] = 0
                screen.blit(imagem_fundo, (0, 0))
                pygame.display.flip()
                pygame.display.update()
            elif taboleiroj[linha][coluna] == 0:
                # print("verificar")
                if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                    # print("feito")
                    print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (trevo, linha, coluna))
                    taboleiroj[linha][coluna] = trevo
                    key = False
                    key1 = False
                    taboleiroj[4][0] = 0
                    screen.blit(imagem_fundo, (0, 0))
                    pygame.display.flip()  # aparece o trevo na parte de baixo do taboleiro
                    pygame.display.update()

            else:
                # print("verificar")
                if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                    # print("feito")
                    print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (trevo, linha, coluna))
                    print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (
                    taboleiroj[linha][coluna], trevo))
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



    #print(trevo_final)
    if controlo == 4:
        return False    #retorna falso para dizer que ja fez a primeira jogada

    return True
