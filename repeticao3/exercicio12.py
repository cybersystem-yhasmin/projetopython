#12- Uma sequência de 50 números será informada pelo usuário. Escreva um programa que:
# Conte quantos desses números são múltiplos de 3.
#Exiba a soma de todos os números pares.
somaPares = 0
qtdMultiplos3 = 0

for contador in range(1, 51):
    numero = int(input("Digite um numero:"))
    
    if numero % 3 == 0:
        print(f"{numero} é múltiplo de 3.")
        qtdMultiplos3 += 1
    else:
        print(f"{numero} não é múltiplo de 3.")
    
    if numero % 2 == 0:
        somaPares += numero

print(f"Quantidade de múltiplos de 3: {qtdMultiplos3}")
print(f"Soma dos números pares: {somaPares}")