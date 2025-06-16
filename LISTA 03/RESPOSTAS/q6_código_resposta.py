logico = True
cor1 = str(input())
while logico == True:
    cor2 = str(input())

    if cor2 == "branco":
        logico = False
    elif cor2 == "preto":
        print("Game Over")
        logico = False
    elif cor1 == cor2:
        print(cor1)
    else:
        cor1 = cor1 + cor2
        logico = True

        if cor1 == "vermelhoamarelo" or cor1 == "amarelovermelho":
            print("laranja")
            cor1 = cor2
        elif cor1 == "vermelhoazul" or cor1 == "azulvermelho":
            print("roxo")
            cor1 = cor2
        elif cor1 == "vermelhoverde" or cor1 == "verdevermelho":
            print("marrom")
            cor1 = cor2
        elif cor1 == "amareloazul" or cor1 == "azulamarelo":
            print("verde")
            cor1 = cor2
        elif cor1 == "amareloverde" or cor1 == "verdeamarelo":
            print("lima")
            cor1 = cor2
        elif cor1 == "azulverde" or cor1 == "verdeazul":
            print("ciano")
            cor1 = cor2