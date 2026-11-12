#Quilômetros para metros
#Leia uma distância em quilômetros e transforme em metros.

quilometros = float(input("Digite os quilômetros: "))

metros = quilometros * 1000

if quilometros > 0:
    print("Metros:", metros)
elif quilometros == 0:
    print("Distância igual a zero")
else:
    print("Distância inválida")