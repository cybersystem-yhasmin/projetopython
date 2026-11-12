#4. Maior entre dois números
#Leia dois números.
#Informe qual deles é maior.
#Considere também a possibilidade de serem iguais.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O primeiro é maior")
elif numero2 > numero1:
    print("O segundo é maior")
else:
    print("Os números são iguais")