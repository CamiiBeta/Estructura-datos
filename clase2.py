#Ejercicio 1
a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))
c = int(input("Introduce el tercer numero: "))
mayor =max(a,b,c)
menor=min(a,b,c)
print("El numero mayor es:",mayor)
print("El numero menor es:",menor)

#Ejercicio 2
a = int(input("Introduce un numero: "))
if a % 2 == 0:
    print(" El numero", a, "es par")
else :
    print("El numero", a, "es impar")

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

#Ejercicio 4
peso = int(input("Introduce tu peso: "))
altura= float(input("Introduce tu altura en decimal (Ej: 1.70)"))
imc = peso / (altura**2)
if imc > 25:
    print("estas en sobrepeso")
else :
    print("no estas en sobrepeso")





