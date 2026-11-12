otal = 0
temp = 0
cont = 0
maior = 0

for i in range(8):
    nome = input("Nome do município: ")
    pop = int(input("População: "))
    t = float(input("Temperatura: "))

    total += pop
    temp += t

    if pop > 100000:
        cont += 1

    if t > 30:
        print("Temperatura acima de 30:", nome)

    if pop > maior:
        maior = pop
        nome_maior = nome

print("População total:", total)
print("Média da população:", total / 8)
print("Municípios acima de 100 mil:", cont)
print("Média da temperatura:", temp / 8)
print("Maior população:", nome_maior)