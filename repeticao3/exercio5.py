#5- Cada espectador de um cinema respondeu a um questionário no qual 
# constava sua idade e a sua opinião em relação ao filme: ótimo=3, bom=2, regular=1.
#  Faça um programa que receba a idade e a opinião de 15 espectadores e que calcule e mostre: (2 pontos)
#A média das idades das pessoas que responderam ótimo
#A quantidade de pessoas que respondeu regular
#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados

total_idade_otimo = 0 
quantidade_otimo = 0 
quantidade_bom = 0 
quantidade_regular = 0 
idades_otimo = 0

for contador in range(1, 16):
    idade= int(input("Digite a idade do espectador:"))
    opiniao =int(input("Digite a opinião do espectador (3-ótimo, 2-bom, 1-regular):"))
    if opiniao == 3:
        total_idade_otimo += idade
        quantidade_otimo += 1
    elif opiniao == 2:
        quantidade_bom += 1
    else:
        quantidade_regular += 1

if quantidade_otimo > 0:
    media_idade_otimo = total_idade_otimo / quantidade_otimo
else:
    media_idade_otimo = 0

percentagem_bom = (quantidade_bom / 15) * 100

print(f"Média das idades das pessoas que responderam ótimo: {media_idade_otimo:.2f}")
print(f"Quantidade de pessoas que respondeu regular: {quantidade_regular}")
print(f"Percentagem de pessoas que respondeu bom: {percentagem_bom:.2f}%")