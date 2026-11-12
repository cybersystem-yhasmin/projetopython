#9- Uma empresa utiliza os códigos 1 para funcionários do setor administrativo e
#  2 para os funcionários do setor operacional. Faça um programa que receba o código
#  e o salário de 20 funcionários. Calcule e mostre:
# a média salarial do setor administrativo.
# a média salarial do setor operacional.
# o total de salários pagos pela empresa.
# a quantidade de funcionários em cada setor.


codigo = int(input("Digite o codigo do funcionario(1 - administrativo, 2 - operacional): "))
salario = float(input("Digite o salario do funcionario: "))

totalAdministrativo = 0
quantidadeAdministrativo = 0
totalOperacional = 0
quantidadeOperacional = 0

for contador in range (1, 21):
    if codigo == 1:
        totalAdministrativo += salario
        quantidadeAdministrativo += 1
    elif codigo == 2:
        totalOperacional += salario
        quantidadeOperacional += 1

if quantidadeAdministrativo > 0:
    mediaAdministrativo = totalAdministrativo / quantidadeAdministrativo
else:
    mediaAdministrativo = 0

if quantidadeOperacional > 0:
    mediaOperacional = totalOperacional / quantidadeOperacional
else:
    mediaOperacional = 0

totalPagamentos = totalAdministrativo + totalOperacional

print(f"Média salarial do setor administrativo: R$ {mediaAdministrativo:.2f}")
print(f"Média salarial do setor operacional: R$ {mediaOperacional:.2f}")
print(f"Total de salários pagos pela empresa: R$ {totalPagamentos:.2f}")
print(f"Quantidade de funcionários no setor administrativo: {quantidadeAdministrativo}")
print(f"Quantidade de funcionários no setor operacional: {quantidadeOperacional}")