lista_coluna = []
lista_linha = []
linha = 2
coluna = 0
taboleiro1 = [[22, 24, 3, 0], [0, 33, 0, 0], [16, 36, 37, 0], [0, 0, 0, 17], [16]]
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