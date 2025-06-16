
def protocolo1(lista):
    nk = len(lista)
    n = len(lista)
    a = 0
    primeiro = lista[0]
    for i in range(0,len(lista)-1):
        X = (primeiro+a)%(nk)
        a = lista[X]
        primeiro = 0
        del lista[X]
        nk = (n - i) - 1 #Mds eu tava fazendo n - (k-1)
    print(*lista)

lista = list(map(int,input().split()))
protocolo1(lista)