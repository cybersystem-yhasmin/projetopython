
total = 0
contador = 0

for numero in range(4, 21, 4):
    contador = contador + 1
    if numero % 8 == 0:
        total = total + numero // 2
    else:
        total = total + numero * 2

    if contador % 2 == 0:
        total = total - 3

print(contador)
print(total)
