#10 atividade da estrutura de repeticao


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