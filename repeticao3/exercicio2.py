#Escrever um algoritmo que leia o nome e o sexo 
# de 56 pessoas e informe o nome e se ela é homem ou mulher.
#  No final informe total de homens e de mulheres. 

total_homens = 0
total_mulheres = 0

for contador in range(1, 57):
    nome = input("Digite o nome da pessoa " + str(contador) + ": ")
    sexo = input("Digite o sexo de " + nome + " (M/F): ")

    if sexo == 'M':
        print(nome + " é homem.\n")
        total_homens += 1
    elif sexo == 'F':
        print(nome + " é mulher.\n")
        total_mulheres += 1
    else:
        print("Opção de sexo inválida.\n")

print("\n RESUMO FINAL")
print("Total de homens: " + str(total_homens))
print("Total de mulheres: " + str(total_mulheres))