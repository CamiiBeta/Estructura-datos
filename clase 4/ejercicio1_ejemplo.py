def calcularFactorial (numero:int)->str|int:
    if numero < 0:
        return "No se puede, valores negativos"
    resultado = 1
    for n in range(1,numero+1):
            resultado = resultado * n
    return resultado
    
numero = int(input("Introduce un número para sacarle factorial:"))
numFactorial= calcularFactorial(numero)
print("El resultado es", numFactorial)
