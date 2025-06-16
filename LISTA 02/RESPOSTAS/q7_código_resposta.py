N1, N2, N3, N4,N5,N6 = map(int,input().split())

soma = (N1+N2+N3+N4+N5+N6)

if soma >= 250:
    print("S+")
elif  250 > soma >= 200:
    print("S")
elif 200 > soma >= 180:
    print("S-")
elif 180 > soma >= 150:
    print("A+")
elif 150 > soma >= 100:
    print("A")
elif 100 > soma >= 80:
    print("A-")
elif 80 > soma >= 60:
    print("B+")
elif 60 > soma >= 40:
    print("B")
else:
    print("B-")