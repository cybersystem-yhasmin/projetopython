#9.Entrada no cinema
#Leia idade e se a pessoa está acompanhada.
#A entrada é permitida se:
#idade >= 18 OU
#idade >= 16 E estiver acompanhada.
 
 
idade = int(input("Digite sua idade: "))
acompanhado = input("Está acompanhado? (sim ou não): ")

if idade >= 18:
    print("Entrada permitida")
elif idade >= 16 and acompanhado == "sim":
    print("Entrada permitida")
else:
    print("Entrada não permitida")