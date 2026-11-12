# 13-Simulação de Crescimento Populacional com Evento Crítico
#Duas populações A e B crescem anualmente:
#A cresce 3% ao ano
#B cresce 1,5% ao ano
#A cada 5 anos ocorre uma crise que reduz ambas em 7%.
#Determine em quantos anos A ultrapassa B, considerando valores
#  iniciais informados pelo usuário.
a = float(input("Digite o valor inicial da população A: "))
b = float(input("Digite o valor inicial da população B: "))
ano = 0
while a <= b:
    a += a * 0.03
    b += b * 0.015
    ano += 1

    if ano % 5 == 0:
        a -= a * 0.07
        b -= b * 0.07

    print(f"Ano {ano}: População A = {a:.2f}, População B = {b:.2f}")

print(f"A população A ultrapassou a população B em {ano} anos.")