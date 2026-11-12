
desgaste = 0
ciclo = 0

while desgaste < 100:
    ciclo = ciclo + 1

    if ciclo <= 3:
        desgaste = desgaste + 15
    else:
        desgaste = desgaste + 25

    print(ciclo, desgaste)

print("Desgaste final:", desgaste)
print("Ciclos executados:", ciclo)