total = 0
cont = 0
maior = 0

for i in range(10):
    venda = float(input("Valor da venda: "))

    total += venda

    if venda > 500:
        cont += 1

    if venda > maior:
        maior = venda

print("Total vendido:", total)
print("Média:", total / 10)
print("Vendas acima de 500:", cont)
print("Maior venda:", maior)