def buscabinaria(lista, elemento):
    n = len(lista)
    esq = 0
    dir = n - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == elemento:
            break
        elif elemento < lista[meio]:
            dir = meio - 1
        else:
            esq = meio + 1
    if lista[meio] == elemento:#achou o elemento que quer
        print("Geral")
    else:
        print('Proibido')

#ENTRADAS
N_Gerais = int(input())
Gerais = list(input().split())
N_Proibidos = int(input())
Proibidos = list(input().split())
N_Consultas = int(input())
Feitiços_Consultar = list(input().split())
for i in range(N_Consultas):
    buscabinaria(Gerais,Feitiços_Consultar[i])