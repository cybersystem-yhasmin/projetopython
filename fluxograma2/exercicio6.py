pos = 0
neg = 0
pares = 0
impares = 0

num = int(input("Digite um número (0 para parar): "))

while num != 0:

    if num > 0:
        pos += num
    else:
        neg += num

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    num = int(input("Digite um número (0 para parar): "))

print("Soma dos positivos:", pos)
print("Soma dos negativos:", neg)
print("Soma das duas somas:", pos + neg)
print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)