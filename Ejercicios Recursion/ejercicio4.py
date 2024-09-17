#Realizar una multiplicación a base de sumas
def multiplicacion(a:int,b:int)->int:
    if a==0:
        return 0
    return b+multiplicacion(a-1,b) 
a=int(input("Ingresa el primer número:"))
b=int(input("Ingresa el segundo número:"))
print("La multiplicación de",a,"y",b,"es igual a",multiplicacion(a,b))
