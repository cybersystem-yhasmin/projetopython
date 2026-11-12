estoque = 200
reposicoes = 0
vendas = 0

for dia in range(1, 6):
    vendas = dia * 17
    estoque = estoque - vendas

    if estoque < 100:
        estoque = estoque + 50
        reposicoes = reposicoes + 1

    if estoque > 180:
        estoque = estoque - 15

print(estoque)
print(reposicoes)
print(vendas)