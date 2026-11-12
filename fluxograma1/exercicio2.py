#2- Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool: 4,40 o litro
#Até 20 litros: desconto de 3% por litro
#Acima de 20 litros: Desconto de 5% por litro 99.
#Gasolina: 6,09 o litro
#Até 20 litros: desconto de 4% por litro
#Acima de 20 litros, desconto de 6% por litro
#Faça um fluxograma que leia o número de litros vendidos, o tipo de 
# combustível, calcule e imprima o valor a ser pago pelo cliente.

litros = float(input("Digite a quantidade de litros: "))

combustivel = input("Digite A para álcool ou G para gasolina: ")

while combustivel != "A" and combustivel != "G":
    print("Combustível inválido!")
    combustivel = input("Digite A para álcool ou G para gasolina: ")

if combustivel == "A":
    preco = 4.40

    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

else:
    preco = 6.09

    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06

total = litros * preco * (1 - desconto)

print("Valor a pagar: R$", round(total, 2))