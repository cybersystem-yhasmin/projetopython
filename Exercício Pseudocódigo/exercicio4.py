#Área do retângulo
#Leia a largura e a altura de um retângulo e calcule sua área.

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

area = largura * altura

if area > 0:
    print("Área do retângulo:", area)
else:
    print("Medidas inválidas")