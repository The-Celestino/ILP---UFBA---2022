N,Q = map(int,input().split())
i = 0
valor = Q
while i < N:
  valor = valor * 2
  i = i + 1
valor = valor - Q
print(valor)