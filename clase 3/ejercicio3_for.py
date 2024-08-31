#crear un arreglo con 10 numeros aleatorios imprimir en pantala el promedio de estos numeros:

import random
numeros=[random.randint(1,100) for i in range (10)]
promedio= sum(numeros)/len(numeros)
print("Los 10 números son", numeros, "y el promedio de estos es:", promedio) 