N = int(input())
C= str(input())    
Codigo = list(C)
P = str(input())
Resultado = []
while len(Codigo) > N:
      Codigo.pop()
for i in P:
          for j in Codigo:
               if Codigo.count(j) == P.count(j):
                    if j == i and Resultado.count(j) < P.count(j):
                         Resultado.append(j)
if len(Resultado)== len(P):
     print("Palavra chave encontrada")
else:
     print("Nenhuma informacao util")
     