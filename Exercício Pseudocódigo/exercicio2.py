#Antecessor e sucessor
#Leia um número inteiro e mostre seu antecessor e seu sucessor.

numero = int(input("Digite um número: "))

antecessor = numero - 1
sucessor = numero + 1

if numero > 0:
    print("Antecessor:", antecessor)
    print("Sucessor:", sucessor)
elif numero < 0:
    print("Antecessor:", antecessor)
    print("Sucessor:", sucessor)
else:
    print("O número é zero")
    print("Antecessor:", antecessor)
    print("Sucessor:", sucessor)