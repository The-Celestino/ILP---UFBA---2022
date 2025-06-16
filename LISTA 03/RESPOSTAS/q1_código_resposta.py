n = 0
while True:
 HF, HDF, HA = map(str, input().split())
 if HF == "NAO" and HDF == "SIM" and HA == "NAO":
  n = 1
 if HF == "FIM" and HDF == "FIM" and HA == "FIM":
   break
if n == 1:
    print('VITORIA')  
else:
    print('DERROTA')