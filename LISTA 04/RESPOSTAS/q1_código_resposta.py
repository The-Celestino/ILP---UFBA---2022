S , N = map(int, input().split()) 
Pedras = [0]*N
a =0
for i in range (0,S):
    Pulos = int(input())
    for j in range(0,N, Pulos):
        Pedras[0+j] = 1                  
b = 0 
while b != len(Pedras):      
   print(Pedras[0+b], end=" ")
   b +=1 
