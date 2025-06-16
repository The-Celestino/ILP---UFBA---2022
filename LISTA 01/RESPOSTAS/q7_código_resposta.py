
N = input()
N = int(N)

H = N//3600
resto = N % 3600
M = resto // 60
S = resto % 60

print(f'{H}h {M}m {S}s')