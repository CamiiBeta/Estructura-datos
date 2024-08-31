#Crear una función que convierta temperatura Celeus a Fahrenheit

def temperatura(temperaturaC):
    resultado = (temperaturaC*(9/5))+32
    return resultado

temperaturaC = float(input("Ingresa la temperatura en grados Celcius:"))
temperaturaF = temperatura(temperaturaC)
print ("La temperatura Fahrenheit seria:", temperaturaF)




