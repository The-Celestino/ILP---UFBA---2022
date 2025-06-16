
T,X = input().split()
T= int(T)
X = int(X)

r = X % T
if r >=0:
    print(r)
elif r <= 0:
    r = T - abs(r)
    print(r)