#11- Uma pesquisa de satisfação foi realizada com 40 clientes de uma loja,
#  pedindo que avaliassem o atendimento como: péssimo = 1, regular = 2, bom = 3,
#  excelente = 4. Faça um programa que leia a avaliação e a idade dos clientes e exiba:
#A média de idade dos clientes que avaliaram como "excelente".
# O total de clientes que avaliaram como "péssimo".
# A porcentagem de clientes que avaliaram como "bom" em relação ao total.
 
qtdExellente = 0
totalIdadeExcellente = 0
qtdPessimo = 0
totalIdadePessimo = 0
qtdBom = 0
totalIdadeBom = 0
qtdRegular = 0
totalIdadeRegular = 0

for contador in range (1, 41):
    idade = int(input("Digite a idade do cliente: "))
    avaliacao = int(input("Digite a avaliação do cliente (1-péssimo, 2-regular, 3-bom, 4-excelente): "))

    if avaliacao == 4:
        qtdExellente += 1
        totalIdadeExcellente += idade
    elif avaliacao == 1:
        qtdPessimo += 1 
        totalIdadePessimo += idade
    elif avaliacao == 3:
        qtdBom += 1
        totalIdadeBom += idade
    elif avaliacao == 2:
        qtdRegular += 1
        totalIdadeRegular += idade
        


    if qtdExellente > 0:
        mediaIdadeExcellente = totalIdadeExcellente / qtdExellente
    else:
        mediaIdadeExcellente = 0

    porcentagemBom = (qtdBom / 40) * 100

    print(f"Média de idade dos clientes que avaliaram como 'excelente': {mediaIdadeExcellente:.2f}")
    print(f"Total de clientes que avaliaram como 'péssimo': {qtdPessimo}")
    print(f"Porcentagem de clientes que avaliaram como 'bom': {porcentagemBom:.2f}%")