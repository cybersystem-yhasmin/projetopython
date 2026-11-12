p = int(input("Digite a pontuação: "))

if p <= 49 and p >= 0:
    print("Insatisfatório")
elif p <= 69 and p >= 50:
    print("Regular")
elif p <= 89 and p >= 70:
    print("Bom")
elif p <= 100 and p >= 90:
    print("Excelente")
else:
    print("Pontuação inválida")