
volume = 100
entrada = 25
consumo = 40

volume = volume + entrada
volume = volume - consumo

if volume < 70:
    alerta = "Nível baixo"
else:
    alerta = "Nível adequado"

if volume < 50:
    alerta = "Nível crítico"

print(volume)
print(alerta)