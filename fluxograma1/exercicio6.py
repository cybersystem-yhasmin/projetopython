#6- Imagine que você está criando um aplicativo para um sistema de 
# monitoramento de saúde. Elabore um fluxograma que represente um programa 
# que permita ao usuário inserir seus batimentos cardíacos por minuto e determine se estão 
#abaixo, dentro ou acima da faixa considerada saudável.
#Baixo menor que 60 bpm
#Normal entre 60 bpm e 100 bpm
#Acima mais que 100 bpm


batimentos = int(input("Digite seus batimentos cardíacos por minuto: "))

while batimentos <= 0:
    print("Valor inválido! Digite novamente.")
    batimentos = int(input("Digite seus batimentos cardíacos: "))

if batimentos < 60:
    print("Batimentos baixos!")

elif batimentos <= 100:
    print("Batimentos normais!")

else:
    print("Batimentos acima do normal!")