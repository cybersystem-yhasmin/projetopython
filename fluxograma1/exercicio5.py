#5- Faça um fluxograma que simule um jogo de pedra, papel e tesoura . 
# O programa deve solicitar a escolha dos jogadores, e determinar o vencedor.
jogar = "sim"

while jogar == "sim":

    jogador1 = input("Jogador 1: pedra, papel ou tesoura? ")
    jogador2 = input("Jogador 2: pedra, papel ou tesoura? ")

    if jogador1 == jogador2:
        print("Empate!")

    elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
         (jogador1 == "papel" and jogador2 == "pedra") or \
         (jogador1 == "tesoura" and jogador2 == "papel"):
        print("Jogador 1 venceu!")

    else:
        print("Jogador 2 venceu!")

    jogar = input("Deseja jogar novamente? (sim/nao): ")
print("Fim do jogo!")