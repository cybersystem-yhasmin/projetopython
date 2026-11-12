#7- Crie um fluxograma que modele um programa de conversão de moedas. 
# O usuário deve fornecer um valor em real e selecionar para qual moeda deseja converter 
# (para dólar, euro ou libra). 
# O programa deve fazer a conversão usando taxas de câmbio fornecidas e exibir o valor convertido.

valor = float(input("Digite o valor em reais: R$ "))

print("Escolha a moeda para conversão:")
print("1 - Dólar")
print("2 - Euro")
print("3 - Libra")

opcao = int(input("Digite sua opção: "))

while opcao < 1 or opcao > 3:
    print("Opção inválida!")
    opcao = int(input("Escolha 1, 2 ou 3: "))

if opcao == 1:
    convertido = valor / 5.00
    print("Valor em dólar: US$", round(convertido, 2))

elif opcao == 2:
    convertido = valor / 5.50
    print("Valor em euro: €", round(convertido, 2))

elif opcao == 3:
    convertido = valor / 6.50
    print("Valor em libra: £", round(convertido, 2))