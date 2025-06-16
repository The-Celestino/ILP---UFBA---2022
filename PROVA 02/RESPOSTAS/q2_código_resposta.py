def obter_senha(matriz):
    n = len(matriz)
    
    while n > 1:
        diagonal_principal = sum(matriz[i][i] for i in range(n))
        diagonal_secundaria = sum(matriz[i][n-1-i] for i in range(n))
        
        linha_eliminar = diagonal_principal % n
        coluna_eliminar = diagonal_secundaria % n
        
        nova_matriz = []
        for i in range(n):
            if i != linha_eliminar:
                nova_linha = []
                for j in range(n):
                    if j != coluna_eliminar:
                        nova_linha.append(matriz[i][j])
                nova_matriz.append(nova_linha)
        
        matriz = nova_matriz
        n -= 1
    
    return matriz[0][0]

matriz = []
while True:
    try:
        linha = list(map(int, input().split()))
        matriz.append(linha)
    except EOFError:
        break

print(obter_senha(matriz))