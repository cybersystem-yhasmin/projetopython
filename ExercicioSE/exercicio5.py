#5. Uma empresa deseja aumentar seus preços em 20%. Faça um algoritmo que leia o código e o 
# preço de custo de cada produto e calcule o preço novo. Calcule também, a média dos preços 
# com e sem aumento.Mostre o código e o preço novo de cada produto e, no final, as médias.

codigo = int(input("Digite o código do produto: "))
preco = float(input("Digite o preço de custo: "))

novoPreco = preco * 1.20

print("Código:", codigo)
print("Novo preço:", novoPreco)