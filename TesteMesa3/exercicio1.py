temperatura = 95
ajustes = 0
alertas = 0

while temperatura < 150:
    temperatura = temperatura + 18
    ajustes = ajustes + 1

    if temperatura > 130:
        temperatura = temperatura - 12
        alertas = alertas + 1

    elif temperatura > 110:
        temperatura = temperatura - 5

    if ajustes % 2 == 0:
        temperatura = temperatura + 3

print(temperatura)
print(ajustes)
print(alertas)

