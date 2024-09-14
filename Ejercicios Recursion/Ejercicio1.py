#Calcular el factorial de un número (n):

"""numero=int(input("Ingresa el número al que le quieres sacar el factorial:"))
suma=1
cont=1
while cont <= numero:
    suma=suma*cont
    cont=cont+1
print("el num fctorial es",suma)"""


def factorial (numero:int,cont:int)->int:
    if cont<=numero:
        return 0
    return cont*factorial(numero,cont)
print (factorial(3,1))
    