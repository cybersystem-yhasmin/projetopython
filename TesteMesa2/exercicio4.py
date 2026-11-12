
falhas = 0
risco = 10
while falhas < 3:
    falhas = falhas + 1
    risco = risco + 15
    if risco >= 40:
        status = "Risco alto"
    else:
        status = "Risco controlado"
print(falhas)
print(risco)
print(status)
