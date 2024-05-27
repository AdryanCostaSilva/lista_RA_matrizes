def maior_num_linha(matriz):
    while True:
        linha = int(input("Escolha uma linha para ver o maior valor nela: "))
        contlinha = 0
        for i in matriz:
            contlinha += 1
        if 0 < linha <= contlinha:
            maior = matriz[linha - 1][0]
            for i in matriz[linha - 1]:
                if i > maior:
                    maior = i
            return maior
        else:
            print("Esta linha não existe! Tente novamente!")
            continue