#Generar los primeros n números de la serie Fibonacci. 
#La serie comienza con 0 y 1 y cada numero siguiente es la suma de los dos anteriores

def serieFibonacci (numero:int)->int:
    if numero<2:
        return numero
    return serieFibonacci(numero-1)+serieFibonacci(numero-2)

numero=int(input("Ingrese cúantos números de la serie fibonacci desea crear"))
print("Los primeros", numero, "números de la serie Fibonacci son:")
for i in range(numero):
    print(serieFibonacci(i), end=" ")