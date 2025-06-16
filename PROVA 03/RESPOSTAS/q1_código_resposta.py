def insert(lista, elemento) : #ALGORITMO DE ORDENAÇÃO slide
    for i in range(elemento,) :
        começo=i
        for j in range(i ,len(lista)):
            if lista[j] < lista[começo]:
                começo =j
        lista[i], lista[começo] = lista[começo], lista[i]
    
def insert2(lista, elemento) : #ALGORITMO DE ORDENAÇÃO slide
    for i in range(elemento) :
        começo=i
        for j in range(i ,len(lista)):
            if lista[j] > lista[começo]:
                começo =j
        lista[i], lista[começo] = lista[começo], lista[i]
    
k = int(input())
sequencia = list(map(int,input().split()))
a = len(sequencia)
insert(sequencia,k)
lista2 = sequencia[:k]#1 1 2
n = len(sequencia)-k
insert2(sequencia, k)
lista3 = sequencia[:k]# 10 43 100
lista4 = []
print(*lista3,*lista2)