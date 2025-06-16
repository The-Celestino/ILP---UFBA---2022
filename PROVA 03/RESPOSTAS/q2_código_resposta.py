def contar_clientes_consumo(n, m, consumos, consultas):
    resultado = []

    # Ordenar a lista de consumos em ordem crescente

    for valor, criterio in consultas:
        contador = 0

        if criterio == 'leq':
            contador = busca_binaria_menor_igual(consumos, valor)
        elif criterio == 'geq':
            contador = m - busca_binaria_menor_igual(consumos, valor - 1)

        resultado.append(contador)

    return resultado


def busca_binaria_menor_igual(lista, valor):
    esquerda = 0
    direita = len(lista) - 1
    indice = -1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] <= valor:
            indice = meio
            esquerda = meio + 1
        else:
            direita = meio - 1

    return indice + 1

def ordenacao_inserc (x) :#X é  a lista que vou ordenar

     n = len (x)
     for i in range (1,n) :
         v = x[ i ]
         j=i - 1
         while j >= 0 and v < x[ j ]: 
             x[ j +1] = x[ j ]
             j=j - 1
         x[j +1] = v
     return x

n, m = map(int, input().split())
consumos = list(map(int, input().split()))
ordenacao_inserc(consumos)
consultas = []
for _ in range(n):
    valor, criterio = input().split()
    consultas.append((int(valor), criterio))

contador_cliente = contar_clientes_consumo(n, m, consumos, consultas)

for contador in contador_cliente:
    print(contador)