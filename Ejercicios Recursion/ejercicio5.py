#Realizar una división a base de restas
def division(a:int,b:int)->int:
    if b==0:
        raise ValueError("El divididendo no puede ser 0")
    if a<b:
        return 0 
    return 1+division(a-b,b) 
a=int(input("Ingresa el primer número:"))
b=int(input("Ingresa el segundo número:"))
print("La división de",a,"y",b,"es igual a",division(a,b))