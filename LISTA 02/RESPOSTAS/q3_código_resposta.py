SC, MM, CK = map(int, input().split())

if SC < 30:
    S = 30 - SC 
    M = 6 - MM
    C = 3 - CK
    print(f'{S} {M} {C}')
else:
    print("PROXIMO MUNDO")