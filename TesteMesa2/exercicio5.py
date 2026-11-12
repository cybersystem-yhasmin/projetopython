
producao = 120
meta = 100
falhas = 2
if producao >= meta and falhas == 0:
    status = "Lote aprovado"
else:
    status = "Lote em análise"

producao = producao - 15
falhas = falhas - 2
if producao >= meta and falhas == 0:
    status = "Lote aprovado"
else:
    status = "Lote reprovado"
print(producao)
print(falhas)
print(status)
