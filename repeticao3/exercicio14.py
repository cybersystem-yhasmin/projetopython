#14-Entrada contínua de temperaturas.
#Regras:
#Ignorar valores < -50 ou > 150
#Encerrar com 999
#Contar temperaturas:
#Entre 20 e 80
#Múltiplas de 5
#Que não sejam divisíveis por 10
#Exibir:
#Quantidade válida
#Maior temperatura válida
#Percentual válido sobre total digitado


totalDigitado = 0
validasContagem = 0
maiorTemperatura = 0

temperatura = float(input("Digite a temperatura (999 para encerrar): "))

while temperatura != 999:
    totalDigitado += 1  
    
    if temperatura < -50 or temperatura > 150:
        print("Temperatura fora dos limites (-50 a 150) e será ignorada.")
    else:
        validasContagem += 1
        
        if maiorTemperatura is 0 or temperatura > maiorTemperatura:
            maiorTemperatura = temperatura
          
        if (20 <= temperatura <= 80) and (temperatura % 5 == 0) and (temperatura % 10 != 0):
           
            print("Esta temperatura atende a todos os critérios específicos!")

    temperatura = float(input("Digite a temperatura (999 para encerrar): "))

    percentualValido = (validasContagem / totalDigitado) * 100
    
    print("\n" + "="*30)
    print(f"Quantidade de temperaturas válidas: {validasContagem}")
    
    if maiorTemperatura is not 0:
        print(f"Maior temperatura válida: {maiorTemperatura}°C")
    else:
        print("Maior temperatura válida: Nenhuma foi inserida")
        
    print(f"Percentual de válidas sobre o total: {percentualValido:.2f}%")
    print("="*30)
else:
    print("Nenhuma temperatura foi digitada.")