maior = 0
menor = 0

for i in range(10):
    idade = int(input("Digite a idade: "))

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print("Maiores:", maior)
print("Menores:", menor)