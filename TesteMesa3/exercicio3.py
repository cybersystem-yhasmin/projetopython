
producao = 60
falhas = 0
pontos = 50

for ciclo in range(1, 5):
    producao = producao + ciclo * 8

    if producao >= 80 and falhas <= 1:
        pontos = pontos + 15

    elif producao >= 70 or falhas == 2:
        pontos = pontos + 8

    else:
        pontos = pontos - 5

    if ciclo % 2 == 0:
        falhas = falhas + 1

    if pontos > 80:
        pontos = pontos - 12

print(producao)
print(falhas)
print(pontos)