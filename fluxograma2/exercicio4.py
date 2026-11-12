j1 = 0
j2 = 0

while (j1 < 21 or j1 - j2 < 2) and (j2 < 21 or j2 - j1 < 2):
    ponto = int(input("Quem fez o ponto? (1 ou 2): "))

    if ponto == 1:
        j1 += 1
    elif ponto == 2:
        j2 += 1
    else:
        print("Código inválido!")

if j1 > j2:
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")

print("Pontos do jogador 1:", j1)
print("Pontos do jogador 2:", j2)