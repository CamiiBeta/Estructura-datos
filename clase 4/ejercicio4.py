#Crear una función que qenere contraseñas aleatorias, la cantidad de caracteres a generar se 
#evalua por parametros.

import random
caracters=["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", 
    "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", 
    "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", 
    "y", "Y", "z", "Z",1,2,3,4,5,6,7,8,9,0]
def createPassword (longitud):
    newPassword=""
    for i in range(longitud):
        newPassword+=str(random.choice(caracters))
    return newPassword
    
longitud=int(input("Ingrese el número de digitos para la nueva contraseña:"))
password= createPassword(longitud)
print(password)
