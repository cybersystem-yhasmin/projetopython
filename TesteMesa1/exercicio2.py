
temperatura = 30
ciclo = 0

while temperatura < 70:
    ciclo = ciclo + 1

    if temperatura < 45:
        temperatura = temperatura + 8
    else:
        temperatura = temperatura + 12

    print(ciclo, temperatura)

print("Temperatura final:", temperatura)
print("Ciclos:", ciclo)