
producao = 0
ciclo = 0

while producao < 150:
    ciclo = ciclo + 1

    if ciclo <= 2:
        quantidade = 20
    elif ciclo <= 4:
        quantidade = 30
    else:
        quantidade = 40

    producao = producao + quantidade

    print(ciclo, quantidade, producao)

print("Produção total:", producao)
print("Ciclos executados:", ciclo)