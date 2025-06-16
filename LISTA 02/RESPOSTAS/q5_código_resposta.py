z, g = (input().split())
d, c = (input().split())
if z != d:
    print("Bloqueado")
else:
    if z == d and g != c:
        print("Driblado")
        print("...e o goleiro pega")
    elif z == d and g == c:
        print("Driblado")
        print("Gol")