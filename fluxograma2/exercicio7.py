canal = int(input("Digite o canal (0 para parar): "))

c4 = 0
c5 = 0
c7 = 0
c12 = 0
total = 0

while canal != 0:
    pessoas = int(input("Quantidade de pessoas assistindo: "))

    total += pessoas

    if canal == 4:
        c4 += pessoas
    elif canal == 5:
        c5 += pessoas
    elif canal == 7:
        c7 += pessoas
    elif canal == 12:
        c12 += pessoas

    canal = int(input("Digite o canal (0 para parar): "))

if total > 0:
    print("Audiência canal 4:", c4 / total * 100, "%")
    print("Audiência canal 5:", c5 / total * 100, "%")
    print("Audiência canal 7:", c7 / total * 100, "%")
    print("Audiência canal 12:", c12 / total * 100, "%")
else:
    print("Nenhuma pessoa participou da pesquisa.")