#10.Bolsa de estudos
#Leia a média e a renda familiar.
#O aluno recebe bolsa se:
#média >= 8 E renda <= 3000

media = float(input("Digite sua média: "))
renda = float(input("Digite a renda familiar: "))

if media >= 8 and renda <= 3000:
    print("Bolsa aprovada")
else:
    print("Bolsa não aprovada")