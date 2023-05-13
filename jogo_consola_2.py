import copy
import random
import json
import os

""" Realizar o turno do primeiro jogador. Considera-se um turno de um jogador o conjunto
das ações que esse jogador executa até passar a vez ao jogador seguinte ou até o jogo
terminar. Só devem ser autorizadas as ações possíveis em cada fase.
a. Quando for o jogador humano a jogar seguir a sequência da jogada:
I. Escolher um trevo
II. Escolher o posicionamento
III. Passar a vez
IV. Sair (além de interromper o jogo deve gravar o estado do mesmo).
b. Quando for o Jogador BOT a jogar, aplicar um algoritmo para o BOT mostrando
as ações escolhidas pelo mesmo.
c. Tomada a decisão da ação escolhida (humano ou BOT), realizá-la e atualizar a
consola com os novos dados.
d. Depois de uma ação de qualquer Jogador (Humano ou BOT) gravar SEMPRE o
estado atual do jogo, de modo a ser possível dar a opção do jogador de
interromper para continuar mais tarde.
e. Todas as ações dos jogadores devem ser mantidas em memória, apresentando
na consola as ações do último turno dos dois jogadores"""
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
def exibir_taboleiro(taboleiro):
    for i in range(4):
        print(str(taboleiro[i][0]), " | ", str(taboleiro[i][1]), " | ", str(taboleiro[i][2]), " | ", str(taboleiro[i][3]))
    print("\n")
def verificar_taboleiro(taboleiro, linha, coluna, trevo):
    taboleiro1 = copy.deepcopy(taboleiro)
    taboleiro1[linha][coluna] = trevo
    #print("TASSDADSAD -", taboleiro1)
    lista_coluna = []
    lista_linha = []

    if trevo > 60:
        trevo_real = trevo - 60
    elif trevo > 40:
        trevo_real = trevo - 40
    elif trevo > 20:
        trevo_real = trevo - 20
    else:
        trevo_real = trevo

    for i in range(4):
        if  taboleiro1[i][coluna] > 60:
            lista_linha.append(taboleiro1[i][coluna] - 60)
        elif  taboleiro1[i][coluna] > 40:
            lista_linha.append(taboleiro1[i][coluna] - 40)
        elif  taboleiro1[i][coluna] > 20:
            lista_linha.append(taboleiro1[i][coluna] - 20)
        else:
            if taboleiro1[i][coluna] == 0:
                continue
            else:
                lista_coluna.append(taboleiro1[i][coluna])

        if taboleiro1[linha][i] > 60:
            lista_coluna.append(taboleiro1[linha][i] - 60)
        elif taboleiro1[linha][i] > 40:
            lista_coluna.append(taboleiro1[linha][i] - 40)
        elif taboleiro1[linha][i] > 20:
            lista_coluna.append(taboleiro1[linha][i] - 20)
        else:
            if taboleiro1[linha][i] == 0:
                continue
            else:
                lista_linha.append(taboleiro1[linha][i])
    #print(lista_coluna)
    #print(lista_linha)
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
def turnoj(nome, taboleiroj, excluidos, totaltrevos, key_inicial, table, jogador):#funcao destinada ao turno do jogador
    print("JOGADOR")
    if key_inicial[1]: #se for a primeira jogada
        key_inicial[1] = primeira_rodada(taboleiroj, excluidos, totaltrevos)
        exibir_taboleiro(taboleiroj)

    else:
        key = True
        while key:
            trevo = random.randint(1, totaltrevos)
            if trevo not in excluidos:
                key = False
                excluidos.append(trevo)

        key = True
        print("Trevo - ", trevo)

        exibir_taboleiro(taboleiroj)

        while key:
            tabela = input("Queres colocar o trevo na table (S/N): ")
            if tabela == "S" or tabela == "s":
                table.append(trevo)
                key = False
                print("\nO trevo %d foi colocado na table\n" % trevo)
            else:
                linha = int(input("Em que linha queres colocar o trevo: "))
                coluna = int(input("Em que coluna queres colocar o trevo: "))

                if taboleiroj[linha][coluna] == 0:
                    if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                        print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (trevo, linha, coluna))
                        taboleiroj[linha][coluna] = trevo
                        key = False
                else:
                    if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                        print("\nO trevo %d foi colocado na linha %d, coluna %d\n" % (trevo, linha, coluna))
                        print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (trevo, taboleiroj[linha][coluna]))
                        table.append(taboleiroj[linha][coluna])
                        taboleiroj[linha][coluna] = trevo
                        key = False

    guardar_na_mem(nome, taboleiroj, excluidos, table, jogador) #vai alterar na memoria os valores do taboleiro pelos atuais
def turnob(taboleirob, excluidos,totaltrevos, key_inicial, table, jogador):#funcao destinada ao turno do bot
    if key_inicial[0]:#se for a primeira jogada
        print("BOT")
        key_inicial[0] = primeira_rodada(taboleirob, excluidos, totaltrevos)

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
                    print("\nO trevo %d foi colocado na table pois foi substituido pelo trevo %d\n" % (trevo, taboleirob[linha][coluna]))
                    table.append(taboleirob[linha][coluna])
                    taboleirob[linha][coluna] = trevo
                    key = False

    exibir_taboleiro(taboleirob)
    guardar_na_mem("BOT", taboleirob, excluidos, table, jogador)
def opcaoA():

    B_preenhido = False #o bot ja preencheu o taboleiro?
    J_prenchido = False #o jogador ja preencheu o taboleiro?
    trevos = [] #todos os trevos vao parar aqui para que nao haja repeticao na geracao de trevos
    taboleiroJ = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #taboleiro do jogador
    taboleiroB = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #taboleiro do bot
    table = []


    nome = input("\nNome do jogador: ")

    initial_write_to_mem(nome, taboleiroJ, trevos, table) #guarda os taboleiros na mem com os nomes do bot e do jogador

    numero = random.randint(0, 1) # quem comeca

    Comeco = [True, True]
    if numero == 0:
        print("Bot começa!")
        while (not B_preenhido and not J_prenchido) and not (len(trevos) == 40):#as condicoes de fim do jogo sao alguem ja ter preenchido to do o taboleiro ou os trevos esgotarem-se
            turnob(taboleiroB, trevos, 40, Comeco, table, nome)
            turnoj(nome,taboleiroJ, trevos, 40, Comeco, table, "BOT")
            #print(table)
            """a = int(input("cheat: "))
            if a == 0:
                B_preenhido = False
                J_prenchido = False"""
        # print(trevos)
    else:
        print("O %s começa!" % nome)
        while (not B_preenhido or not J_prenchido) and not (len(trevos) == 40):
            turnoj(nome, taboleiroJ, trevos, 40, Comeco, table, "BOT")
            turnob(taboleiroB, trevos, 40, Comeco, table, nome)
            #print(table)
            """a = int(input("cheat: "))
            if a == 0:
                B_preenhido = False
                J_prenchido = False"""
        # print(trevos)
def opcaoB():
    dicionario = {}
    B_preenhido = False  # o bot ja preencheu o taboleiro?
    J_prenchido = False  # o jogador ja preencheu o taboleiro?
    trevos = []  # todos os trevos vao parar aqui para que nao haja repeticao na geracao de trevos
    table = []

    with open("save.txt", "r") as f:
        linhas = f.readlines()

    for linha in linhas:
        nome, tabuleiro_str = linha.strip().split("/")
        tabuleiro = eval(tabuleiro_str)
        dicionario[nome] = tabuleiro

    taboleiroB = dicionario["BOT"] #taboleiro do bot com base na memoria
    taboleiroJ = dicionario["aa"] #taboleiro do jogador com base na memoria
    prox_jogador = dicionario["jogador"] #proximo jogador a jogar com base na memoria
    trevos = dicionario["excluidos"] #obter os trevos "excluidos" que ja foram usados
    table = dicionario["table"] #obter os trevos que estavam na table
    #numero = random.randint(0, 1)  # quem comeca
    nome = "aa"
    Comeco = [False, False]

    if prox_jogador == "BOT":
        print("Bot começa!")
        while (not B_preenhido and not J_prenchido) and not (len(trevos) == 40):  # as condicoes de fim do jogo sao alguem ja ter preenchido to do o taboleiro ou os trevos esgotarem-se
            turnob(taboleiroB, trevos, 40, Comeco, table, nome)
            turnoj(nome, taboleiroJ, trevos, 40, Comeco, table, "BOT")
            print(table)
            """a = int(input("cheat: "))
            if a == 0:
                B_preenhido = False
                J_prenchido = False"""
        # print(trevos)
    else:
        print("O %s começa!" % nome)
        while (not B_preenhido or not J_prenchido) and not (len(trevos) == 40):
            turnoj(nome, taboleiroJ, trevos, 40, Comeco, table, "BOT")
            turnob(taboleiroB, trevos, 40, Comeco, table, nome)
            print(table)
            """a = int(input("cheat: "))
            if a == 0:
                B_preenhido = False
                J_prenchido = False"""

def opcaoC():
    print(' Lucky Numbers é um jogo de tabuleiro no qual o utilizador tem que fazer uma sequência crescente de números tanto horizontalmente como verticalmente.\n A cada jogada é fornecida um numero novo,exceto quando na jogada anterior o utilizador não tenha posto no tabuleiro o número que lhe foi atribuido ou se trocou com um dos números\n que já estava no tabuleiro, nestes casos, o número substituido vai para a mesa de cima, a qual ambos os jogadores têm acesso\n e que podem utilizar para futuras trocas de números se assim lhes der jeito. ')
def opcaoD():
    exit()

key = True

while key:
    print("A. Jogar uma Partida\nB. Carregar uma partida a partir de um ficheiro\nC. Apresentar uma descrição do jogo\nD. Sair da aplicação.")
    op = input("Seleciona a opcao: ")
    match op:
        case "A":
            opcaoA()
            key = False
            break

        case "B":
            opcaoB()
            key = False
            break

        case "C":
            opcaoC()
            key = False
            break

        case "D":
            opcaoD()
            key = False
            break
