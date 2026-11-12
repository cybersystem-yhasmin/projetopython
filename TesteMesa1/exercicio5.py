
carga = 100
ciclo = 0

while carga > 30:
    ciclo = ciclo + 1

    if ciclo <= 3:
        carga = carga - 8
    else:
        carga = carga - 15

    print(ciclo, carga)

print("Carga final:", carga)
print("Ciclos executados:", ciclo)