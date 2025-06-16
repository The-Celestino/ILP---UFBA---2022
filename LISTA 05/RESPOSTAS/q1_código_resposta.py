# ORDENAÇÃO
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
# BUSCA BINARIA:
def buscabinaria(banco, M1):
    n = len(banco)
    esq = 0
    dir = n - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if banco[meio][0] == M1:
            break
        elif M1 < banco[meio][0]:
            dir = meio - 1
        else:
            esq = meio + 1
    if banco[meio][0] == M1:
        print(f'{banco[meio][1]}: {banco[meio][2]}')
    else:
        print('Aluno nao encontrado')
# INICIO
N = int(input())  # Número de estudantes do sistema
banco = []
for i in range(N):
    M0, Tele, Nome = input().split()
    M0 = int(M0)
    Tele = int(Tele)
    banco.append([M0, Nome, Tele])
ordenacao_inserc(banco) 
C = int(input())  # número de consultas
for j in range(C):
    M1 = int(input())  # número de matricula sendo consultado
    buscabinaria(banco, M1)