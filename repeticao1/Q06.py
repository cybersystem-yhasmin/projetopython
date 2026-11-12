#6 atividade da estrutura de repeticao

inicio = int(input("Digite o número inicial: "))
intervalo = int(input("Digite o intervalo: "))

if intervalo <= 0:
    print("O intervalo deve ser maior que zero.")
else:
    for contagem in range(inicio, -1, -intervalo):
        print(contagem)