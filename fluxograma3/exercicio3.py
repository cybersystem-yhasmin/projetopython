soma = 0
cont = 0

idade = int(input("Digite a idade (0 para parar): "))

while idade > 0:
    soma += idade
    cont += 1
    idade = int(input("Digite a idade (0 para parar): "))

print("Pessoas cadastradas:", cont)

if cont > 0:
    print("Média das idades:", soma / cont)