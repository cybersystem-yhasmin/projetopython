#Dobro e triplo
#Leia um número e mostre o dobro e o triplo.

numero = int(input("Digite um número: "))

if numero > 0:
    print("Dobro:", numero * 2)
    print("Triplo:", numero * 3)
elif numero < 0:
    print("Dobro:", numero * 2)
    print("Triplo:", numero * 3)
else:
    print("O número é zero")
