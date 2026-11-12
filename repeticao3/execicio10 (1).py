#10- Um professor registrou as notas de 35 alunos em uma prova. 
# Faça um algoritmo que:
# Leia o nome e a nota de cada aluno.
#Informe a média geral da turma.
#Conte quantos alunos tiveram nota acima de 7.

total = 0
acima_de_7 = 0

for contador in range (1, 36):
    nome = input(f"Digite o nome do aluno({contador}): ")
    nota = float(input(f"Digite a nota do aluno {nome}: "))
    total += nota
    if nota > 7:
        acima_de_7 += 1

media = total / 35
print(f"Média geral da turma: {media:.2f}")
print(f"Quantidade de alunos com nota acima de 7: {acima_de_7}")
