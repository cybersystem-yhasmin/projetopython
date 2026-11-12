#Minutos para segundos
#Leia uma quantidade de minutos e transforme em segundos

minutos = int(input("Digite os minutos: "))

while minutos < 0:
    print("Valor inválido!")
    minutos = int(input("Digite novamente: "))

segundos = minutos * 60

print("Segundos:", segundos)