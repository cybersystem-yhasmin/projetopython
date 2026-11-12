#Celsius para Fahrenheit
#Leia uma temperatura em Celsius e converta para Fahrenheit.
#Fórmula:
#F = (C × 9/5) + 32


celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

if celsius > 0:
    print("Temperatura positiva")
elif celsius < 0:
    print("Temperatura negativa")
else:
    print("Temperatura igual a zero")

print("Fahrenheit:", fahrenheit)