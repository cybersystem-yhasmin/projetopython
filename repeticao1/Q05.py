#5 atividade da estrutura de repeticao

soma = 0
quantidade = 0

num = int(input("Digite um número (0 para parar): "))

while num != 0:
    if num % 2 == 0:
        soma += num
        quantidade += 1

    num = int(input("Digite um número (0 para parar): "))

if quantidade > 0:
    media = soma / quantidade
    print("A média dos números pares é:", media)
else:
    print("Nenhum número par foi digitado.")