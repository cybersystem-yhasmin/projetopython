
alertas = 0
soma = 0

for leitura in range(1, 6):
    temperatura = 20 + leitura * 7
    soma = soma + temperatura

    if temperatura > 45:
        alertas = alertas + 1
        soma = soma - 5
    elif temperatura >= 35:
        soma = soma + 3

print(soma)
print(alertas)
