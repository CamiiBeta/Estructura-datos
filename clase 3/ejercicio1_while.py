#Ejercicio en clase, creación de un sistema de control de ingreso para evitar el sobrecupo

totalBoletos = int(input("Ingrese el número total de boletos que van a ingresar:"))
boletosIngresados = 0
while boletosIngresados < totalBoletos:
    boletoValido = int(input("¿El boleto es válido?, ingrese el número '1' para si, y el número '2' para no:"))
    if boletoValido == 1:
        print("El boleto fue ingresado correctamente")
        boletosIngresados = boletosIngresados + 1
    elif boletoValido == 2:
        print("El boleto no ess válido por lo tanto no fue ingresado")
    else:
        print("La opción que usted ingresó no es válida, recuerde que debe ingresar e número '1' para sí, y el número '2' para no.")
print("Ya no se permiten más ingresos, todos los boletos fueron ingresados")