
resultado = 0
contador = 0

for valor in range(3, 15, 3):
    contador = contador + 1
    if valor % 2 == 0:
        resultado = resultado + valor // 2
    else:
        resultado = resultado + valor * 2
    if contador >= 3:
        resultado = resultado - contador

print(contador)
print(resultado)