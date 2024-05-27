from random import randint
from segundoex import imprimir_matriz
from terceiroex import soma_pares_matriz
from quartoex import soma_coluna
from quintoex import maior_num_linha

def linha():
    print("=" * 40)
def matriz_n_aleatorios(quantlinhas, quantcolunas):
    matriz = []
    for i in range(0, quantlinhas):
        matriz.append([])
    for i in range(0, quantlinhas):
        for j in range(0, quantcolunas):
            matriz[i].append(randint(1,20))
    return matriz


quantidadelinhas = int(input("Informe a quantidade de linhas (i):\n>>>"))
quantidadecolunas = int(input("Informe a quantidade de colunas (j):\n>>>"))

#1
matriz = matriz_n_aleatorios(quantidadelinhas, quantidadecolunas)

#2
imprimir_matriz(matriz)

print("\n")

#3
linha()
somapares = soma_pares_matriz(matriz)
print(f"A soma dos números pares da matriz é {somapares}")
linha()

#4
linha()
somacoluna = soma_coluna(matriz)
print(f"A soma da coluna informada é {somacoluna}")
linha()

#5
linha()
maiorlinha = maior_num_linha(matriz)
print(f"O maior número da linha informada foi {maiorlinha}")
linha()
