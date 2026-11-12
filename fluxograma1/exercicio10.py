#10- Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma certa cidade, em
#um determinado dia. Para cada casa visitada foi fornecido o número do canal (4, 5, 7, 12) e o
#número de pessoas que estavam assistindo a ele naquela casa. Se a televisão estivesse desligada,
#nada seria anotado, ou seja, esta casa não entraria na pesquisa. Faça um fluxograma que:
#leia um número indeterminado de dados, isto é, o número do canal e o número de pessoas que
#estavam assistindo;
#calcule e imprima a porcentagem de audiência em cada canal. Para encerrar a entrada de dados,
#digite o número do canal zero.

canal4 = 0
canal5 = 0
canal7 = 0
canal12 = 0
total = 0

canal = int(input("Digite o canal (4, 5, 7, 12 ou 0 para sair): "))

while canal != 0:

    if canal == 4:
        pessoas = int(input("Quantas pessoas estavam assistindo? "))
        canal4 = canal4 + pessoas
        total = total + pessoas

    elif canal == 5:
        pessoas = int(input("Quantas pessoas estavam assistindo? "))
        canal5 = canal5 + pessoas
        total = total + pessoas

    elif canal == 7:
        pessoas = int(input("Quantas pessoas estavam assistindo? "))
        canal7 = canal7 + pessoas
        total = total + pessoas

    elif canal == 12:
        pessoas = int(input("Quantas pessoas estavam assistindo? "))
        canal12 = canal12 + pessoas
        total = total + pessoas

    else:
        print("Canal inválido!")

    canal = int(input("Digite o canal (4, 5, 7, 12 ou 0 para sair): "))

if total > 0:
    porcentagem4 = (canal4 / total) * 100
    porcentagem5 = (canal5 / total) * 100
    porcentagem7 = (canal7 / total) * 100
    porcentagem12 = (canal12 / total) * 100

    print("Audiência do canal 4:", round(porcentagem4, 2), "%")
    print("Audiência do canal 5:", round(porcentagem5, 2), "%")
    print("Audiência do canal 7:", round(porcentagem7, 2), "%")
    print("Audiência do canal 12:", round(porcentagem12, 2), "%")

else:
    print("Nenhuma audiência registrada!")