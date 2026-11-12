#1- Faça um fluxograma que leia um número inteiro de 1 a 7 e informe 
# o dia da semana correspondente, sendo domingo o dia de número Se 
# o número não corresponder a um dia da semana, mostre uma mensagem de erro.

numero = int(input("Digite um número inteiro de 1 a 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Erro! Número inválido. Digite um número de 1 a 7.")