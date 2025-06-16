matriz = []
N = 8
K0 = 0
K1 = 0
K2 = 0
K3 = 0
for i in range (0, N):
    linhas = list(map(int, input().split()))
    matriz.append(linhas)
x , y = map(int, input().split())

matriz[x][y] = 1
for j in range(x, -1, -1): #varredura pra cima ok 
    if matriz[j][y]== 1:
         break
    elif matriz[j][y]==2:
         K0 = 1
         matriz[j][y] = 0
         break
for k in range(x+1, N):#varredura pra baixo ok
     if matriz[k][y]== 1:
         break
     elif matriz[k][y]==2:
         K1 = 1
         matriz[k][y] = 0
         break
for l in range(x+1, N):#varredura direita ok
     if matriz[x][l] == 1:
         break
     elif matriz[x][l] == 2:
         K2 = 1
         matriz[x][l] = 0
         break
for m in range(x-1,-1, -1):#varredura esquerda ok 
     if matriz[x][m] == 1:
         break
     elif matriz[x][m] == 2:
         K3 = 1
         matriz[x][m] = 0
Somatorio = K0+ K1 + K2 + K3
print(Somatorio)