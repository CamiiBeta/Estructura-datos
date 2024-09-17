#Calcular el factorial de un número (n):

def factorial (numero:int)->int:
    if numero==0:
        return 1
    return numero*factorial(numero-1)

numero=int(input("ingresa el número al que le quieres sacar factorial:"))
print("el factorial de",numero,"es",factorial(numero))
    