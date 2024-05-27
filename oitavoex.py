
jogovelha = [["1A","2A","3A"],["1B","2B","3B"],["1C","2C","3C"]]

while True:
    cont = 0
    while True:
        cont += 1
        if cont % 2 == 0:
            saida = "X"
        else:
            saida = "O"
        for i in jogovelha:
            print(i)
        print("=" * 30)
        jogada = str(input(f"Vez do ({saida})\n Escolha a jogada: "))
        if jogada == "1A":
            if jogovelha[0][0] != "1A":
                print("Esta posição já foi escolhida!")
                cont -= 1
                continue
            else:
                jogovelha[0][0] = saida
        elif jogada == "2A":
            if jogovelha[0][1] != "2A":
                print("Esta posição já foi escolhida!")
                cont -= 1
                continue
            else:
                jogovelha[0][1] = saida
        elif jogada == "3A":
            if jogovelha[0][2] != "3A":
                print("Esta posição já foi escolhida!")
                cont -= 1
                continue
            else:
                jogovelha[0][2] = saida
        elif jogada == "1B":
            if jogovelha[1][0] != "1B":
                print("Esta posição já foi escolhida!")
                cont -= 1
                continue
            else:
                jogovelha[1][0] = saida
        elif jogada == "2B":
            if jogovelha[1][1] != "2B":
                print("Esta posição já foi escolhida!")
                cont -= 1
                continue
            else:
                jogovelha[1][1] = saida
        elif jogada == "3B":
            if jogovelha[1][2] != "3B":
                print("Esta posição já foi escolhida!")
                cont -= 1
                continue
            else:
                jogovelha[1][2] = saida
        elif jogada == "1C":
            if jogovelha[2][0] != "1C":
                print("Esta posição já foi escolhida!")
                cont -= 1
                continue
            else:
                jogovelha[2][0] = saida
        elif jogada == "2C":
            if jogovelha[2][1] != "2C":
                print("Esta posição já foi escolhida!")
                cont -= 1
                continue
            else:
                jogovelha[2][1] = saida
        elif jogada == "3C":
            if jogovelha[2][2] != "3C":
                print("Esta posição já foi escolhida!")
                cont -= 1
                continue
            else:
                jogovelha[2][2] = saida

        if jogovelha[0][0] == jogovelha[0][1] == jogovelha[0][2]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[1][0] == jogovelha[1][1] == jogovelha[1][2]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[2][0] == jogovelha[2][1] == jogovelha[2][2]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[0][0] == jogovelha[1][0] == jogovelha[2][0]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            print("=" * 30)
            break
        elif jogovelha[0][1] == jogovelha[1][1] == jogovelha[2][1]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[0][2] == jogovelha[1][2] == jogovelha[2][2]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[0][0] == jogovelha[1][1] == jogovelha[2][2]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        elif jogovelha[0][2] == jogovelha[1][1] == jogovelha[2][0]:
            print(f"({saida}) VENCEU!!!")
            print("=" * 30)
            break
        else:
            if cont == 9:
                print("=" * 30)
                print("EMPATE!!!")
                print("=" * 30)
                break
    while True:
        resp = str(input("Deseja jogar denovo? (S/N)"))
        print("=" * 30)
        if resp not in "SsNn":
            print("Digito inválido! Tente novamente.")
            continue
        elif resp in "Ss":
            jogovelha.clear()
            jogovelha = [["1A","2A","3A"],["1B","2B","3B"],["1C","2C","3C"]]
            break
        elif resp in "Nn":
            break
    if resp in "Nn":
        break
print("FIM DE JOGO!!!")