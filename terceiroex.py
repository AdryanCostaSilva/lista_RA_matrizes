def soma_pares_matriz(matriz):
    soma = 0
    for i in matriz:
        for j in i:
            if j % 2 == 0:
                soma += j
    return soma
