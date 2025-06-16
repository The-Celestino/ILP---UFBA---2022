N = int(input()) #Quantidade de linhas
matriz = []
somadearvores = 0
soma = 0
for j in range(0,N): #preenchimento da matriz
    linhas =  list(map(int, input().split()))
    matriz.append(linhas)
QC = int(input()) #Quantidade de coordenadas
for i in range (0, QC): #loop para verificar o numero  igual a quantidade de coordenadas
    X , Y = map(int, input().split())
    soma = matriz[X][Y]
    somadearvores = somadearvores + soma

print(somadearvores)