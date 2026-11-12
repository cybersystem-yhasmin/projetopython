
producao = 0
pontos = 10
ciclo = 1
falhas = 0
while ciclo <= 4:
    producao = producao + ciclo * 10
    if producao % 20 == 0:
        pontos = pontos + 15
    else:
        pontos = pontos + 5
    if pontos >= 40:
        falhas = falhas + 1
        pontos = pontos - 10
    ciclo = ciclo + 1
if producao >= 90 and falhas <= 2:
    status = "Lote aprovado"
else:
    status = "Lote reprovado"
print(producao)
print(pontos)
print(falhas)
print(ciclo)