#9- Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a 
# sua opinião em relação ao filme: ótimo=3, bom=2, regular=1. Faça um fluxograma que receba a 
# idade e a opinião de 15 espectadores e que calcule e mostre:
#A média das idades das pessoas que responderam ótimo
#A quantidade de pessoas que respondeu regular
#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados

contador = 1

soma_idades = 0
quantidade_otimo = 0
quantidade_regular = 0
quantidade_bom = 0

while contador <= 15:

    idade = int(input("Digite a idade: "))
    opiniao = int(input("Digite a opinião (3-Ótimo, 2-Bom, 1-Regular): "))

    if opiniao == 3:
        soma_idades = soma_idades + idade
        quantidade_otimo = quantidade_otimo + 1

    elif opiniao == 1:
        quantidade_regular = quantidade_regular + 1

    elif opiniao == 2:
        quantidade_bom = quantidade_bom + 1

    else:
        print("Opinião inválida!")

    contador = contador + 1

if quantidade_otimo > 0:
    media = soma_idades / quantidade_otimo
    print("Média das idades de quem respondeu ótimo:", round(media, 2))
else:
    print("Ninguém respondeu ótimo.")

porcentagem = (quantidade_bom / 15) * 100

print("Quantidade de pessoas que responderam regular:", quantidade_regular)
print("Porcentagem de pessoas que responderam bom:", round(porcentagem, 2), "%")