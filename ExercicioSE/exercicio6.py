#6. Crie um programa que ajude a programar turnos de trabalho em uma empresa. 
# O usuário deve informar o dia da semana (1 a 7, sendo 1 para domingo e 7 para sábado).
#  O programa deve exibir a programação dos turnos:
#Dias úteis (segunda a sexta): Turno Normal
#Sábado: Turno Reduzido
#Domingo: Sem Trabalho

dia = int(input("Digite o dia da semana (1 a 7): "))

if dia == 1:
    print("Domingo: Sem Trabalho")
elif dia == 7:
    print("Sábado: Turno Reduzido")
elif dia >= 2 and dia <= 6:
    print("Dia útil: Turno Normal")
else:
    print("Dia inválido")