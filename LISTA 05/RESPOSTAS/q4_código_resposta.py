def ordenacao_inserc (x) :
     n = len (x)
     for i in range (1,n) :
         v = x[ i ]
         j=i - 1
         while j >= 0 and v < x[ j ]: 
             x[ j +1] = x[ j ]
             j=j - 1
         x[j +1] = v
     return x

#ENTRADAS
N_Musicas = int(input())
banco = []
for i in range(N_Musicas):
    X = input()
    banco.append(X)
ordenacao_inserc(banco)

for j in banco:
    print(j)