import copy
import random

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

def primeira_rodada(taboleiro, excluidos, totaltrevos):
    key = True
    aVnE = False  # algum valor nos excluidos

    while key:
        trevo = []
        for i in range(4):  # gerar 4 valores de 1 até totaltrevos
            trevo.append(random.randint(1, totaltrevos))

        for i in range(4):
            if i == 3:  # se estiver no 4 elemento
                if trevo[i] not in excluidos and not aVnE:  # e o quarto elemento nao estiver na lista dos excluidos e a key ainda for True
                    key = False  # acaba o loop
                    for j in range(4):  # adiciona todos á lista dos excluidos, pois vao ser usados agora
                        excluidos.append(trevo[j])
                if trevo[i] in excluidos:
                    aVnE = True

    for i in range(4):
        if trevo[i] > 20:
            trevo[i] -= 20

    trevo.sort()

    for i in range(4):
        if trevo[i] > 20:
            trevo[i] += 20
        taboleiro[i][i] = trevo[i]

    return False

def turnoj(taboleiroj, excluidos, totaltrevos, key_inicial, table):
    print("JOGADOR")
    if key_inicial[1]:#se for a primeira jogada
        key_inicial[1] = primeira_rodada(taboleiroj, excluidos, totaltrevos)

    else:
        key = True
        while key:
            trevo = random.randint(1, totaltrevos)
            if trevo not in excluidos:
                key = False
                excluidos.append(trevo)

        key = True
        print("Trevo - ", trevo)

        while key:
            tabela = input("Queres colocar o trevo na table (S/N): ")
            if tabela == "S":
                table.append(trevo)
                key = False
            else:
                linha = int(input("Em que linha queres colocar o trevo: "))
                coluna = int(input("Em que coluna queres colocar o trevo: "))

                if taboleiroj[linha][coluna] == 0:
                    if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                        taboleiroj[linha][coluna] = trevo
                        key = False
                else:
                    if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                        table.append(taboleiroj[linha][coluna])
                        taboleiroj[linha][coluna] = trevo
                        key = False

    exibir_taboleiro(taboleiroj)

def turnob(taboleirob, excluidos,totaltrevos, key_inicial, table):
    print("BOT")

    if key_inicial[0]:#se for a primeira jogada
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
        print("Trevo - ", trevo)

        while key:
            """tabela = input("Queres colocar o trevo na table (S/N): ")
            if tabela == "S":
                key = False
                table.append(trevo)
            else:"""
            linha = random.randint(0, 3)
            coluna = random.randint(0, 3)
            if taboleirob[linha][coluna] == 0:
                if verificar_taboleiro(taboleirob, linha, coluna, trevo):
                    taboleirob[linha][coluna] = trevo
                    key = False
            else:
                if verificar_taboleiro(taboleirob, linha, coluna, trevo):
                    taboleirob[linha][coluna] = trevo
                    key = False
                    excluidos.append(trevo)

    exibir_taboleiro(taboleirob)


def opcaoA():

    B_preenhido = False #o bot ja preencheu o taboleiro?
    J_prenchido = False #o jogador ja preencheu o taboleiro?
    trevos = [] #todos os trevos vao parar aqui para que nao haja repeticao na geracao de trevos
    taboleiroJ = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #taboleiro do jogador
    taboleiroB = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] #taboleiro do bot
    table = []

    nome = input("\nNome do jogador: ")

    numero = random.randint(0, 1)  # quem comeca

    Comeco = [True, True]
    if numero == 0:
        print("Bot começa!")
        while (not B_preenhido and not J_prenchido) and not (len(trevos) == 40):#as condicoes de fim do jogo sao alguem ja ter preenchido todo o taboleiro ou os trevos esgotarem-se
            turnob(taboleiroB, trevos, 40, Comeco, table)
            turnoj(taboleiroJ, trevos, 40, Comeco, table)
            print(table)
            """a = int(input("cheat: "))
            if a == 0:
                B_preenhido = False
                J_prenchido = False"""
        # print(trevos)
    else:
        print("O %s começa!" % nome)
        while not (B_preenhido or not J_prenchido) and not (len(trevos) == 40):
            turnoj(taboleiroJ, trevos, 40, Comeco, table)
            turnob(taboleiroB, trevos, 40, Comeco, table)
            print(table)
            """a = int(input("cheat: "))
            if a == 0:
                B_preenhido = False
                J_prenchido = False"""
        # print(trevos)


def opcaoB():
    print("B")
def opcaoC():
    print("C")
def opcaoD():
    print("D")

key = True

while key:
    print(
        "A. Jogar uma Partida\nB. Carregar uma partida a partir de um ficheiro\nC. Apresentar uma descrição do jogo\nD. Sair da aplicação.")
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
