#Crear una funcion que realice operaciones básicas (suma,resta, división y multiplicación), entre dos números

def operaciones (a, b, operacion)->str:
    if operacion == "+":
        return f"El resultado de la suma es: {a + b}"
    elif operacion == "-":
        return f"El resultado de la resta es: {a - b}"
    elif operacion == "x":
        return f"El resultado de la multiplicación es: {a * b}"
    elif operacion == "/":
        if b != 0:
            return f"El resultado de la división es: {a / b}"
        else:
            return f"No es posible dividir por 0"
    else:
        return f"La operación que usted ingresó no es valida"
    
a = float(input("Introduce el primer número:"))
b = float(input("Introduce el segundo número:"))
operacion = input("Introduce la operación que quieres realizar: sumar(+), restar(-), multiplicar(x), dividir(/)")
resultado = operaciones (a, b, operacion)
print(resultado)
