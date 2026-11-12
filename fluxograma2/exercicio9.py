
for i in range(150):
    nome = input("Nome do cliente: ")
    compras = float(input("Valor das compras: "))

    if compras < 500000:
        bonus = compras * 0.10
    else:
        bonus = compras * 0.15

    print("Cliente:", nome)
    print("Bônus: R$", bonus)