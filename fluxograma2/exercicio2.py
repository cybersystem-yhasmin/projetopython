c1 = 0
c2 = 0
c3 = 0
c4 = 0

codigo = int(input("Digite o código (0 para sair): "))

while codigo != 0:

    if codigo == 1:
        print("Alimento não-perecível")
        c1 += 1

    elif codigo >= 2 and codigo <= 4:
        print("Alimento perecível")
        c2 += 1

    elif codigo == 5 or codigo == 6:
        print("Vestuário")
        c3 += 1

    elif codigo == 7:
        print("Higiene pessoal")
        c4 += 1

    elif codigo >= 8 and codigo <= 15:
        print("Limpeza e utensílios domésticos")
        c4 += 1

    else:
        print("Código inválido")

    codigo = int(input("Digite o código (0 para sair): "))

print("\n--- TOTAL DE PRODUTOS ---")
print("Alimento não-perecível:", c1)
print("Alimento perecível:", c2)
print("Vestuário:", c3)
print("Higiene pessoal:", c4)