N=int(input())
P=list(map(int, input().split()))

x = set()

for p in P:
    if p in x:
        print(p)
        break
    x.add(p)
else:
    print("-1")