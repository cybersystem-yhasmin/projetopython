#8 atividade da estrutura de repeticao

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("O número deve ser positivo.")
else:
    if numero % 2 != 0:
        numero -= 1

    print("Números pares em ordem decrescente:")
    while numero >= 0:
        print(numero)
        numero -= 2