def soma_coluna(matriz):
    while True:
        contcoluna = 0
        colunasum = int(input("Informe a coluna a ser somada: "))
        for i in range(0, len(matriz[0])):
            contcoluna += 1
        if 0 < colunasum <= contcoluna:
            soma = 0
            for i in matriz:
                soma += i[colunasum - 1]
            return soma
        else:
            print("Esta coluna não existe! Tente novamente.")
            continue