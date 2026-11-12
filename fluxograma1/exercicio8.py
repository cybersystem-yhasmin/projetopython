#8- A concessionária de veículos “CARANGO” está vendendo os seus veículos com desconto. 
#Faça um fluxograma que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente. 
#O desconto deverá ser calculado sobre o valor do veículo de acordo com o combustível 
#(álcool – 25%, gasolina – 21% ou diesel –14%). Com valor do veículo zero encerra entrada de dados.
# Informe total de desconto e total pago pelos clientes.
total_desconto = 0
total_pago = 0

for contador in range(100):

    valor = float(input("Digite o valor do veículo (0 para encerrar): R$ "))

    if valor == 0:
        break

    combustivel = input("Digite o combustível (A - Álcool, G - Gasolina, D - Diesel): ")

    if combustivel == "A":
        desconto = valor * 0.25

    elif combustivel == "G":
        desconto = valor * 0.21

    elif combustivel == "D":
        desconto = valor * 0.14

    else:
        print("Combustível inválido!")
        continue

    valor_final = valor - desconto

    total_desconto = total_desconto + desconto
    total_pago = total_pago + valor_final

    print("Desconto: R$", round(desconto, 2))
    print("Valor a pagar: R$", round(valor_final, 2))

print("Total de descontos: R$", round(total_desconto, 2))
print("Total pago: R$", round(total_pago, 2))