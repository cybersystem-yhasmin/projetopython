#8. Faça um programa que permita o cadastro de produtos em uma empresa.
#O usuário deve informar o tipo de produto (Alimento, Bebida, Vestuário).
#O programa deve exibir uma mensagem de confirmação com o tipo de produto 
#cadastrado e se ele é perecível ou não, de acordo com as seguintes regras:
#Alimento: Perecível
#Bebida: Não Perecível
#Vestuário: Não Perecível

produto = input("Digite o tipo de produto (Alimento, Bebida ou Vestuário): ")

if produto == "Alimento":
    print("Produto cadastrado: Alimento")
    print("Perecível")

elif produto == "Bebida":
    print("Produto cadastrado: Bebida")
    print("Não Perecível")

elif produto == "Vestuário":
    print("Produto cadastrado: Vestuário")
    print("Não Perecível")

else:
    print("Tipo de produto inválido!")