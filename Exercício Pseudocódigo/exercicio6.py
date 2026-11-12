#Metros para centímetros
#Leia uma distância em metros e transforme em centímetros.

metros = float(input("Digite a distância em metros: "))

while metros < 0:
    print("Digite uma distância válida!")
    metros = float(input("Digite novamente: "))

centimetros = metros * 100

print("Centímetros:", centimetros)