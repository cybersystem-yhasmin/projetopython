
producao = 150
falhas = 3
pontuacao = 0

if producao >= 150:
    pontuacao = pontuacao + 20

    if falhas <= 2:
        pontuacao = pontuacao + 30
    else:
        pontuacao = pontuacao + 10

producao = producao - 20
falhas = falhas - 1

if producao >= 130 and falhas < 3:
    pontuacao = pontuacao + 15
else:
    pontuacao = pontuacao - 5

print(producao)
print(falhas)
print(pontuacao)