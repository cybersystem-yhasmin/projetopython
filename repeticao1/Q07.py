#7 atividade da estrutura de repeticao

somaPositivos = 0
quantidadePositivos = 0

numero = float(input("Digite um número ou um negativo para encerrar: "))

while numero >= 0:
    if numero > 0:
        somaPositivos += numero
        quantidadePositivos += 1
    numero = float(input("Digite um número ou um negativo para encerrar: "))

if quantidadePositivos > 0:
    media = somaPositivos / quantidadePositivos
    print("A média dos números positivos digitados é:", media)
else:
    print("Nenhum número positivo foi digitado.")

   