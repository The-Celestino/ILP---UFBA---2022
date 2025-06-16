T =  int(input())
a = False
while True:
 P = int(input())
 if P > T:
  a = True
 if P == 0:
  break
if a == True:
 print("ALARME")
else:
 print('O Havai pode dormir tranquilo')
  