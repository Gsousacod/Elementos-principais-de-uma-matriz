matriz =  [ [0,0,0], [0,0,0], [0,0,0]]
lista_diagonalp = []
for i in range (0,3):
    for j in range(0,3):
        matriz[i][j] = int(input("Digite um elemento:"))
        if(i==j):
                lista_diagonalp.append(matriz[i][j])
                
print(matriz)
print('<<>>'*5)                
for i in range (0,3):
        for j in range(0,3):
                print(f'[{matriz[i] [j] :^5}]', end = "")
        print()
print('<<>>'*5)
print(lista_diagonalp)
print('<<>>'*5)

