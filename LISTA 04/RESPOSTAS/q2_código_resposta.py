N = int(input())
x = list(map(int, input().split()))
M = int(input())
Vida = 1
'''while len(x) > N:
    x.pop()
a = 0'''
soma = 0
for i in x:
    if i != 1:
        soma = i + soma
        if soma >= M:
            Vida = 0
    else:
        soma = 0

    

if Vida == 0:
    print('You Died')
else:
    print('Yes, you can')