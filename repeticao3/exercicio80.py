valor = float(input("Digite o valor da dívida: "))

ciclo = 0

print("Valor da Dívida - Valor dos Juros - Qtd Parcelas - Valor da Parcela")

while ciclo < 5:

    if ciclo == 0:
        juros = 0
        parcelas = 1
    elif ciclo == 1:
        juros = 0.10
        parcelas = 3
    elif ciclo == 2:
        juros = 0.15
        parcelas = 6
    elif ciclo == 3:
        juros = 0.20
        parcelas = 9
    else:
        juros = 0.25
        parcelas = 12

    valorJuros = valor * juros
    valorTotal = valor + valorJuros
    valorParcela = valorTotal / parcelas

    print(f"R$ {valorTotal:.2f} - R$ {valorJuros:.2f} - {parcelas} - R$ {valorParcela:.2f}")

    ciclo = ciclo + 1