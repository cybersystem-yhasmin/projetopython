#9 atividade da estrutura de repeticao

import random

numero = random.randint(1, 50)
tentativas = 0

print("Adivinhe o número entre 1 e 50!")

while tentativas < 5:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite < numero:
        print("O número sorteado é MAIOR!")
    elif palpite > numero:
        print("O número sorteado é MENOR!")
    else:
        print("Parabéns! Você acertou!")
        break

if palpite != numero:
    print("Suas tentativas acabaram!")
    print("O número sorteado era:", numero)