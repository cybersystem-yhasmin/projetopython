valor = float(input("Digite o valor do carro: R$ "))

print("\nQuantidade | Preço final | Valor da parcela")

print("À vista:", valor * 0.80)

for i in range(6, 61, 6):
    acrescimo = i / 2
    preco = valor * (1 + acrescimo / 100)
    parcela = preco / i

    print(i, "| R$", round(preco, 2), "| R$", round(parcela, 2))