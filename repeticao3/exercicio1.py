#1-Ler 80 números e ao final informar quantos número(s)
#  est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive) 

qtd = 0 

for contador in range (1,81):
    numero = int(input("Digite um numero: "))

    if numero >= 10 and numero <= 150:
        qtd += 1
print(" quantidade de numeros entre 10 e 150 é: ", qtd)



