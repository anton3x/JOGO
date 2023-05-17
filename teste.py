def bu():
    dicionario = {}
    with open("save.txt", "r") as f:
        linhas = f.readlines()
    i = 0
    for linha in linhas:
        nome, tabuleiro_str = linha.strip().split("/")
        if i == 0:
            dicionario["jogador1"] = [nome]
            i += 1
        elif i == 1:
            dicionario["jogador2"] = [nome]
            i += 1

        tabuleiro = eval(tabuleiro_str)
        dicionario[nome] = tabuleiro

    print(dicionario)

bu()