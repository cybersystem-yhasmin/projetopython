#Feita uma pesquisa em 12 cidades para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#- código da cidade
#- número de veículos de passeio
#- número de acidentes de trânsito com vítimas
#Deseja-se saber:
#a) o maior e o menor índice de acidentes de trânsito e a que cidades/estado
#pertencem
#b) qual a média de veículos nas cidades brasileiras (total / por state)
#c) qual a média de acidentes com vítimas nas cidades de Santa Catarina e o
#total por state.

contador = 0

total_veiculos = 0
veiculos_sc = 0
veiculos_rs = 0
veiculos_pr = 0

acidentes_sc = 0
acidentes_rs = 0
acidentes_pr = 0

maior = 0
menor = 999999

while contador < 12:

    codigo = int(input("Digite o código da cidade: "))
    veiculos = int(input("Digite o número de veículos: "))
    acidentes = int(input("Digite o número de acidentes: "))

    indice = acidentes / veiculos * 100

    if indice > maior:
        maior = indice
        cod_maior = codigo

    if indice < menor:
        menor = indice
        cod_menor = codigo

    total_veiculos += veiculos

    if codigo // 10 == 1:
        veiculos_sc += veiculos
        acidentes_sc += acidentes

    elif codigo // 10 == 2:
        veiculos_rs += veiculos
        acidentes_rs += acidentes

    elif codigo // 10 == 3:
        veiculos_pr += veiculos
        acidentes_pr += acidentes

    contador += 1

print("\nMAIOR ÍNDICE:", maior, "Código:", cod_maior)
print("MENOR ÍNDICE:", menor, "Código:", cod_menor)

print("Média geral de veículos:", total_veiculos / 12)

print("Média de veículos SC:", veiculos_sc / 4)
print("Média de veículos RS:", veiculos_rs / 4)
print("Média de veículos PR:", veiculos_pr / 4)

print("Média de acidentes SC:", acidentes_sc / 4)

print("Total de acidentes SC:", acidentes_sc)
print("Total de acidentes RS:", acidentes_rs)
print("Total de acidentes PR:", acidentes_pr)