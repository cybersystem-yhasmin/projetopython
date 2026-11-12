#2- Controle de Temperatura de Forno
#Um forno industrial inicia com temperatura informada pelo usuário.
#A cada ciclo:
#Se temperatura < 800 → aumenta 50 graus
#Se temperatura ≥ 800 e < 1000 → aumenta 20 graus
#Se temperatura ≥ 1000 → mantém constante
#O sistema deve repetir até:
#Atingir 1000 graus
#Exibir:
#Quantos ciclos foram necessários
#Temperatura final
 
temperatura = int(input("Digite a temperatura inicial do forno: "))

ciclo = 0

while temperatura < 1000:
        ciclo += 1
        if temperatura < 800:
            temperatura += 50
        elif temperatura >= 800 and temperatura < 1000:
            temperatura += 20
        else:
            break
print(f"Quantidade de ciclos: {ciclo}")
print(f"Temperatura final: {temperatura} graus")