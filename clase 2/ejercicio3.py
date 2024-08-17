#Ejercicio 3
a = int(input("Introduce l primer numero: "))
b = int(input("Introduce el segundo número:"))
operacion = input("Introduce la operación que quieres realizar: sumar(+), restar(-), multiplicar(x), dividir(/)")
if operacion == "+":
    print("El resultado de la suma es", a + b)
elif operacion == "-":
    print("El resultdo de la resta es", a - b)
elif operacion == "x":
    print("El resultado de la multiplicación es", a * b)
elif operacion == "/":
    print("El resultado de la división es", a / b)
else:
    print("La operación que usted ingresó no es valida")