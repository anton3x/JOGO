import random
def partida():
    nome = input("Nome do jogador: ")
    numero = random.randint(0, 1) #quem comeca
    if numero == 0:
        print("Bot começa!")
    else:
        print("O %s começa!" % (nome))

