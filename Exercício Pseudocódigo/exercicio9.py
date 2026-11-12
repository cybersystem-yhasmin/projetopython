#Idade em meses
#Leia a idade de uma pessoa em anos e calcule aproximadamente quantos meses ela viveu.


idade = int(input("Digite sua idade: "))

if idade > 0:
    meses = idade * 12
    print("Sua idade em meses:", meses)
elif idade == 0:
    print("Você tem menos de um ano")
else:
    print("Idade inválida")