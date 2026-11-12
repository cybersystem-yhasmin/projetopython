#4 atividade da estrutura de repeticao

salario = 0
somaSalario = 0
maiorSalario = 0
qtdAte100 = 0
qtdPessoas = 0
somaFilhos = 0

while salario >= 0:
    salario = float(input("Digite seu salário: "))

    if salario < 0:
        break

    filhos = int(input("Digite a quantidade de filhos: "))

    qtdPessoas += 1
    somaSalario += salario
    somaFilhos += filhos

    if salario > maiorSalario:
        maiorSalario = salario

    if salario <= 100:
        qtdAte100 += 1

if qtdPessoas > 0:
    print("a) Média dos salários:", somaSalario / qtdPessoas)
    print("b) Média de filhos:", somaFilhos / qtdPessoas)
    print("c) Maior salário:", maiorSalario)
    print("d) Percentual com salário até R$ 100,00:", qtdAte100 * 100 / qtdPessoas, "%")
else:
    print("Nenhum dado foi digitado.")