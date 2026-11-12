
estoque = 40
ciclo = 0

while ciclo < 5:
    ciclo = ciclo + 1
    entrada = 15
    saida = 9

    estoque = estoque + entrada
    estoque = estoque - saida

    print(ciclo, estoque)

print("Estoque final:", estoque)