tamanho = int(input())
matriz = []
for i in range (0, tamanho):
    linhas = list(map(int, input().split()))
    matriz.append(linhas)
h , r = map(int, input().split())
ac1 = 0
for j in matriz[h]:#harry linhas
    ac1 = ac1 + j   
conta = 0
ac2 = 0
for k in range (0,tamanho): #ron colunas
    conta = matriz[k][r]
    ac2 = ac2 + conta

if h < r or h == r:
    ac1 = ac1 - matriz[h][r]
elif h > r:
    ac2 = ac2 - matriz[h][r]

print('Harry', ac1)
print('Ron', ac2)