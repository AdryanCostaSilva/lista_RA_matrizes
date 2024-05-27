matriz = []
for i in range(10):
    matriz.append([])
    for j in range(10):
        matriz[i].append(0)
print(matriz)

for i in range(0, len(matriz)):
    for j in range(len(matriz[i])):
        if i < j:
            matriz[i][j] = 2*i + 7*j - 2
        elif i == j:
            matriz[i][j] = 3*i**2 - 1
        elif i > j:
            matriz[i][j] = 4*i**3 - 5*j**2 + 1

print("O modelo da matriz é este.")    
for linha in matriz:
    print(linha)