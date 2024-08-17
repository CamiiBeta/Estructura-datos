#Ejercicio 4
peso = int(input("Introduce tu peso: "))
altura= float(input("Introduce tu altura en decimal (Ej: 1.70)"))
imc = peso / (altura**2)
if imc > 25:
    print("estas en sobrepeso")
else :
    print("no estas en sobrepeso")