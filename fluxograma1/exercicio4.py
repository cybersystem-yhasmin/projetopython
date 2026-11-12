#4- Uma companhia de carros paga a seus empregados um salário de R$ 2000,00 por mês mais uma 
# comissão de R$ 100,00 para cada carro vendido isso se bater a meta de 3 carros vendidos.
#  Faça um fluxograma para calcular e imprimir o salário do vendedor num dado mês.

salario = 2000
carros = 0

quantidade = int(input("Quantos carros foram vendidos? "))

while carros < quantidade:
    carros = carros + 1

if quantidade >= 3:
    comissao = quantidade * 100
else:
    comissao = 0

salario_final = salario + comissao

print("O salário final do vendedor é: R$", salario_final)
print("O vendedor vendeu", quantidade, "carros e recebeu uma comissão de R$", comissao)
print("O salário base do vendedor é: R$", salario)