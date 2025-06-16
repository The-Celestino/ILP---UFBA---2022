def buscabinaria(v,elem):
    n = len(v)
    esq = 0
    dir = n - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if v[meio] == elem:
            break
        elif elem < v[meio]:
            dir = meio - 1
        else:
            esq = meio + 1
    if v[meio] == elem:
        print(meio)
    else:
        print(-1)
nc = int(input())
for dentes in range(0,nc):
    tamanholista = int(input())
    listaA = list(map(int,input().split()))
    elem = int(input())
    buscabinaria(listaA,elem)