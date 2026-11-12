producao = 85
meta = 80
falha = False

if producao >= meta and falha == False:
    status = "Produção aprovada"
else:
    status = "Verificar produção"
producao = producao - 10
falha = True
if producao < meta or falha == True:
    status = "Revisão necessária"
print(producao)
print(falha)
print(status)