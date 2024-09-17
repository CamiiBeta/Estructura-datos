#Sumar los elementos de un Arreglo
import random
def sumarElementos(arreglo:list):
    if len(arreglo) == 0:
        return 0
    return arreglo[0] + sumarElementos(arreglo[1:])
arreglo = [random.randint(1,100) for i in range (5)]
print("Los elementos del arreglo son:",arreglo," y su suma es:",sumarElementos(arreglo))
