#4- Uma loja utiliza o código 1 para transação à vista e 2 para transação a prazo.
#Faça um programa que receba o código e o valor de 15 transações. Calcule e mostre:
#O valor total das compras à vista
# O valor total as compras a prazo
#O valor total das compras efetuadas
#O valor da primeira prestação das compras a prazo, sabendo se que essas serão pagas em três vezes

valortotalVista = 0
valortotalPrazo = 0
valortotalCompras = 0

for contador in range(1, 16):

    codigo = int(input("digite o codigo da transação (1- à vista, 2- a prazo): "))
    valor = float(input("Digite o valor da transação:"))

    if codigo == 1:
        valortotalVista += valor
    elif codigo == 2:
        valortotalPrazo += valor

valortotalCompras = valortotalVista + valortotalPrazo
valor_primeira_prestacao = valortotalPrazo / 3

print(f"Valor total das compras à vista: R$ {valortotalVista:.2f}")
print(f"Valor total das compras a prazo: R$ {valortotalPrazo:.2f}")
print(f"Valor total das compras efetuadas: R$ {valortotalCompras:.2f}")
print(f"Valor da primeira prestação das compras a prazo: R$ {valor_primeira_prestacao:.2f}")