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
    if trevo > 60:
        trevo_real = trevo - 60
    elif trevo > 40:
        trevo_real = trevo - 40
    elif trevo > 20:
        trevo_real = trevo - 20
    else:
        trevo_real = trevo

    for i in range(coluna):
        if taboleiro[linha][i] > 60:
            el_taboleiro = taboleiro[linha][i] - 60
        elif taboleiro[linha][i] > 40:
            el_taboleiro = taboleiro[linha][i] - 40
        elif taboleiro[linha][i] > 20:
            el_taboleiro = taboleiro[linha][i] - 20
        else:
            el_taboleiro = taboleiro[linha][i]
        if el_taboleiro > trevo_real:
            return False
        else:
            continue

    for j in range(linha):
        if  taboleiro[j][coluna] > 60:
            el_taboleiro = taboleiro[j][coluna] - 60
        elif  taboleiro[j][coluna] > 40:
            el_taboleiro = taboleiro[j][coluna] - 40
        elif  taboleiro[j][coluna] > 20:
            el_taboleiro = taboleiro[j][coluna] - 20
        else:
            el_taboleiro = taboleiro[j][coluna]
        if taboleiro[j][coluna] > trevo_real:
            return False
        else:
            continue
    return True


def turnoj(taboleiroj, excluidos):
    print("JOGADOR")
    key = True

    while key:
        trevo = random.randint(1, 80)
        if trevo not in excluidos:
            key = False
            excluidos.append(trevo)

    key = True
    print("Trevo - ", trevo)

    while key:
        linha = int(input("Em que linha queres colocar o trevo: "))
        coluna = int(input("Em que coluna queres colocar o trevo: "))

        if taboleiroj[linha][coluna] == 0:
            if verificar_taboleiro(taboleiroj, linha, coluna, trevo):
                taboleiroj[linha][coluna] = trevo
                key = False

    exibir_taboleiro(taboleiroj)

def turnob(taboleirob, excluidos):
    print("BOT")
    key = True

    while key:
        trevo = random.randint(1, 80)
        if trevo not in excluidos:
            key = False
            excluidos.append(trevo)

    key = True
    print("Trevo - ", trevo)

    while key:
        linha = random.randint(0, 3)
        coluna = random.randint(0, 3)
        if taboleirob[linha][coluna] == 0:
            if verificar_taboleiro(taboleirob, linha, coluna, trevo):
                taboleirob[linha][coluna] = trevo
                key = False

    exibir_taboleiro(taboleirob)


def opcaoA():
    B_preenhido = True
    J_prenchido = True
    trevos = []
    taboleiroJ = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    taboleiroB = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    nome = input("\nNome do jogador: ")

    numero = random.randint(0, 1)  # quem comeca

    print(taboleiroJ)
    if numero == 0:
        print("Bot começa!")
        while B_preenhido or J_prenchido:
            turnob(taboleiroB, trevos)
            turnoj(taboleiroJ, trevos)

            a = int(input("cheat: "))
            if a == 0:
                B_preenhido = False
                J_prenchido = False
        # print(trevos)
    else:
        print("O %s começa!" % nome)
        while B_preenhido or J_prenchido:
            turnoj(taboleiroJ, trevos)
            turnob(taboleiroB, trevos)

            a = int(input("cheat: "))
            if a == 0:
                B_preenhido = False
                J_prenchido = False
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
