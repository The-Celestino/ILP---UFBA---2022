#Entrada
v = []
N = int(input())
for i in range (N):
    numero, nome = input().split()
    v.append({"nome" : nome, "numero": numero })
#Ordenação
for inicio in range(1, N):
   i = inicio
   while i >= 1 and  v[i]["nome"] < v[i-1]["nome"]:
       v[i], v[i-1] = v[i-1], v[i]
       i -= 1
#Saida
for aluno in v:
    print(aluno["nome"], aluno["numero"])