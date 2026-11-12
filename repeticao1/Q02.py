#2 atividade da estrutura de repeticao

tabuada = int(input("Digite o número para ver a tabuada: "))
limite = int(input("Digite o limite do cálculo: "))

contador = 1

while contador <= limite:
    resultado = tabuada * contador
    print(tabuada, "x", contador, "=", resultado)
    contador += 1