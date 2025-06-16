
notas = []
while True:
    notas.clear()
    total = 0
    while True:
        n = input()
        notas.append(n)
        if n == 'FIM':
            notas.pop()
            notas[:] = list(map(int, notas)) #converter a lista de strings em nums
            break
    if len(notas) > 2:
        menor = min(notas)
        maior = max(notas)
        notas.remove(menor)
        notas.remove(maior)
        for i in notas:
            total = total + i
        media1 = total // (len(notas))
        print(media1)
    elif len(notas) == 2:
        for i in notas:
         total= total + i
        media2 = total // len(notas)
        print(media2)
    elif len(notas) == 1:
        print(notas[0])
    else:
        break
    