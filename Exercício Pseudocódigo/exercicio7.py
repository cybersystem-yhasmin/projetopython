#Horas para minutos
#Leia uma quantidade de horas e informe quantos minutos ela representa.

horas = int(input("Digite a quantidade de horas: "))

for i in range(1, horas + 1):
    print(i, "hora(s) =", i * 60, "minutos")

minutos = horas * 60

print("Total de minutos:", minutos)