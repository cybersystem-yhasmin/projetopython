#3 atividade da estrutura de repeticao

numero = int(input("Digite um número (0 para parar): "))
quantidade = 0

while numero != 0:
    if numero < 0:
        quantidade += 1

    numero = int(input("Digite um número (0 para parar): "))

print("Quantidade de valores negativos:", quantidade)