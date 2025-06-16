N , M = map(int, input().split())

matriz = []
for i in range (0, N):
    linhas = list(map(int, input().split()))
    matriz.append(linhas)
somatorio = 0
for j in range(0, M):
    soma = 0
    contador = 0
    L,C = map(int, input().split())
    
    for k in range(L, -1, -1):
         if matriz[L][C] != matriz[k][C]:
            soma = 1
            contador= soma + contador
            if contador <= 1:
             matriz[k][C] = 0
    somatorio = somatorio + soma                        
              
print(somatorio)


