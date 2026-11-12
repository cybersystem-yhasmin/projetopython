#11.Empréstimo
#Leia salário e idade.
#O empréstimo pode ser aprovado se:
#salário >= 3000 E idade >= 21.

salario = float(input("Digite seu salário: "))
idade = int(input("Digite sua idade: "))

if salario >= 3000 and idade >= 21:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")