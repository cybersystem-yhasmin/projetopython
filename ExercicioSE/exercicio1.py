#1. Positivo ou negativo
#Leia um número.
#Informe se ele é positivo ou negativo.

numero = int(input("Digite um número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")